#Container With Most Water
#https://leetcode.com/problems/container-with-most-water/description/

caseHeight_1 = [1,8,6,2,5,4,8,3,7]
caseHeight_2 = [1,1]

if True:
    def maxArea(height):
        left, right, area = 0, len(height) -1, 0

        while left < right:
            area = max(area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area

print(f"{maxArea(caseHeight_1)}")
print(f"{maxArea(caseHeight_2)}")