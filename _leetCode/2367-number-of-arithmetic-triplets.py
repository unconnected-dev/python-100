#Number Of Arithmetic Triplets
#https://leetcode.com/problems/number-of-arithmetic-triplets/description/

caseNums_1 = [0,1,4,6,7,10]
caseDiff_1 = 3

caseNums_2 = [4,5,6,7,8,9]
caseDiff_2 = 2

if False:
    def arithmeticTriplets(nums, diff):
        res = {}
        left_val =0

        for i in range(len(nums)):
            left_val = nums[i]
            target_mid = left_val + diff
            
            found_j = False
            for j in range(i+1, len(nums)):
                if nums[j] == target_mid:
                    target_right = target_mid + diff

                    for k in range(j+1, len(nums)):
                        if nums[k] == target_right:
                            res[f"{i}_{j}_{k}"] = 1
                            found_j = True
                            break
                
                if found_j == True:
                    break

        return len(res)

if True:
    def arithmeticTriplets(nums, diff):
        my_set = set(nums)
        res = 0

        for n in nums:
            if n + diff in my_set and n + diff*2 in my_set:
                res += 1

        return res

print(f"{arithmeticTriplets(caseNums_1, caseDiff_1)}")
print(f"{arithmeticTriplets(caseNums_2, caseDiff_2)}")