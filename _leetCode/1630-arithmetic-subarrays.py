#Arithmetic Subarrays
#https://leetcode.com/problems/arithmetic-subarrays/description/

caseNums_1 = [4,6,5,9,3,7]
caseL_1 = [0,0,2]
caseR_1 = [2,3,5]

caseNums_2 = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
caseL_2 = [0,1,6,4,8,7]
caseR_2 = [4,4,9,7,9,10]

if True:
    def checkArithmeticSubarrays(nums, l, r):
        result = []

        for i in range(len(l)):
            sliced_nums = nums[l[i]:r[i] + 1]
            sliced_nums.sort()

            diff = sliced_nums[0] - sliced_nums[1]
            diff_fine = True
            for j in range(len(sliced_nums) - 1):
                if (sliced_nums[j] - sliced_nums[j + 1]) != diff:
                    diff_fine = False
                    break
            
            if diff_fine == True:
                result.append(True)
            else:
                result.append(False)

        return result

print(f"{checkArithmeticSubarrays(caseNums_1, caseL_1, caseR_1)}")
print(f"{checkArithmeticSubarrays(caseNums_2, caseL_2, caseR_2)}")