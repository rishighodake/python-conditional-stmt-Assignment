years_of_service = int(input("Enter years of service: "))
annual_salary = float(input("Enter annual salary: "))

if years_of_service < 0 or annual_salary < 0:
    print("Years of service and salary cannot be negative.")
elif years_of_service < 5:
    print("No bonus.")
else:
    bonus = annual_salary * 0.05
    print("Bonus:", bonus)
