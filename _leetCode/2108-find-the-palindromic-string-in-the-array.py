#Find The Palindromic String In The Array
#https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

caseWords_1 = ["abc","car","ada","racecar","cool"]
caseWords_2 = ["notapalindrome","racecar"]
caseWords_3 = ["def","ghi"]

if False:
    def firstPalindrome(words):
        for word in words:
            if word == word[::-1]:
                return word
        
        return ""

if True:
    def firstPalindrome(words):
        for word in words:
            left, right = 0, len(word)-1

            while left < len(word)//2 +1:
                if word[left] != word[right]:
                    break
                    
                left+=1
                right-=1

            if left == len(word)//2 + 1:
                return word    

        return ""

print(f"{firstPalindrome(caseWords_1)}")
print(f"{firstPalindrome(caseWords_2)}")
print(f"{firstPalindrome(caseWords_3)}")