age = int(input("Enter age: "))
monthly_income = float(input("Enter monthly income: "))

if age < 0 or monthly_income < 0:
    print("Please enter a valid age and income.")
elif age >= 21 and monthly_income >= 25000:
    print("Eligible to apply for a loan.")
else:
    print("Not eligible to apply for a loan.")
