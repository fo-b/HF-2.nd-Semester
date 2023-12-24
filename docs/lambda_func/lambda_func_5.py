import base64
import string
import random
import json
import boto3
import os


def get_latest_ami(os_type):
    ec2 = boto3.client('ec2')
    filters = [
        {'Name': 'architecture', 'Values': ['x86_64']},
        {'Name': 'state', 'Values': ['available']},
        {
            'Name': 'name',
            'Values': [
                f'{os_type.lower()}*jammy-22.04-amd64-server*',
                f'al2023-ami-2023.2.2023*',
            ],
        },
    ]

    images = ec2.describe_images(Filters=filters, Owners=['amazon'])

    # Sort images by creation date in descending order
    sorted_images = sorted(images['Images'], key=lambda x: x['CreationDate'], reverse=True)

    if sorted_images:
        return sorted_images[0]['ImageId']
    else:
        raise Exception(f"No available stable server AMI found for {os_type}.")


def get_default_subnet():
    ec2 = boto3.client('ec2')
    response = ec2.describe_subnets(Filters=[{'Name': 'default-for-az', 'Values': ['true']}])

    if response['Subnets']:
        return {'SubnetId': response['Subnets'][0]['SubnetId']}
    else:
        raise Exception("No default subnet found.")
        
def get_default_vpc():
    ec2 = boto3.client('ec2')
    response = ec2.describe_vpcs(Filters=[{'Name': 'isDefault', 'Values': ['true']}])

    if response['Vpcs']:
        return {'VpcId': response['Vpcs'][0]['VpcId']}
    else:
        raise Exception("No default VPC found.")
        
def create_security_group(group_name, description, vpc_id):
    ec2 = boto3.client('ec2')

    response = ec2.create_security_group(
        GroupName=group_name,
        Description=description,
        VpcId=vpc_id
    )

    # Get the newly created security group ID
    security_group_id = response['GroupId']

    # Authorize inbound traffic for SSH (port 22) and HTTP (port 80)
    ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
        ]
    )

    return security_group_id

def lambda_handler(event, context):
    # Extract SQS message body
    sqs_messages = event['Records']

    for sqs_message in sqs_messages:
        sqs_body = json.loads(sqs_message['body'])
    
        # Create a new security group and get its ID
        random_number = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        security_group_name = f"wubwubpoop-{random_number}"
        security_group_description = "Security group for EC2 instance"
        vpc_id = get_default_vpc()['VpcId']
        security_group_id = create_security_group(security_group_name, security_group_description, vpc_id)
    
        # Extract information from the SQS input sqs_body
        process_instance_id = sqs_body["orderID"]
        surname = sqs_body["surname"]
        lastname = sqs_body["lastname"]
        department = sqs_body["department"]
        email = sqs_body["email"]
        order_description = sqs_body["orderDescription"]
        instance_name = sqs_body["instanceName"]
        ami = sqs_body["ami"]
        instance_type = sqs_body["instanceType"]
        environment = sqs_body["environment"]
        network_subnet = sqs_body["networkSubnet"]
        firewall_profiles = sqs_body["firewallProfiles"]
        public_ip = sqs_body["publicIP"]
        state = sqs_body["state"]
        user_data = sqs_body["userData"]
        cost_center = sqs_body["costCenter"]
        
        if state.lower() == "stopped":
            # Get the instance ID based on the provided ProcessInstanceId
            ec2 = boto3.client('ec2')
            response = ec2.describe_instances(
                Filters=[
                    {'Name': 'tag:ProcessInstanceID', 'Values': [process_instance_id]},
                    {'Name': 'instance-state-name', 'Values': ['running']}
                ]
            )
    
            instances = response.get('Reservations', [])
    
            if instances:
                instance_id_to_stop = instances[0]['Instances'][0]['InstanceId']
                ec2.stop_instances(InstanceIds=[instance_id_to_stop])
                print(f"EC2 instance {instance_id_to_stop} stopped successfully.")
    
                return {
                    'statusCode': 200,
                    'body': f'EC2 instance {instance_id_to_stop} stopped successfully.'
                }
            else:
                print(f"No running EC2 instance found with ProcessInstanceID {process_instance_id}.")
                return {
                    'statusCode': 404,
                    'body': f'No running EC2 instance found with ProcessInstanceID {process_instance_id}.'
                }
        
        # Check if the state is "deleted"
        if state.lower() == "deleted":
            # If the state is "deleted," find the EC2 instance with the given ProcessInstanceId
            ec2 = boto3.client('ec2')
            response = ec2.describe_instances(Filters=[
                {'Name': 'tag:ProcessInstanceID', 'Values': [process_instance_id]}
            ])
    
            # Check if there are running instances with the given ProcessInstanceId
            instances = response.get('Reservations', [])
            if instances:
                instance_id_to_delete = instances[0]['Instances'][0]['InstanceId']
                ec2.terminate_instances(InstanceIds=[instance_id_to_delete])
                print(f"EC2 instance {instance_id_to_delete} is being terminated.")
                return {
                    'statusCode': 200,
                    'body': f'EC2 instance {instance_id_to_delete} is being terminated.'
                }
            else:
                print(f"No running instances found with ProcessInstanceId {process_instance_id}. Nothing to delete.")
                return {
                    'statusCode': 404,
                    'body': f'No running instances found with ProcessInstanceId {process_instance_id}. Nothing to delete.'
                }
        
        # Check if the state is "restarted"
        if state.lower() == "restarted":
            # If the state is "restarted," find the EC2 instance with the given ProcessInstanceId
            ec2 = boto3.client('ec2')
            response = ec2.describe_instances(Filters=[
                {'Name': 'tag:ProcessInstanceID', 'Values': [process_instance_id]}
            ])
        
            # Check if there are running instances with the given ProcessInstanceId
            instances = response.get('Reservations', [])
            if instances:
                instance_id_to_restart = instances[0]['Instances'][0]['InstanceId']
                
                # Reboot the specified EC2 instance
                ec2.reboot_instances(InstanceIds=[instance_id_to_restart])
        
                print(f"EC2 instance {instance_id_to_restart} is being restarted.")
                return {
                    'statusCode': 200,
                    'body': f'EC2 instance {instance_id_to_restart} is being restarted.'
                }
            else:
                print(f"No running instances found with ProcessInstanceId {process_instance_id}. Nothing to restart.")
                return {
                    'statusCode': 404,
                    'body': f'No running instances found with ProcessInstanceId {process_instance_id}. Nothing to restart.'
                }

    
    # Add a shebang line and encode user data to base64
    cloud_init_script = "#!/bin/bash\n" + user_data
    encoded_user_data = base64.b64encode(cloud_init_script.encode('utf-8')).decode('utf-8')

    # Update the event dictionary with the encoded user data
    event["userData"] = encoded_user_data

    # Initialize EC2 client
    ec2 = boto3.client('ec2')

    # Map AMI to the latest image ID
    if ami.lower() == 'ubuntu':
        ami = get_latest_ami('ubuntu')
    elif ami.lower() == 'amazon_linux':
        ami = get_latest_ami('amazon')

    # Map subnet to an existing subnet in the same region
    network_subnet = get_default_subnet()

    # Create EC2 instance
    response = ec2.run_instances(
        ImageId=ami,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        UserData=encoded_user_data,
        SecurityGroupIds=[security_group_id],
        SubnetId=network_subnet['SubnetId'],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': instance_name},
                    {'Key': 'Environment', 'Value': environment},
                    {'Key': 'Department', 'Value': department},
                    {'Key': 'orderID', 'Value': str(process_instance_id)},
                    {'Key': 'Cost center', 'Value': cost_center},
                ]
            },
        ]
    )

    # Wait for the instance to be running and obtain its public IP
    instance_id = response['Instances'][0]['InstanceId']
    ec2_resource = boto3.resource('ec2')
    instance = ec2_resource.Instance(instance_id)
    instance.wait_until_running()

    # Get the public IP address
    public_ip = instance.public_ip_address
    
    #When Instance is up running make SSH connection to CamundaFeedback & send Response back to Camunda

    ssm = boto3.client('ssm')

    variable_value = str(process_instance_id)
    
    ssm.put_parameter(
        Name='/MyApp/Environment/orderID',
        Value=variable_value,
        Type='String',
        Overwrite=True
    )
        
        
    print(f"EC2 instance {instance_id} created successfully.")
    print(f"Public IP address of the created instance {public_ip}")

    return {
        'statusCode': 200,
        'body': f'EC2 instance {instance_id} created successfully.'
    }