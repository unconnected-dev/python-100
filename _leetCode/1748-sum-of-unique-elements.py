#Sum Of Unique Elements
#https://leetcode.com/problems/sum-of-unique-elements/description/

caseNums_1 = [1,2,3,2]
caseNums_2 = [1,1,1,1,1]
caseNums_3 = [1,2,3,4,5]

if False:
    def sumOfUniqueElements(nums) -> int:
        myDict = dict()
        count = 0

        for num in nums:
            if num in myDict:
                myDict[num] = 1
            else:
                myDict[num] = 0
        
        for k, val in myDict.items():
            if val == 0:
                count += k
        
        return count

if True:
    def sumOfUniqueElements(nums) -> int:
        my_dict = {}
        res = 0

        for n in nums:
            my_dict[n] = my_dict.get(n, 0) + 1
        
        for k, v in my_dict.items():
            if v == 1:
                res += k
                
        return res

print(f"{sumOfUniqueElements(caseNums_1)}")
print(f"{sumOfUniqueElements(caseNums_2)}")
print(f"{sumOfUniqueElements(caseNums_3)}")