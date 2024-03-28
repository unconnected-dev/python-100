#DI String Match
#https://leetcode.com/problems/di-string-match/description/

caseS_1 = "IDID"
caseS_2 = "III"
caseS_3 = "DDI"

if False:
    def diStringMatch(s):
        res = []
        left = 0
        right = len(s)

        for c in s:
            if c == "I":
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1

        res.append(left)
        return res

if False:
    def diStringMatch(s):
        res = []
        left, right = 0, len(s)

        for c in s:
            if c == "I":
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1

        res.append(left)
        return res

if True:
    def diStringMatch(s):
        res = [0] * (len(s)+1)
        left, right = 0, len(s)
        
        for i in range(len(s)):
            if s[i] == "I":
                res[i] = left
                left+=1
            else:
                res[i] = right
                right-=1
        
        res[-1] = left

        return res




print(f"{diStringMatch(caseS_1)}")
print(f"{diStringMatch(caseS_2)}")
print(f"{diStringMatch(caseS_3)}")