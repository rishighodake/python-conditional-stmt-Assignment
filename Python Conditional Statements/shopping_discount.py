total = float(input("Enter the total shopping amount: "))

if total < 0:
    print("The shopping amount cannot be negative.")
elif total < 100:
    discount_rate = 0
elif total < 500:
    discount_rate = 0.05
else:
    discount_rate = 0.10

if total >= 0:
    discount = total * discount_rate
    print(f"Discount: {discount:.2f}")
    print(f"Amount to pay: {total - discount:.2f}")
