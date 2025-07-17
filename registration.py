while True:
    print("1. Registration")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter your choice : "))
    if choice==1:
        a=input("Enter the name: ")
        b=input("Enter the address: ")
        c=int(input("Enter the age: "))
        if int (c) <= 18:
           continue
        d=input("Enter the Username: ")
        e=int(input("Enter the Password: "))
        f=input("Enter the Phone number: ")
        if len(f) == 10:
            print("verifed number")
        else:
            print("Invalid")
    elif choice==2:
        g=input("Enter the Username: ")
        h=int(input("Enter the Password: "))
        if g==d and h==e:
            print("login successfull")
            print("The details: ")
            print("name :",a)
            print("address :",b)
            print("age :",c)
            print("username :",d)
            print("password :",e)
            print("phone number :",f)
        else:
            print("wrong username or password")
    elif choice==3:

        break 
