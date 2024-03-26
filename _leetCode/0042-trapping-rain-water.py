#Trapping Rain Water
#https://leetcode.com/problems/trapping-rain-water/description/

caseHeight_1 = [0,1,0,2,1,0,1,3,2,1,2,1]
caseHeight_2 = [4,2,0,3,2,5]

if True:
    def trap(height):
        max_left, max_right, min_lr = [], [], []
        l = len(height)
        total = 0
        
        if l <= 2:
            return 0
        
        max_left.append(0)
        for i in range(0, l-1):
            max_left.append(max(max_left[-1], height[i]))

        max_right.append(0)
        for i in range(l-1,0,-1):
            max_right.append(max(max_right[-1], height[i]))
        max_right = max_right[::-1]

        for i in range(l):
            min_lr.append(min(max_left[i], max_right[i]))

        for i in range(l):
            res = min_lr[i] - height[i]
            if res > 0:
                total += res

        return total

print(f"{trap(caseHeight_1)}")
print(f"{trap(caseHeight_2)}")