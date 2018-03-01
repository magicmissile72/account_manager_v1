def menu():
    print()
    print(" " * 22 + "Menu")
    print("-" * 48)
    print("\t1. Enter a new user")
    print("\t2. Delete a new user")
    print("\t3. Update a users password")
    print("\t4. Login")
    print()
    print("\t'Q' to Quit")
    print()
#
def get_command():
    item = input("Enter your choice: ")
    return item
#
def add_user():
    f_name = ""
    l_name = ""
    login = ""
    passw = ""
    print("Add a new user")
    print("-" * 44)
    while f_name == "":
        f_name = input("Enter the new users 'First' name: ")
    while l_name == "":
        l_name = input("Enter the new users 'Last' name: ")
    while login == "":
        login = input("Enter the new users 'login' name: ")
    while passw == "":
        passw = input("Enter the new users 'password' name: ")
    print()
    print("You entered the following:")
    print(f"\tFirst name:\t{f_name}")
    print(f"\tLast name:\t{l_name}")
    print(f"\tLogin name:\t{login}")
    print(f"\tPassword:\t{passw}")
    answer = input("is this information correct (y/n): ")
    if answer == 'n':
        return
    elif answer == 'y':
        database = open("database.txt", 'a')
        database.write(login + "," + f_name + "," + l_name + "," + passw + "\n")
        database.close()
        return
    else:
        print("invalid option")
        return
    
#
def del_user():
    print("Press enter to return to the main menu if you don't know the name")
    remove_user = input("Enter the username/login of the account to delete:\n> ")
    database = open("database.txt", 'r')
    lines = database.readlines()
    database.close()
    database = open("database.txt", 'w')
    database.truncate()
    database.seek(0)
    for line in lines:
        temp = line.split(",")
        if remove_user not in line:
            database.write(line)
    database.close()
#
def cha_pass():
    print("Press enter to return to the main menu if you don't know the new password")
    login_name = input("Enter the username of the account to change the password:\n> ")
    pass_a = input("The new password: ")
    pass_b = input("Repeat the password: ")
    if pass_a != pass_b:
        print("The passwords do not match...")
        return
    database = open("database.txt", 'r')
    lines = database.readlines()
    database.close()
    database = open("database.txt", 'w')
    database.truncate()
    database.seek(0)
    for line in lines:
        temp = line.split(",")
        if login_name not in line:
            database.write(line)
        elif login_name in line:
            database.write(temp[0] + "," + temp[1] + "," + temp[2] + "," + pass_a + "\n")
        else:
            print("Error0xf001")
    database.close()
#
def auth():
    auth_user = input("Login: ")
    auth_pass = input("Pass: ")
    if auth_user != "admin":
        print("Unauthorized account!")
        return
    elif auth_user == "admin":
        database = open("database.txt", 'r')
        lines = database.readlines()
        database.close()
        for line in lines:
            temp = line.split(",")
            if "admin" in line and line[3] == auth_pass:
                return True
            else:
                print("Authetication failed")
                return False
        print("Error: 1001")
#
def login():
    check = auth()
    if check == True:
        print()
    elif check == False:
        return
    else:
            print("Some kind of error")
    database = open("database.txt", 'r')
    lines = database.readlines()
    database.close()
    print(" " * 15 + "Admin Access Only")
    print(" " * 15 + "The User Database")
    print("-" * 48)
    print("Login\tFirst Name\tLast Name\tPassword")
    print("-" * 48)
    for line in lines:
        line.replace("\n","")
        temp = line.split(",")
        print(temp[0] + "\t" + temp[1] + "\t\t" + temp[2] + "\t\t" + temp[3])
    
# -- Main --
# -------------------------------------------------------
while True:
    menu()
    item = get_command()
    if item == '1':
        add_user()
    elif item == '2':
        del_user()
    elif item == '3':
        cha_pass()
    elif item == '4':
        login()
    elif item == 'q' or 'Q':
        print("Thank you for using this program...")
        print("Bye")
        break
    else:
        print("Error")
#database_tmp = open("database.txt.tmp", 'w')
#database_tmp.truncate()
#database = open("database.txt", 'r')

#database_tmp.write()
#database_tmp.close()
#database.close()


# EOF