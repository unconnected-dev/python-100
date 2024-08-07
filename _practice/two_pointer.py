
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

if False:
    def move_zeroes_right(nums):
        right = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
        
        return nums
    
    caseNums = [0, 1, 0, 3, 12]
    print(move_zeroes_right(caseNums))

if True:
    def find_square_root(n) -> int:
        if n < 2:
            return 0
        
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == n:
                return mid
            
            elif mid * mid < n:
                left = mid + 1
            
            else:
                right = mid - 1

        return right
        
    print(f"{find_square_root(25)}")