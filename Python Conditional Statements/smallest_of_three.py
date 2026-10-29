first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
third = float(input("Enter the third number: "))

if first <= second and first <= third:
    smallest = first
elif second <= first and second <= third:
    smallest = second
else:
    smallest = third

print("The smallest number is", smallest)
