#Remove Duplicates From Sorted Array
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

caseNums_1 = [1,1,2]
caseNums_2 = [0,0,1,1,1,2,2,3,3,4]

#Removes duplicates with a Set
if False:
    def removeDuplicates(nums):
        i = 0

        aSet = set(nums)
        nums.clear()

        for num in aSet:
            nums.append(num)

        return nums

#Removes duplicates by checking the next value over
if False:
    def removeDuplicates(nums):
        i = 0

        while i + 1 < len(nums):
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
                
        return nums

#Removes duplicates by going through list
#Finds the first unique instance of each number
#Puts them to the start of the list with i
if True:
    def removeDuplicates(nums):
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1

        return nums[0:i]
     
print(f"{removeDuplicates(caseNums_1)}")
print(f"{removeDuplicates(caseNums_2)}")