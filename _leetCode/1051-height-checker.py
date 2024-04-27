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

if False:
    def heightChecker(heights):
        res = 0
        for sh, s in zip(sorted(heights),heights):
            if sh != s:
                res += 1

        return res

if True:
    def heightChecker(heights):
        max_height = max(heights)
        count = [0] * (max_height + 1)
        res = 0

        for height in heights:
            count[height] += 1
        
        j = len(heights)-1
        for expected_height in range(len(count)-1,0,-1):
            
            while count[expected_height] > 0:
                if j >= 0 and  heights[j] != expected_height:
                    res += 1

                j -= 1
                count[expected_height] -= 1

        return res

print(f"{heightChecker(caseHeights_1)}")
print(f"{heightChecker(caseHeights_2)}")
print(f"{heightChecker(caseHeights_3)}")