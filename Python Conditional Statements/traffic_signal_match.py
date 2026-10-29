signal = input("Enter a traffic signal color (red, yellow, green): ").lower()

match signal:
    case "red":
        print("Stop.")
    case "yellow":
        print("Wait.")
    case "green":
        print("Go.")
    case _:
        print("Unknown traffic signal.")
