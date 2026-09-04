
userList = {
    "admin" : "Admin_123",
    "user" : "User_123",
    "vedant" : "Vedant_123"
}
def user_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    credentials = {
        "username": username,
        "password": password
    }
    return credentials

def add_user(username, password):
    if username in userList:
        print("Username already exists. Please choose a different username.")
        return False
    else:
        userList[username] = password
        print(f"User {username} added successfully.")

        # list of users after adding new user
        print("List of users after adding new user:")
        for username, password in userList.items():
            print(f"Username: {username}, Password: {password}")
        return True

def loginSystem(username, password):

    if(username not in userList):
        print("Username not found. Please try again.")
        return False

    if password == userList[username]:
        return True
    else:
        return False

for i in range(3):
    forCredentials = user_login()

    login_user = loginSystem(forCredentials["username"], forCredentials["password"])
    if login_user == True:
        print(f"Login successful! Welcome {forCredentials['username']}")
        print("1. Add User \n2. Logout \n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_user(username, password)
        elif choice == 2:
            print("Logging out...")
            break
        elif choice == 3:
            print("Exiting...")
            break
        break
    else:
        print(f"Invalid username or password. you have only {2 - i} attempts left. Please try again.")

else:
    print("You have exceeded the maximum login attempts. Account locked. Please contact support.")