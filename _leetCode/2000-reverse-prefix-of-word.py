#Reverse Prefix Of Word
#https://leetcode.com/problems/reverse-prefix-of-word/description/

caseWord_1 = "abcdefd"
caseCh_1 = "d"

caseWord_2 = "xyxzxe"
caseCh_2 = "z"

caseWord_3 = "abcd"
caseCh_3 = "z"

if False:
    def reversePrefix(word, ch):
        if ch in word:
            i = word.index(ch) + 1
            substring = word[:i]
            return substring[::-1] + word[i:]
        else:
            return word

if True:
    def reversePrefix(word, ch):
        return word[:word.index(ch) + 1][::-1] + word[word.index(ch) + 1:] if ch in word else word

if True:
    def reversePrefix(word, ch):
        if ch in word:
            i = word.index(ch) + 1
            substring = list(word[:i])
            left, right = 0, len(substring) - 1
            while left < right:
                substring[left], substring[right] = substring[right], substring[left]
                left += 1
                right -= 1
            return ''.join(substring) + word[i:]

        else:
            return word
        
print(f"{reversePrefix(caseWord_1, caseCh_1)}")
print(f"{reversePrefix(caseWord_2, caseCh_2)}")
print(f"{reversePrefix(caseWord_3, caseCh_3)}")