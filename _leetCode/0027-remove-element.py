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

#Returns list comprehension
if True:
    def removeElement(nums, val) -> int:
        return len([n for n in nums if n != val])

print(f"{removeElement(caseNums_1, caseVal_1)}")
print(f"{removeElement(caseNums_2, caseVal_2)}")