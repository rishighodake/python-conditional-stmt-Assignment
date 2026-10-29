role = input("Enter a role (admin, user, guest): ").strip().lower()

match role:
    case "admin":
        print("Administrator access.")
    case "user":
        print("Standard user access.")
    case "guest":
        print("Guest access.")
    case _:
        print("Unknown role.")
