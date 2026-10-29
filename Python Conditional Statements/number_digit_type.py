number = int(input("Enter an integer: "))
number_of_digits = len(str(abs(number)))

if number_of_digits == 1:
    print("The number is a single-digit number.")
elif number_of_digits == 2:
    print("The number is a double-digit number.")
elif number_of_digits == 3:
    print("The number is a three-digit number.")
else:
    print("The number has more than three digits.")
