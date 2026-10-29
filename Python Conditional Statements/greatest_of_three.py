first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
third = float(input("Enter the third number: "))

if first >= second and first >= third:
    greatest = first
elif second >= first and second >= third:
    greatest = second
else:
    greatest = third

print("The greatest number is", greatest)
