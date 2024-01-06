#Palindrome Number
#https://leetcode.com/problems/palindrome-number/description/

caseNum_1 = 121
caseNum_2 = -121
caseNum_3 = 10

if True:
    def isPalindrome(num):
        numString = str(num)
        numStringReversed = numString[::-1]

        return numString == numStringReversed

print(f"{isPalindrome(caseNum_1)}")
print(f"{isPalindrome(caseNum_2)}")
print(f"{isPalindrome(caseNum_3)}")