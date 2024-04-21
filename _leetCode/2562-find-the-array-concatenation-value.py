#Find The Array Concatenation Value
#https://leetcode.com/problems/find-the-array-concatenation-value/description/

caseNums_1 = [7,52,2,4]
caseNums_2 = [5,14,13,8,12]

if True:
    def findTheArrayConcVal(nums):
        left, right = 0, len(nums)-1
        res = 0
        while left <= right:
            conc = ""
            if left != right:
                conc = str(nums[left]) + str(nums[right])
            else:
                conc = str(nums[left])
            
            res += int(conc)

            left += 1
            right -= 1
            
        return res            
                
print(f"{findTheArrayConcVal(caseNums_1)}")
print(f"{findTheArrayConcVal(caseNums_2)}")