#Contains Duplicate II
#https://leetcode.com/problems/contains-duplicate-ii/description/

caseNums_1 = [1,2,3,1]
caseK_1 = 3

caseNums_2 = [1,0,1,1]
caseK_2 = 1

caseNums_3 = [1,2,3,1,2,3]
caseK_3 = 2

if True:
    def containsNearbyDuplicate(nums, k):
        my_dict = {}

        for i, n in enumerate(nums):
            if n in my_dict and abs(i - my_dict[n]) <= k:
                return True
            else:
                my_dict[n] = i

        return False


print(f"{containsNearbyDuplicate(caseNums_1, caseK_1)}")
print(f"{containsNearbyDuplicate(caseNums_2, caseK_2)}")
print(f"{containsNearbyDuplicate(caseNums_3, caseK_3)}")