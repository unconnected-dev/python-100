#Palindrome Number
#https://leetcode.com/problems/palindrome-number/description/

caseNum_1 = 121
caseNum_2 = -121
caseNum_3 = 10

if False:
    def isPalindrome(x):
        numString = str(x)
        numStringReversed = numString[::-1]

        return numString == numStringReversed
    
if False:
    def isPalindrome(x):
        ns = str(x)
        return ns == ns[::-1]

if True:
    def isPalindrome(x):
        n_string = str(x)
        left, right = 0, len(n_string) - 1

        while left < right:
            if n_string[left] != n_string[right]:
                return False
            left += 1
            right -= 1

        return True

print(f"{isPalindrome(caseNum_1)}")
print(f"{isPalindrome(caseNum_2)}")
print(f"{isPalindrome(caseNum_3)}")