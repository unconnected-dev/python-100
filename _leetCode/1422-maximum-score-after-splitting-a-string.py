#Maximum Score After Splitting A String
#https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/

caseS_1 = "011101"
caseS_2 = "00111"
caseS_3 = "1111"

if False:
    def maxScore(s):
        max_, left = 0, 0
        right = s.count("1")
        
        for i in range(len(s)-1):
            
            if s[i] == "0":
                left += 1
            else:
                right -= 1
                
            max_ = max(max_, left + right)
        
        return max_

if True:
    def maxScore(s):
        max_ = 0
        for i in range(0, len(s) - 1):
            t = 0
            t += s[:i+1].count("0")
            t += s[i:].count("1")

            max_ = max(max_, t)

        return max_
        
print(f"{maxScore(caseS_1)}")
print(f"{maxScore(caseS_2)}")
print(f"{maxScore(caseS_3)}")