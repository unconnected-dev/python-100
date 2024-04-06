#Running Sum Of 1d Array
#https://leetcode.com/problems/running-sum-of-1d-array/description/

caseNums_1 = [1,2,3,4]
caseNums_2 = [1,1,1,1,1]
caseNums_3 = [3,1,2,10,1]

if False:
    def runningSumOf1dArray(nums):
        runner = 0
        runningList = []
        
        for num in nums:
            runningList.append(runner + num)
            runner += num

        return runningList

if False:
    def runningSumOf1dArray(nums):
        return [sum(nums[:i+1]) for i in range(len(nums))]

if True:
    def runningSumOf1dArray(nums):
        res = [0] * len(nums)
        r, i = 0, 0

        for n in nums:
            res[i] = r + n
            r += n
            i += 1
            
        return res


print(f"{runningSumOf1dArray(caseNums_1)}")
print(f"{runningSumOf1dArray(caseNums_2)}")
print(f"{runningSumOf1dArray(caseNums_3)}")