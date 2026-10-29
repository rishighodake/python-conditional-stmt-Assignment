character = input("Enter a character: ")

if len(character) != 1 or not character.isalpha():
    print("Please enter a single alphabetic character.")
elif character.lower() in "aeiou":
    print("The character is a vowel.")
else:
    print("The character is a consonant.")
