#Unique Morse Code Words
#https://leetcode.com/problems/unique-morse-code-words/description/

caseWords_1 = ["gin","zen","gig","msg"]
caseWords_2 = ["a"]

morseAlphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

if True:
    def uniqueMorseCodeWords(words):
        myDict = dict()
        for word in words:
            codeWord = ""
            for c in list(word):
                codeWord += morseAlphabet[ord(c) - 97]

            if codeWord != "":
                myDict[codeWord] = 1

        print(f"{len(myDict)}")

    uniqueMorseCodeWords(caseWords_1)
    uniqueMorseCodeWords(caseWords_2)