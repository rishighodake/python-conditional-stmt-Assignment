print("1. Python")
print("2. Java")
print("3. C++")
choice = input("Choose a language (1-3): ")

match choice:
    case "1":
        print("You chose Python.")
    case "2":
        print("You chose Java.")
    case "3":
        print("You chose C++.")
    case _:
        print("Invalid choice.")
