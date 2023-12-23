import base64
import string
import random
import boto3

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

    security_group_id = response['GroupId']

    ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
        ]
    )

    return security_group_id

def lambda_handler(event, context):
    

    random_number = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    security_group_name = f"wubwubpoop-{random_number}"
    security_group_description = "Security group for EC2 instance"
    vpc_id = get_default_vpc()['VpcId']
    security_group_id = create_security_group(security_group_name, security_group_description, vpc_id)

    process_instance_id = event["ProcessInstanceId"]
    surname = event["surname"]
    lastname = event["lastname"]
    department = event["department"]
    email = event["email"]
    order_description = event["orderDescription"]
    instance_name = event["instanceName"]
    ami = event["ami"]
    instance_type = event["instanceType"]
    environment = event["environment"]
    network_subnet = event["networkSubnet"]
    firewall_profiles = event["firewallProfiles"]
    public_ip = event["publicIP"]
    state = event["state"]
    user_data = event["userData"]
    cost_center = event["costCenter"]
    
    if state.lower() == "stopped":
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
    
    if state.lower() == "deleted":
        ec2 = boto3.client('ec2')
        response = ec2.describe_instances(Filters=[
            {'Name': 'tag:ProcessInstanceID', 'Values': [process_instance_id]}
        ])

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

    if state.lower() == "restarted":
        ec2 = boto3.client('ec2')
        response = ec2.describe_instances(Filters=[
            {'Name': 'tag:ProcessInstanceID', 'Values': [process_instance_id]}
        ])

        instances = response.get('Reservations', [])
        if instances:
            instance_id_to_restart = instances[0]['Instances'][0]['InstanceId']
            
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

    
    cloud_init_script = "#!/bin/bash\n" + user_data
    encoded_user_data = base64.b64encode(cloud_init_script.encode('utf-8')).decode('utf-8')

    event["userData"] = encoded_user_data

    ec2 = boto3.client('ec2')

    if ami.lower() == 'ubuntu':
        ami = get_latest_ami('ubuntu')
    elif ami.lower() == 'amazon_linux':
        ami = get_latest_ami('amazon')

    network_subnet = get_default_subnet()

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
                    {'Key': 'ProcessInstanceID', 'Value': process_instance_id},
                ]
            },
        ]
    )

    instance_id = response['Instances'][0]['InstanceId']
    ec2_resource = boto3.resource('ec2')
    instance = ec2_resource.Instance(instance_id)
    instance.wait_until_running()

    public_ip = instance.public_ip_address

    print(f"EC2 instance {instance_id} created successfully.")
    print(f"Public IP address of the created instance {public_ip}")

    return {
        'statusCode': 200,
        'body': f'EC2 instance {instance_id} created successfully.'
    }