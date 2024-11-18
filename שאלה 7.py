from venv import create

user_name = 0
pasword = 0
valabal = 0
while valabal == 0:
    user = input("a,login\nb,Create a user\nc,logout \n"
                 "d,Back to the main menu \nChoose one from a,b,c,d:")  # בחירות המשתמש
    if valabal == "d":
        valabal == 0
    elif valabal == "b":
        while True:
            create_user = input("please enter your 'ID'")
            if len(user) >= 9 and user.isdigit():
                print("your user is valid ")
                create_user = input("please enter your 'ID'")
                user_name = create_user
                import re
                create_pasword = input("enter your pasword (must include letters and numbers)")
                if re.search("[A-Za-z]", create_pasword) and re.search("[0-9]", create_pasword):
                    print("your pasword is good")
                    pasword = create_pasword
                    break
                else:
                    print("(must include letters and numbers)")
            else:
                (print("please enter at exactly 9 digits "))






            #     break
            # else:
            #     (print("please enter at exactly 9 digits "))










            # create_user = input("please enter your 'ID'")
            # user_name = create_user
            # import re
            #
            # create_pasword = input("enter your pasword (must include letters and numbers)")
            # if re.search("[A-Za-z]", create_pasword and re.search("[0-9]", create_pasword):
