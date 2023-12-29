#Unique Morse Code Words
#https://leetcode.com/problems/unique-morse-code-words/description/

caseWords_1 = ["gin","zen","gig","msg"]
caseWords_2 = ["a"]

morseAlphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

if False:
    def uniqueMorseCodeWords(words) -> int:
        myDict = dict()
        for word in words:
            codeWord = ""
            for c in list(word):
                codeWord += morseAlphabet[ord(c) - 97]

            myDict[codeWord] = 1

        return len(myDict)

if True:
    def uniqueMorseCodeWords(words) -> int:
        mySet = set()
        for word in words:
            morseWord = ""
            for c in list(word):
                morseWord += morseAlphabet[ord(c) - 97]
            
            mySet.add(morseWord)
        
        return len(mySet)

print(f"{uniqueMorseCodeWords(caseWords_1)}")
print(f"{uniqueMorseCodeWords(caseWords_2)}")