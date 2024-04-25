#Reverse Only Letters
#https://leetcode.com/problems/reverse-only-letters/description/

caseS_1 = "ab-cd"
caseS_2 = "a-bC-dEf-ghIj"
caseS_3 = "Test1ng-Leet=code-Q!"
caseS_4 = "-"

if False:
    def reverseOnlyLetters(s):
        s = [*s]
        left, right = 0, len(s)-1
        
        while left <= right:
            
            while left < len(s) and not s[left].isalpha():
                left += 1
                
            while right > 0 and not s[right].isalpha():
                right -= 1

            if left <= right:
                s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
            
        return ''.join(s)

if True:
    def reverseOnlyLetters(s):
        letters = [c for c in s if c.isalpha()]
        res = [None if c.isalpha() else c for c in s]
        
        for i in range(len(res)):
            if res[i] is None:
                res[i] = letters.pop()

        return ''.join(res)
    
print(f"{reverseOnlyLetters(caseS_1)}")
print(f"{reverseOnlyLetters(caseS_2)}")
print(f"{reverseOnlyLetters(caseS_3)}")
print(f"{reverseOnlyLetters(caseS_4)}")