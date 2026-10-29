units = float(input("Enter units consumed: "))

if units < 0:
    print("Units consumed cannot be negative.")
elif units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2
else:
    bill = 100 * 1.5 + 100 * 2 + (units - 200) * 3

if units >= 0:
    print(f"Electricity bill: {bill:.2f}")
