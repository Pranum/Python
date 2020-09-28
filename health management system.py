# # # Health Management System

client_list={1:"Ankita",2:"Snehal",3:"Kasturi"}
log_list = {1:"excercise",2:"diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Enter client name")
    for key, value in client_list.items():
        print("press",key, "for", value,"\n", end="")
    client_name=int(input())
    print("selected job:",client_list[client_name],"\n",end="")
    print("press 1 for log")
    print("2 for retrieve")
    op=int(input())

    if op==1:
        for key, value in log_list.items():
            print("press",key, "to log", value,"\n", end="")
        log_name=int(input())
        print("selected job",log_list[log_name],"\n", end="")
        f=open(client_list[client_name]+"_"+log_list[log_name]+".txt","a")
        k="y"
        while (k !="n"):
            print("Enter",log_list[log_name],"\n",end="")
            mtxt=input()
            f.write("["+str(getdate())+"]:"+mtxt+"\n")
            k= input("ADD MORE?y/n")
            continue
        f.close()

    elif op==2:
        for key, value in log_list.items():
            print("press",key,"to retrieve",value,"\n",end="")
        log_name = int(input())
        print("selected job:",client_list[client_name],"_",log_list[log_name],"Report:","\n",end="")
        f=open(client_list[client_name]+"_"+log_list[log_name]+".txt","rt")
        a=f.readlines()
        for line in a:
            print(line,end="")
        f.close()
    else:
        print("Invalid entry")
except Exception as e:
    print("Wrong entry!!")







