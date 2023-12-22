#Single Number
#https://leetcode.com/problems/single-number/description/

caseNums_1 = [2,2,1]
caseNums_2 = [4,1,2,1,2]
caseNums_3 = [1]

if True:
    def singleNumber(nums):
        myDict = dict()

        for n in nums:
            if n in myDict:
                myDict[n] = 1
            else:
                myDict[n] = 0
        
        for key, val in myDict.items():
            if val == 0:
                return key
            
    print(f"{singleNumber(caseNums_1)}")
    print(f"{singleNumber(caseNums_2)}")
    print(f"{singleNumber(caseNums_3)}")