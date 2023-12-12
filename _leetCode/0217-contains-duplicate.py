#Contains Duplicate
#https://leetcode.com/problems/contains-duplicate/description/

caseNums_1 = [1,2,3,1]
caseNums_2 = [1,2,3,4]
caseNums_3 = [1,1,1,3,3,4,3,2,4,2]

if True:
    def containsDuplicate(nums):
        aSet = set(nums)

        if len(aSet) < len(nums):
            print(f"Contains a duplicate")
        else:
            print(f"Doesn't contain a duplicate")
        
    containsDuplicate(caseNums_1)
    containsDuplicate(caseNums_2)
    containsDuplicate(caseNums_3)