age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))

if age < 0 or weight < 0:
    print("Please enter a valid age and weight.")
elif 18 <= age <= 65 and weight >= 50:
    print("Eligible to donate blood.")
else:
    print("Not eligible to donate blood.")
