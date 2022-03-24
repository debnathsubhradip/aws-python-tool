import boto3
import os
from dotenv import load_dotenv
import json
load_dotenv()
accesskeyid=os.getenv("ACCESS-KEY-ID")
secretaccesskey=os.getenv("SECRET-ACCESS-KEY")

session = boto3.Session(
    aws_access_key_id=accesskeyid,
    aws_secret_access_key=secretaccesskey
)

def check_service():
    available_services=session.get_available_services()
    print('Available Services :')
    for item in available_services:
        print(str(item))


# check the code below this --> This was to check if the Instances are running fine or not. and by how much and its details
def check_ec2_service():
    client = session.client("ec2", region_name="us-west-2")
    response = client.describe_instances(
    Filters=[
        {   'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)
    return response

print(json.dumps(check_ec2_service()))
# check_ec2_service()

