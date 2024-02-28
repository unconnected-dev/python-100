#Average Value Of Even Numbers That Are Divisible By Three
#https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description/

caseNums_1 = [1,3,6,10,12,15]
caseNums_2 = [1,2,4,7,10]

if True:
    def averageValue(nums):
        res_nums = []

        for n in nums:
            if n % 3 == 0 and n % 2 == 0:
                res_nums.append(n)
        
        total = sum(res_nums)
        return int(total/len(res_nums)) if total > 0 else 0

print(f"{averageValue(caseNums_1)}")
print(f"{averageValue(caseNums_2)}")