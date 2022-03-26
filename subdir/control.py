from re import L
import boto3
import os
from dotenv import load_dotenv
import json
load_dotenv()
accesskeyid=os.getenv("ACCESS-KEY-ID")
secretaccesskey=os.getenv("SECRET-ACCESS-KEY")
aws_regions=["us-east-2","us-east-1","us-west-1","us-west-2","af-south-1","ap-east-1","ap-southeast-3","ap-south-1","ap-northeast-3","ap-northeast-2","ap-southeast-1","ap-southeast-2","ap-northeast-1","ca-central-1","eu-central-1","eu-west-1","eu-west-2","eu-south-1","eu-west-3","eu-north-1","me-south-1","sa-east-1"]
# aws_regions=["us-east-1"]


# Boto3 Session
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
    return_response={
    'ctr_pending':0,
    'ctr_running':0,
    'ctr_shutting_down':0,
    'ctr_terminated':0,
    'ctr_stopping':0,
    'ctr_stopped':0
    }
    for region in aws_regions:
        try:
            client = session.client("ec2", region_name=str(region))
            
            # Pending
            response_pending = client.describe_instances(
            Filters=[
                {   'Name': 'instance-state-name',
                    'Values': ['pending']
                }
            ]
            )
            if (response_pending['Reservations'])!=[]:
                return_response['ctr_pending']=len(response_pending['Reservations'])
            
            # Running
            response_running = client.describe_instances(
            Filters=[
                {   'Name': 'instance-state-name',
                    'Values': ['running']
                }
            ]
            )

            if (response_running['Reservations'])!=[]:
                return_response['ctr_running']=len(response_running['Reservations'])
            
            # Shutting Down
            response_shutting_down = client.describe_instances(
            Filters=[
                {   'Name': 'instance-state-name',
                    'Values': ['shutting-down']
                }
            ]
            )
            if (response_shutting_down['Reservations'])!=[]:
                return_response['ctr_shutting_down']=len(response_shutting_down['Reservations'])
            
            # Terminated
            response_terminated = client.describe_instances(
            Filters=[
                {   'Name': 'instance-state-name',
                    'Values': ['terminated']
                }
            ]
            )
            if (response_terminated['Reservations'])!=[]:
                return_response['ctr_terminated']=len(response_terminated['Reservations'])

            # Stopping
            response_stopping = client.describe_instances(
            Filters=[
                {   'Name': 'instance-state-name',
                    'Values': ['stopping']
                }
            ]
            )
            if (response_stopping['Reservations'])!=[]:
                return_response['ctr_stopping']=len(response_stopping['Reservations'])

            # Stopped
            response_stopped = client.describe_instances(
            Filters=[
                {   'Name': 'instance-state-name',
                    'Values': ['stopped']
                }
            ]
            )
            if (response_stopped['Reservations'])!=[]:
                return_response['ctr_stopped']=len(response_stopped['Reservations'])
            
            print(f'''
            AWS EC2 STATS FOR REGION \t-\t {region}
            PENDING EC2 \t=\t {return_response['ctr_pending']}
            RUNNING EC2 \t=\t {return_response['ctr_running']}
            SHUTTING DOWN EC2 \t=\t {return_response['ctr_shutting_down']}
            TERMINATED EC2 \t=\t {return_response['ctr_terminated']}
            STOPPING EC2 \t=\t {return_response['ctr_stopping']}
            STOPPED EC2 \t=\t {return_response['ctr_stopped']}
            ''')
        except:
            print(f"\t\tEITHER AUTHORIZATION FOR KEYS NOT AVAILABLE FOR REGION - {region} OR REGION {region} IS NOT ENABLED")
        return_response['ctr_pending']=0
        return_response['ctr_running']=0
        return_response['ctr_shutting_down']=0
        return_response['ctr_terminated']=0
        return_response['ctr_stopping']=0
        return_response['ctr_stopped']=0
        

