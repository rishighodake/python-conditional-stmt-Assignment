result = input("Enter result status (pass or fail): ").strip().lower()

match result:
    case "pass":
        print("Congratulations, you passed.")
    case "fail":
        print("You did not pass.")
    case _:
        print("Invalid result status.")
