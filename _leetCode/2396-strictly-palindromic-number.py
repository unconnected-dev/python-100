#Strictly Palindromic Number
#https://leetcode.com/problems/strictly-palindromic-number/description/

caseN_1 = 9
caseN_2 = 4

if True:
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

print(f"{isStrictlyPalindromic(caseN_1)}")
print(f"{isStrictlyPalindromic(caseN_2)}")