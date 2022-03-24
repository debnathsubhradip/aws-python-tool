import boto3
import os
from dotenv import load_dotenv
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

