#Caeser Cypher
#Encrypt / Decrypt a user message depending on inputs

import os
import caeserCypherArt

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def hailCaeser(startText, shift, direction):
    if direction == "decode":
        shift = -shift
    
    reply = ""
    for c in startText:
        if c in alphabet:
            pos = (alphabet.index(c) + shift) % 26
            reply += alphabet[pos]
        else:
            reply += c
            
    print("========================================")
    if direction == "encode":
        return(f"Your encrypted message is: {reply}\n")
    elif direction == "decode":
        return(f"Your decrypted message is: {reply}\n")


print(caeserCypherArt.logo)

#Main loop
loopMe = True
while loopMe == True:
    #Get user inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    message = input("Type your message:\n ").lower()

    shiftBy = int(input("Type the shift number:\n"))

    print(hailCaeser(message, shiftBy, direction))
    
    repeat = input("Would you like to go again? y/n \n")

    if repeat == "n":
        loopMe = False
    
    os.system('cls')


print("Goodbye")