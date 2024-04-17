#Minimum String Length After Removing Substrings
#https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/

caseS_1 = "ABFCACDB"
caseS_2 = "ACBBD"

if False:
    def minLength(s):
        
        while "AB" in s or "CD" in s:
            
            s = s.split("AB")
            s = ''.join(s)
            s = s.split("CD")
            s = ''.join(s)
    
        return len(s)

if True:
    def minLength(s):
        
        while "AB" in s or "CD" in s:
            s = s.replace("AB","").replace("CD","")
        
        return len(s)
    
print(f"{minLength(caseS_1)}")
print(f"{minLength(caseS_2)}")