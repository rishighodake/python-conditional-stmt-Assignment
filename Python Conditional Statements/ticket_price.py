age = int(input("Enter the person's age: "))
base_price = 100

if age < 0:
    print("Please enter a valid age.")
elif age < 5:
    print("The ticket is free.")
elif age < 18:
    print("The ticket price is", base_price / 2)
else:
    print("The ticket price is", base_price)
