year = int(input("Enter a year: "))

if year <= 0:
    print("Please enter a positive year.")
else:
    is_century_year = year % 100 == 0
    is_leap_year = year % 400 == 0 or (year % 4 == 0 and not is_century_year)

    if is_leap_year:
        print("It is a leap year.")
    else:
        print("It is not a leap year.")

    if is_century_year:
        print("It is a century year.")
    else:
        print("It is not a century year.")
