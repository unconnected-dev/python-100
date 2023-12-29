#Reverse String III
#https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

caseString_1 = "Let's take LeetCode contest"
caseString_2 = "Mr Ding"

if True:
    def reverseString(s):
        splitString = s.split(" ")

        for i in range(len(splitString)):
            word = splitString[i]
            splitString[i] = word [::-1]

        s = " ".join(splitString)
        return s

print(f"{reverseString(caseString_1)}")
print(f"{reverseString(caseString_2)}")