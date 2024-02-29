#Count Number Of Pairs With Absolute Difference K
#https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/

caseNums_1 = [1,2,2,1]
caseK_1 = 1

caseNums_2 = [1,3]
caseK_2 = 3

caseNums_3 = [3,2,1,5,4]
caseK_3 = 2

if True:
    def countKDifference(nums, k):
        result = 0

        for i in range(len(nums)):
            search_plus = nums[i] + k
            search_minus = nums[i] - k

            for j in range(i,len(nums)):
                if nums[j] == search_plus or nums[j] == search_minus:
                    result += 1

        return result

print(f"{countKDifference(caseNums_1, caseK_1)}")
print(f"{countKDifference(caseNums_2, caseK_2)}")
print(f"{countKDifference(caseNums_3, caseK_3)}")