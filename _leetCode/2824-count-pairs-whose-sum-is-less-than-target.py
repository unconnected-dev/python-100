#Count Pairs WHose Sum Is Less Than Target
#https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

caseNums_1 = [-1,1,2,3,1]
caseTarget_1 = 2

caseNums_2 = [-6,2,5,-2,-7,-1,3]
caseTarget_2 = -2

if False:
    def countPairs(nums, target):
        c = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    c+=1

        return c

if False:
    def countPairs(nums, target):
        nums.sort()
        c = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] < target:
                #counts all pairs satisfying condition
                #due to nums being sorted
                c += right - left
                left += 1
            else:
                right -= 1
        
        return c

if True:
    def countPairs(nums, target):
        left, right = 0, len(nums) - 1
        res = 0

        while left < len(nums) - 1:
            while right > left:
                if (nums[left] + nums[right]) < target:
                    res += 1
                right -= 1
            
            left += 1
            right = len(nums) - 1

        return res

print(f"{countPairs(caseNums_1, caseTarget_1)}")
print(f"{countPairs(caseNums_2, caseTarget_2)}")