#Rearrange Array Elements By Sign
#https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

caseNums_1 = [3,1,-2,-5,2,-4]
caseNums_2 = [-1,1]

#Time limit exceeded
if False:
    def rearrangeArray(nums):
        left = 0 
        res = []
        pos = 1

        while len(nums) > 0:
            if (pos == 1 and nums[left] > 0) or (pos == -1 and nums[left] < 0):
                res.append(nums.pop(left))
                left = -1
                pos *= -1

            left += 1

        return res

if False:
    def rearrangeArray(nums):
        pos, neg, res = [], [], []

        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)

        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        
        return res

if True:
    def rearrangeArray(nums):
        posInd, negInd = 0, 1
        res = [0] * len(nums)

        for n in nums:
            if n > 0:
                res[posInd] = n
                posInd += 2
            else:
                res[negInd] = n
                negInd += 2

        return res

print(f"{rearrangeArray(caseNums_1)}")
print(f"{rearrangeArray(caseNums_2)}")