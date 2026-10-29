grade = input("Enter a grade (A, B, C, Fail): ").strip().upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Pass")
    case "FAIL":
        print("Needs improvement")
    case _:
        print("Invalid grade.")
