#DI String Match
#https://leetcode.com/problems/di-string-match/description/

caseS_1 = "IDID"
caseS_2 = "III"
caseS_3 = "DDI"

if True:
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

print(f"{diStringMatch(caseS_1)}")
print(f"{diStringMatch(caseS_2)}")
print(f"{diStringMatch(caseS_3)}")