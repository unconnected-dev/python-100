#Minimize String Length
#https://leetcode.com/problems/minimize-string-length/description/

caseString_1 = "aaabc"
caseString_2 = "cbbd"
caseString_3 = "dddaaa"

if False:
    def minimizeStringLength(s):
        stringSet = set(list(s))
        return len(stringSet)

if True:
    def minimizeStringLength(s):
        return len(set(s))

print(f"{minimizeStringLength(caseString_1)}")
print(f"{minimizeStringLength(caseString_2)}")
print(f"{minimizeStringLength(caseString_3)}")