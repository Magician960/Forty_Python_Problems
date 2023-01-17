#You are responsible for writing a program that will simulate logging into a database and
#prompting a user to change their password. All usernames and passwords to the database will
#be stored in a dictionary. Upon entering the correct credentials, your program will prompt the
#user to enter a new password that is a minimum of eight characters long. If the new password
#meets the criteria, it will be accepted, otherwise the new password will be rejected. If the user
#who logged in is the admin, a list of all usernames and passwords will be displayed.

#Welcome message
print("Welcome to the Database Admin Program\n")

#Initialise database
user_database ={"mooman74":{"password":"alskes145",
                            "isAdmin":False},
                "meramo1986":{"password":"kehns010101",
                            "isAdmin":False},
                "nickyD":{"password":"world1star",
                            "isAdmin":False},
                "george2":{"password":"booo3oha",
                            "isAdmin":False},
                "admin00":{"password":"admin1234",
                            "isAdmin":True},
                }

#Ask for user credentials and checks it
current_user_name = input("\nEnter your username: ")

if current_user_name not in user_database.keys():
    print("Username not in database, goodbye.")
    quit()

current_user_pw = input("Enter your password: ")

if user_database[current_user_name]["password"] != current_user_pw:
    print("Password incorrect!")
    quit()
else:
    print(f"\nHello {current_user_name}! You are logged in!")

#Checks for admin status
if user_database[current_user_name]["isAdmin"]:
    print("\nHere is the current user database:")
    #Print userbase
    for user, user_details in user_database.items():
        user_password = user_details["password"]
        print(f"Username: {user}\t\tPassword: {user_password}")
else:
    #Ask whether to change user's password
    if input("Would you like to change your password: ").lower() == "yes":
        new_password = input("What would you like your new password to be: ")
        if len(new_password) < 8:
            print(f"{new_password} not the minimum eight characters.")
        else:
            user_database[current_user_name]["password"] = new_password
            print(f"\n{current_user_name} your password is {new_password}")
    else:
        print("Okay. Goodbye!")
