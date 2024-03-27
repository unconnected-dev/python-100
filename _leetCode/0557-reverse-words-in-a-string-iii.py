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
    
if False:
    def reverseString(s):
        f = lambda word: word[::-1]
        return ' '.join(map(f,s.split()))

if True:
    def reverseString(s):
        split_string = s.split(" ")
        res = []
        for word in split_string:
            left, right = 0, len(word) - 1
            word_l = list(word)

            while left < right:
                word_l[left], word_l[right] = word_l[right], word_l[left]
                left+=1
                right-=1
            
            res.append(''.join(word_l))

        return ' '.join(res)

print(f"{reverseString(caseString_1)}")
print(f"{reverseString(caseString_2)}")