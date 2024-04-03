#Single Number
#https://leetcode.com/problems/single-number/description/

caseNums_1 = [2,2,1]
caseNums_2 = [4,1,2,1,2]
caseNums_3 = [1]
caseNums_4 = [-1]
caseNums_5 = [-1,-1,-2]
caseNums_6 = [1,3,1,-1,3]

if False:
    def singleNumber(nums) -> int:
        myDict = dict()

        for n in nums:
            if n in myDict:
                myDict[n] = 1
            else:
                myDict[n] = 0
        
        for key, val in myDict.items():
            if val == 0:
                return key

if False:
    def singleNumber(nums) -> int:
        res = 0
        for n in nums:
            res ^= n
        
        return res

if True:
    def singleNumber(nums) -> int:
        my_dict = dict()

        for n in nums:
            my_dict[n] = my_dict.get(n, 0) + 1
        
        for key, val in my_dict.items():
            if val == 1:
                return key
        
        return 0

print(f"{singleNumber(caseNums_1)}")
print(f"{singleNumber(caseNums_2)}")
print(f"{singleNumber(caseNums_3)}")
print(f"{singleNumber(caseNums_4)}")
print(f"{singleNumber(caseNums_5)}")
print(f"{singleNumber(caseNums_6)}")
    