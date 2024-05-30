#Maximum Count Of Positive Integer And Negative Integer
#https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/

caseNums_1 = [-2,-1,-1,1,2,3]
caseNums_2 = [-3,-2,-1,0,0,1,2]
caseNums_3 = [5,20,66,1314]

if True:
    def maximumCount(nums):
        pos, neg = 0, 0
        for n in nums:
            if n > 0:
                pos += 1
            elif n < 0:
                neg += 1

        return max(pos, neg)
    
print(f"{maximumCount(caseNums_1)}")
print(f"{maximumCount(caseNums_2)}")
print(f"{maximumCount(caseNums_3)}")