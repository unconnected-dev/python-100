#Largest Rectangle In Histogram
#https://leetcode.com/problems/largest-rectangle-in-histogram/description/

caseHeights_1 = [2,1,5,6,2,3]
caseHeights_2 = [2,4]
caseHeights_3 = [0]
caseHeights_4 = [2,0,2]

if True:
    def largestRectangleArea(heights):
        
        max_area = 0
        stack = []
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height*(i-index))
                start = index
            stack.append([start, h])
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area
        
print(f"{largestRectangleArea(caseHeights_1)}")
print(f"{largestRectangleArea(caseHeights_2)}")
print(f"{largestRectangleArea(caseHeights_3)}")
print(f"{largestRectangleArea(caseHeights_4)}")