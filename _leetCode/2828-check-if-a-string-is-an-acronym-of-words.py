#Check If A String Is An Acronym Of Words
#https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/

caseWords_1 = ["alice","bob","charlie"]
caseS_1 = "abc"

caseWords_2 = ["an","apple"]
caseS_2 = "a"

caseWords_3 = ["never","gonna","give","up","on","you"]
caseS_3 = "ngguoy"

if False:
    def isAcronym(words, s):
        arr = []
        for word in words:
            arr.append(word[0])
        
        return ''.join(arr) == s

if False:
    def isAcronym(words, s):
        arr = [0] * len(words)
        for i in range(len(words)):
            arr[i] = words[i][0]
        
        return ''.join(arr) == s

if True:
    def isAcronym(words, s):
        res = ""
        for i in range(len(words)):
            res += words[i][0]

        return res == s

print(f"{isAcronym(caseWords_1, caseS_1)}")
print(f"{isAcronym(caseWords_2, caseS_2)}")
print(f"{isAcronym(caseWords_3, caseS_3)}")