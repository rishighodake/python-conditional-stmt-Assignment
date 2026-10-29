password = input("Enter a password: ")

if password:
    if len(password) >= 8:
        print("The password is valid.")
    else:
        print("The password is invalid: it must be at least 8 characters long.")
else:
    print("The password is invalid: it cannot be empty.")
