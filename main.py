import boto3
import os
from dotenv import load_dotenv
load_dotenv('variable.env')
check=os.getenv("TEST")
def nameCheck(name):
    # print ("This is {name}".format(name=name))
    print (f"This is {name}")
if __name__=="__main__":
    nameCheck(check)