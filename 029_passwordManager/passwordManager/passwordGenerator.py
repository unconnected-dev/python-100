#Password Generator
#Create a random password string depending on user input
#From day 005

from random import randint

class PasswordGenerator:

    def makePassword(self):
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

        nrLetters = randint(8, 10)
        nrNumbers = randint(2, 4)
        nrSymbols = randint(2, 4)

        pickedCharacters = []

        passwordLetters = [letters[randint(0, len(letters) - 1)] for _ in range(1, nrLetters + 1)]
        passwordNumbers = [numbers[randint(0, len(numbers) - 1)] for _ in range(1, nrNumbers + 1)]
        passwordSymbols = [symbols[randint(0, len(symbols) - 1)] for _ in range(1, nrSymbols + 1)]

        pickedCharacters = passwordLetters + passwordNumbers + passwordSymbols

        #.shuffle is a thing that can be used on lists
        #instead of the random selection below
        totalCharacters = len(pickedCharacters)
        password = ""
        for i in range(1, totalCharacters + 1):
            char = pickedCharacters.pop(randint(0, len(pickedCharacters) - 1))
            password += char

        return password