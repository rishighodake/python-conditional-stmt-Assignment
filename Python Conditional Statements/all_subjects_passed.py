subject_count = int(input("Enter the number of subjects: "))

if subject_count <= 0:
    print("Enter a positive number of subjects.")
else:
    passed_all = True

    for subject_number in range(1, subject_count + 1):
        marks = float(input(f"Enter marks for subject {subject_number}: "))
        if marks < 40:
            passed_all = False

    if passed_all:
        print("The student passed all subjects.")
    else:
        print("The student did not pass all subjects.")
