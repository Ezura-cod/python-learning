register_user_username = input("Enter your username: ")
register_user_password = input("Enter your password: ")
print("User registered successfully!")
login_user_username = input("Enter your username to login: ")
login_user_password = input("Enter your password to login: ")
if login_user_username == register_user_username and login_user_password == register_user_password:
    print("Login successful!")
else:
    print("Invalid username or password.")
