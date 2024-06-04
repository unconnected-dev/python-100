#First Bad Version
#https://leetcode.com/problems/first-bad-version/description/

caseN_1 = 5
caseBad_1 = 4

caseN_2 = 1
caseBad_2 = 1

caseN_3 = 2126753390
caseBad_3 = 1702766719


#Can't run due to call on isBadVersion being on leet code
if False:
    def firstBadVersion(n, bad):
        left, right = 1, n + 1

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

# print(f"{firstBadVersion(caseN_1, caseBad_1)}")
# print(f"{firstBadVersion(caseN_2, caseBad_2)}")
# print(f"{firstBadVersion(caseN_3, caseBad_3)}")