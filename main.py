import boto3
import os
from dotenv import load_dotenv
load_dotenv('variable.env')
check=os.getenv("TEST")
flag=1
def options(argument):
    
    command={
        "exit":"Exit out of the program",
        "1":"Check account details"
    }
    if argument=="all":
        return command
    else:
        return command.get(argument)

def menu():
    while(flag!=0):
        menus=options('all')
        
        print('''
        |||\t\t\tAWS PYTHON TOOL\t\t\t||| 
        ''')
        # print(menus['1'])
        for item in menus.keys():
            print("\t"+item+"\t:\t"+menus[item])
        command=input("\n\t|||\t"+"Enter Command"+"\t"+":")
        print(options(command))


def nameCheck(name):
    # print ("This is {name}".format(name=name))
    print (f"This is {name}")
if __name__=="__main__":
    menu()