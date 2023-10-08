#Hangman
#Player has to input letters to guess a word

import random
import hangmanArt
import hangmanWordList

chosenWord = hangmanWordList.wordList[random.randint(0, len(hangmanWordList.wordList) - 1)]

displayWord = []
for i in range(len(chosenWord)):
    displayWord.append("_")

foundLetter = False
chances = 6
wordComplete = False
guessedLetters = []


# print(chosenWord)
while wordComplete == False and chances > 0:
    #Display the word with unguessed letters hidden
    print(hangmanArt.stages[chances])
    print(displayWord)
    guess = input("Guess a letter: \n").lower()

    #If guess is repeated skip with continue
    if guess in guessedLetters:
        print(f"You have already guessed {guess}")
        continue

    #Go through all letters to reveal on match
    foundLetter = False
    for index, c in enumerate(chosenWord):
        if(c == guess):
            displayWord[index] = c
            foundLetter = True
    
    #If no letter match, player loses a chance
    if foundLetter == False:
        chances -= 1
        print(f"{guess} is not in the word...")
    
    guessedLetters.append(guess)

    #Check if word has been completed
    wordComplete = False
    if "_" not in displayWord:
        wordComplete = True


#Game result message
print(hangmanArt.stages[chances])
if chances != 0:
    print("You win")
else:
    print("You lose")