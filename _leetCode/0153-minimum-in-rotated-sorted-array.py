#Find Minimum In Rotated Sorted Array
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

caseNums_1 = [3,4,5,1,2]
caseNums_2 = [4,5,6,7,0,1,2]
caseNums_3 = [11,13,15,17]
caseNums_4 = [2,1]
caseNums_5 = [3,1,2]

if True:
    def findMin(nums):
        left, right = 0, len(nums)-1
        res = nums[0]
        
        while left <= right:
            
            if nums[left] <= nums[right]:
                res = min(res, nums[left])
                break
            
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid 
                
        return res
    
print(f"{findMin(caseNums_1)}")
print(f"{findMin(caseNums_2)}")
print(f"{findMin(caseNums_3)}")
print(f"{findMin(caseNums_4)}")
print(f"{findMin(caseNums_5)}")