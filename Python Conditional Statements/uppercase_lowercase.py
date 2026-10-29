character = input("Enter a character: ")

if len(character) != 1 or not character.isalpha():
    print("Please enter a single alphabetic character.")
elif character.isupper():
    print("The character is uppercase.")
else:
    print("The character is lowercase.")
