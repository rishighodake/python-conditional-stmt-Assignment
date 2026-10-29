age = int(input("Enter age: "))

if age < 0:
    print("Please enter a valid age.")
elif age >= 18:
    print("Eligible to apply for a driving license.")
else:
    print("Not eligible to apply for a driving license.")
