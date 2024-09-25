import csv

admin={
    "name":"irfan",
    "id":1432
}
owner_details={
    "name":"junaid",
    "id":1234
}




def admine(admin):
    print("admin athentication")
    admin_name=input("enter admin name")
    admin_id=int(input("enter admin id"))
    if admin_name==admin["name"] and admin_id==admin["id"]:
        print("admin aproved")
        return True
    else:
        print("check your name or id carefully")
        
        
        


def owner(owner_details):
    print("owner athentication")
    owner_name=input("enter owner name")
    owner_id=int(input("enter owner id"))
    if owner_name==owner_details["name"] and owner_id==owner_details["id"]:
        print("owner aproved")
        return True
    else:
        print("check your name or id carefully")
        

def company_account():
    
    data = []
    field=["company_name","company_id"]

    while True:
        name = input("Enter your company name: ")
        id = int(input("Enter your id: "))
        data.append([name, id])
        break

    with open('data.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(field)
        csv_writer.writerows(data)

        print("create company successfully")
def user_account():
    
    data = []
    field=["user_name","user_id"]

    while True:
        name = input("Enter your user name: ")
        id = int(input("Enter your id: "))
        data.append([name, id])
        break

    with open('user.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(field)
        csv_writer.writerows(data)

        print("create user successfully")




running=True
while running==True:
    print("....Select your role....\n..1: Admin..\n..2: owner..\n..3: user..\n..0: stop..")
    select=int(input("enter your post:"))
    if select==1:
        if admine(admin)==True:
            run=True
            while run==True:
                
                print(".... owner athentication....\n....1: create accounts for company....\n...2: create user account...\n...3: manage income....\n....3: manage reports....\n....0: stop operations....")
                    
                choice= int(input("enter your choice"))
                
                if choice == 1:
                    print("create account for company")
                    
                    company_account()
                elif choice == 2:
                    print("create user account")
                    user_account()
                elif choice == 3:
                    print("manage income")
                elif choice == 4:
                    print("manage reports")
                elif choice == 0:
                    print("exit")
                    run=False
                else:
                    print("invalid operation")
                    run=False
        
    elif select==2:
        if owner(owner_details)==True:
            run=True
            while run==True:
                
                print("....1: create user account....\n....2: manage income....\n....3: manage reports....\n....0: stop operations....")
                    
                choice= int(input("enter your choice"))
                
                
                if choice == 1:
                    print("create user account")
                    user_account()
                elif choice == 2:
                    print("manage income")
                elif choice == 3:
                    print("manage reports")
                elif choice == 0:
                    print("exit")
                    run=False
                else:
                    print("invalid operation")
                    run=False
    elif select==3:
        print("User")
        run=True
        while run==True:
            
            print("....1: manage income....\n....2: manage reports....\n....0: stop operations....")
                
            choice= int(input("enter your choice"))
            
           
            if choice == 1:
                print("manage income")
            elif choice == 2:
                print("manage reports")
            elif choice == 0:
                print("exit")
                run=False
            else:
                print("invalid operation")
                run=False
    elif select==0:
        print("exit")
        running=False
    else:
        running=False
        