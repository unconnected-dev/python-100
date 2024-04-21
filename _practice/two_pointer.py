
if False:
    def two_sum(nums, target):
        left, right = 0 ,len(nums)-1
        
        while left <= right:
            total = sum([nums[left], nums[right]])
            
            if total > target:
                right -= 1
            elif total < target:
                left += 1
                
            if total == target:
                return [left, right]
            
    caseNums = [2, 7, 11, 15]
    caseTarget = 22
    
    print(f"{two_sum(caseNums, caseTarget)}")
    
if False:
    def move_zeroes(nums):
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                
        return nums
    
    caseNums = [0, 1, 0, 3, 12]
    print(move_zeroes(caseNums))