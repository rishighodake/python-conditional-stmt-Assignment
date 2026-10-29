month_number = int(input("Enter a month number (1-12): "))

match month_number:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 days")
    case 4 | 6 | 9 | 11:
        print("30 days")
    case 2:
        print("28 days")
    case _:
        print("Please enter a number from 1 to 12.")
