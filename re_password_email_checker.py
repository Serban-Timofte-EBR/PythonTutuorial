import re

flag = True

while flag:
    emailPattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)") #local usage only to avoid global variables
    email = input("Enter your email: ")
    a = emailPattern.search(email)

    if a != None:
        flag = False
        print("Email valid")
    else:
        print("Invalid email! Try again")

flag = True

while flag:
    passwordPattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$") #local usage only to avoid global variables
    password = input("Enter your password: ")
    b = passwordPattern.search(password)

    if b != None:
        flag = False
        print("Password valid")
    else:
        print("Invalid password! Try again")

del flag
