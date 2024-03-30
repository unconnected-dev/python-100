#Move Zeroes
#https://leetcode.com/problems/move-zeroes/description/

caseNums_1 = [0,1,0,3,12]
caseNums_2 = [0]
caseNums_3 = [4,2,4,0,0,3,0,5,1,0]
caseNums_4 = [2,1]

if False:
    def moveZeroes(nums):
        if len(nums) <= 1:
            return nums
        
        left = 0 
        while nums[left] != 0:
            left += 1
            if left >= len(nums):
                return nums

        right = left
        while left < len(nums):
            if nums[left] != 0:
                left += 1
                continue

            if nums[right] == 0 and right + 1 < len(nums):
                right += 1
                continue

            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]   
            else:
                break

        return nums

if True:
    def moveZeroes(nums):
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left+=1

        return nums

print(f"{moveZeroes(caseNums_1)}")
print(f"{moveZeroes(caseNums_2)}")
print(f"{moveZeroes(caseNums_3)}")
print(f"{moveZeroes(caseNums_4)}")