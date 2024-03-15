#Largest Number At Least Twice Of Others
#https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

caseNums_1 = [3,6,1,0]
caseNums_2 = [1,2,3,4]

if True:
    def dominantIndex(nums):
        
        if len(nums) < 2:
            return -1

        high, high_index = float('-inf'), 0
        next_high = float('-inf')

        for key, value in enumerate(nums):
            if value > high:
                next_high = high
            
                high = value
                high_index = key
            elif value > next_high:
                next_high = value

        if high >= next_high*2:
            return high_index
        else:
            return -1

print(f"{dominantIndex(caseNums_1)}")
print(f"{dominantIndex(caseNums_2)}")