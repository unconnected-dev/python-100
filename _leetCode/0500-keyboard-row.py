#Keyboard Row
#https://leetcode.com/problems/keyboard-row/description/

caseWords_1 = ["Hello","Alaska","Dad","Peace"]
caseWords_2 = ["omk"]
caseWords_3 = ["adsdf","sfd"]

if True:
    def findWords(words):

        rWords = []
        for word in words:
            characterSet = set()
            characterSet.update(set(word.lower()))

            if all(c in "qwertyuiop" for c in characterSet) or all(c in "asdfghjkl" for c in characterSet) or all(c in "zxcvbnm" for c in characterSet):
                rWords.append(word)
                
        return rWords
    
print(f"{findWords(caseWords_1)}")
print(f"{findWords(caseWords_2)}")
print(f"{findWords(caseWords_3)}")