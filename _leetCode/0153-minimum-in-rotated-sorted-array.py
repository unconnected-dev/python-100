#Find Minimum In Rotated Sorted Array
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

caseNums_1 = [3,4,5,1,2]
caseNums_2 = [4,5,6,7,0,1,2]
caseNums_3 = [11,13,15,17]

if True:
    def findMin(nums):
        left, right = 0, len(nums)-1
        res = float('inf')
        
        while left <= right:
            
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
                
        return res
    
print(f"{findMin(caseNums_1)}")
print(f"{findMin(caseNums_2)}")
print(f"{findMin(caseNums_3)}")