#Remove Element
#https://leetcode.com/problems/remove-element/description/

caseNums_1 = [3,2,2,3]
caseVal_1 = 3

caseNums_2 = [0,1,2,2,3,0,4,2]
caseVal_2 = 2

#Pops elements equal to the val by the index
if False:
    def removeElement(nums, val) -> int:
        i = 0
        
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                continue
            
            i += 1

        return i

#Removes elements by the val
if False:
    def removeElement(nums, val) -> int:
        while val in nums:
            nums.remove(val)
        
        return len(nums)

#Question requires in-place not a new array
#Return the number of elements in nums not equal to val
#Tracks elements equal to val via i and replaces with n
if False:
    def removeElement(nums, val) -> int:
        i = 0
        for n in nums:
            if n != val:
                nums[i] = n
                i += 1
        
        return i

if True:
    def removeElement(nums, val) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == val:
                nums[left], nums[right], right = nums[right], nums[left], right - 1
            else:
                left += 1

        return left
        
print(f"{removeElement(caseNums_1, caseVal_1)}")
print(f"{removeElement(caseNums_2, caseVal_2)}")