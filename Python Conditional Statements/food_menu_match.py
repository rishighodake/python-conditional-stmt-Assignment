print("1. Pizza")
print("2. Burger")
print("3. Pasta")
print("4. Salad")
choice = input("Choose a food item (1-4): ")

match choice:
    case "1":
        print("You selected Pizza.")
    case "2":
        print("You selected Burger.")
    case "3":
        print("You selected Pasta.")
    case "4":
        print("You selected Salad.")
    case _:
        print("Invalid selection.")
