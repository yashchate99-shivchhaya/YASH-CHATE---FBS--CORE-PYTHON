correct_id = "admin"
correct_password = "1234"

for i in range(3):

    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")

    if user_id == correct_id and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Invalid User ID or Password")

else:
    print("Account Locked")