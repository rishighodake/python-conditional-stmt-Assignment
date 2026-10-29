first_number = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

match operator:
    case "+":
        print("Result:", first_number + second_number)
    case "-":
        print("Result:", first_number - second_number)
    case "*":
        print("Result:", first_number * second_number)
    case "/":
        if second_number == 0:
            print("Cannot divide by zero.")
        else:
            print("Result:", first_number / second_number)
    case _:
        print("Invalid operator.")
