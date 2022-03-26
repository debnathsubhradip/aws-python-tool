import subdir.control as control
flag=1
def options(argument):
    
    command={
        "exit":"Exit out of the program",
        "1":"Check account details",
        "2":"Check EC2 Details"
    }
    if argument=="all":
        return command
    if argument=="exit":
        exit(0)
    elif argument=="1":
        control.check_service()
    elif argument=="2":
        control.check_ec2_service()
    # else:
    #     return command.get(argument)

def menu():
    while(flag!=0):
        menus=options('all')
        
        print('''
        |||\t\t\tAWS PYTHON TOOL\t\t\t||| 
        ''')
        for item in menus.keys():
            print("\t"+item+"\t:\t"+menus[item])
        command=input("\n\t|||\t"+"Enter Command"+"\t"+":")
        options(command)


def nameCheck(name):
    # print ("This is {name}".format(name=name))
    print (f"This is {name}")
if __name__=="__main__":
    menu()