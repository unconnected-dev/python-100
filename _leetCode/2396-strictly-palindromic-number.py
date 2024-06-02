#Strictly Palindromic Number
#https://leetcode.com/problems/strictly-palindromic-number/description/

caseN_1 = 9
caseN_2 = 4

if False:
    def isStrictlyPalindromic(n):
        
        for i in range(2, n-1):
            arr = []
            
            j = n
            while j > 0:
                arr.append(j%i)
                j = j // i

            if arr != arr[::-1]:
                return False
                
        return True

#Due to base (n-2) it will always be 12 which is not palindromic
if True:
    def isStrictlyPalindromic(n):
        return False

print(f"{isStrictlyPalindromic(caseN_1)}")
print(f"{isStrictlyPalindromic(caseN_2)}")