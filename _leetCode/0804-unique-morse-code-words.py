#Unique Morse Code Words
#https://leetcode.com/problems/unique-morse-code-words/description/

caseWords_1 = ["gin","zen","gig","msg"]
caseWords_2 = ["a"]

morseAlphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

if False:
    def uniqueMorseCodeWords1(words):
        myDict = dict()
        for word in words:
            codeWord = ""
            for c in list(word):
                codeWord += morseAlphabet[ord(c) - 97]

            myDict[codeWord] = 1

        print(f"{len(myDict)}")

    uniqueMorseCodeWords1(caseWords_1)
    uniqueMorseCodeWords1(caseWords_2)

if True:
    def uniqueMorseCodeWords2(words):
        mySet = set()
        for word in words:
            morseWord = ""
            for c in list(word):
                morseWord += morseAlphabet[ord(c) - 97]
            
            mySet.add(morseWord)
        
        print(f"{len(mySet)}")
        
    uniqueMorseCodeWords2(caseWords_1)
    uniqueMorseCodeWords2(caseWords_2)