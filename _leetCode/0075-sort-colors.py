#Sort Colors
#https://leetcode.com/problems/sort-colors/description/

caseNums_1 = [2,0,2,1,1,0]
caseNums_2 = [2,0,1]

if True:
    def sortColors(nums):
        z, o, l = 0, 0, len(nums)
        
        for n in nums:
            if n == 0:
                z += 1
            elif n == 1:
                o += 1
                
        for i in range(0, z):
            nums[i] = 0
            
        for i in range(z, z + o):
            nums[i] = 1
            
        for i in range(z + o, l):
            nums[i] = 2 

        return nums

print(f"{sortColors(caseNums_1)}")
print(f"{sortColors(caseNums_2)}")