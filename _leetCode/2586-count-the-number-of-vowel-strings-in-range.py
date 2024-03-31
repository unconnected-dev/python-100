#Count The Number Of Vowel Strings In Range
#https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/description/

caseWords_1 = ["are","amy","u"]
caseLeft_1 = 0
caseRight_1 = 2

caseWords_2 = ["hey","aeo","mu","ooo","artro"]
caseLeft_2 = 1
caseRight_2 = 4

if False:
    def vowelStrings(words, left, right):
        sub_words = words[left:right+1]
        vowels = ["a","e","i","o","u"]
        res = 0
        for word in sub_words:
            if word[0] in vowels and word[-1] in vowels:
                res += 1

        return res

if True:
    def vowelStrings(words, left, right):
        my_set = set(["a","e","i","o","u"])
        res = 0

        for word in words[left:right+1]:
            if word[0] in my_set and word[-1] in my_set:
                res += 1

        return res

print(f"{vowelStrings(caseWords_1, caseLeft_1, caseRight_1)}")
print(f"{vowelStrings(caseWords_2, caseLeft_2, caseRight_2)}")