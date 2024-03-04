#Reverse Prefix Of Word
#https://leetcode.com/problems/reverse-prefix-of-word/description/

caseWord_1 = "abcdefd"
caseCh_1 = "d"

caseWord_2 = "xyxzxe"
caseCh_2 = "z"

caseWord_3 = "abcd"
caseCh_3 = "z"

if True:
    def reversePrefix(word, ch):
        if ch in word:
            i = word.index(ch) + 1
            substring = word[:i]
            return substring[::-1] + word[i:]
        else:
            return word
        
print(f"{reversePrefix(caseWord_1, caseCh_1)}")
print(f"{reversePrefix(caseWord_2, caseCh_2)}")
print(f"{reversePrefix(caseWord_3, caseCh_3)}")