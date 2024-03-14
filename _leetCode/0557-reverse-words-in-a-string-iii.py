#Reverse String III
#https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

caseString_1 = "Let's take LeetCode contest"
caseString_2 = "Mr Ding"

if False:
    def reverseString(s):
        splitString = s.split(" ")

        for i in range(len(splitString)):
            word = splitString[i]
            splitString[i] = word [::-1]

        s = " ".join(splitString)
        return s

if False:
    def reverseString(s):
        splitString = s.split(" ")

        for i in range(len(splitString)):
            splitString[i] = splitString[i][::-1]

        return " ".join(splitString)
    
if True:
    def reverseString(s):
        f = lambda word: word[::-1]
        return ' '.join(map(f,s.split()))

print(f"{reverseString(caseString_1)}")
print(f"{reverseString(caseString_2)}")