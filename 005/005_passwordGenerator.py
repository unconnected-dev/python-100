#Password Generator
#Create a random password string depending on user input

import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator")
nrLetters = int(input("How many letters would you like in your password?\n"))
nrNumbers = int(input("How many numbers would you like?\n"))
nrSymbols = int(input("How many symbols would you like?\n"))

pickedCharacters = []

#.choice could have been used on lists
for i in range(1, nrLetters + 1):
    pickedCharacters.append(letters[random.randint(0, len(letters) - 1)])

for i in range(1, nrNumbers + 1):
    pickedCharacters.append(numbers[random.randint(0, len(numbers) - 1)])

for i in range(1, nrSymbols + 1):
    pickedCharacters.append(symbols[random.randint(0, len(symbols) - 1)])


#.shuffle is a thing that can be used on lists
#instead of the random selection below
totalCharacters = len(pickedCharacters)
password = ""
for i in range(1, totalCharacters + 1):
    char = pickedCharacters.pop(random.randint(0, len(pickedCharacters) - 1))
    password += char

print(f"Your password is: {password}")