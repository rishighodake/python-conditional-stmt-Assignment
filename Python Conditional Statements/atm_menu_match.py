balance = 1000.0

print("1. Check balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")
choice = input("Choose an option (1-4): ")

match choice:
    case "1":
        print(f"Balance: {balance:.2f}")
    case "2":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            print(f"New balance: {balance + amount:.2f}")
        else:
            print("Deposit amount must be positive.")
    case "3":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            print(f"Remaining balance: {balance - amount:.2f}")
    case "4":
        print("Thank you for using the ATM.")
    case _:
        print("Invalid option.")
