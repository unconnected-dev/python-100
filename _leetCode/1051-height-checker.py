#Height Checker
#https://leetcode.com/problems/height-checker/description/

caseHeights_1 = [1,1,4,2,1,3]
caseHeights_2 = [5,1,2,3,4]
caseHeights_3 = [1,2,3,4,5]

if False:
    def heightChecker(heights):
        new_heights = sorted(heights)
        res = 0

        for i in range(len(heights)):
            if heights[i] != new_heights[i]:
                res += 1

        return res

if True:
    def heightChecker(heights):
        res = 0
        for sh, s in zip(sorted(heights),heights):
            if sh != s:
                res += 1

        return res

print(f"{heightChecker(caseHeights_1)}")
print(f"{heightChecker(caseHeights_2)}")
print(f"{heightChecker(caseHeights_3)}")