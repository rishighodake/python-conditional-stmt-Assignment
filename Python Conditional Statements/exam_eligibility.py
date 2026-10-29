attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter marks: "))

if attendance >= 75:
    if marks >= 40:
        print("The student is eligible for the exam.")
    else:
        print("The student is not eligible: marks are below 40.")
else:
    print("The student is not eligible: attendance is below 75%.")
