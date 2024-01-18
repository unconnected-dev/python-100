#Contains Duplicate
#https://leetcode.com/problems/contains-duplicate/description/

caseNums_1 = [1,2,3,1]
caseNums_2 = [1,2,3,4]
caseNums_3 = [1,1,1,3,3,4,3,2,4,2]

if False:
    def containsDuplicate(nums) -> bool:
        aSet = set(nums)
        return len(aSet) != len(nums)

if True:
    def containsDuplicate(nums) -> bool:
        aSet = set()
        for n in nums:
            if n in aSet:
                return True
            else:
                aSet.add(n)

        return False
    
print(f"{containsDuplicate(caseNums_1)}")
print(f"{containsDuplicate(caseNums_2)}")
print(f"{containsDuplicate(caseNums_3)}")