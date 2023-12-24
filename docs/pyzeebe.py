import os
import boto3
import datetime
import asyncio
from pyzeebe import (
    ZeebeClient,
    create_camunda_cloud_channel,
)

os.environ['AWS_DEFAULT_REGION'] = 'eu-north-1'

ssm = boto3.client('ssm')

# Specify the parameter path
parameter_path = '/MyApp/Environment/orderID'

# Retrieve the variable from Parameter Store
response = ssm.get_parameter(
    Name=parameter_path,
    WithDecryption=True  # If the parameter is encrypted, decrypt it
)

variable_value = response['Parameter']['Value']

# Now you can use variable_value in your script as needed
output_message = f"{variable_value}"
print(output_message)

# Log to a file
log_file_path = '/home/ubuntu/logfile.txt'
with open(log_file_path, 'a') as log_file:
    log_file.write(f"{datetime.datetime.now()} - {output_message}\n")

async def main():
    # Create a Zeebe client for Camunda Cloud
    grpc_channel = create_camunda_cloud_channel(
        client_id="jnQI~g9ezuFesFTWy4vY2CpmbTRpctP7",
        client_secret="G-bkziwKMmH3HKnRFFtNVbSqO0KvlfpnlrUWyeYw~LgIQJgb0KvJef9zZ0jzgQIi",
        cluster_id="a21c5657-a334-441e-85f8-4d680f16d26f",
        region="bru-2",  # Default is bru-2
    )
    zeebe_client = ZeebeClient(grpc_channel)

    camunda_var = {
        "awsDeploymentSucessfull": True
    }

    try:
        # Publish message
        await zeebe_client.publish_message(name="sqsOrderId", correlation_key=output_message, variables=camunda_var)
        print("Message sent successfully")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Run the asynchronous main function
asyncio.run(main())