#Widest Vertical Area Between Two Points Containing No Points
#https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/description/

casePoints_1 = [[8,7],[9,9],[7,4],[9,7]]
casePoints_2 = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]

if True:
    def maxWidthOfVerticalArea(points):
        f = lambda p: p[0]
        points = sorted(points, key=f)
        
        max_width = 0
        for i in range(len(points) - 1):
            max_width = max(points[i + 1][0] - points[i][0], max_width)
        
        return max_width

print(f"{maxWidthOfVerticalArea(casePoints_1)}")
print(f"{maxWidthOfVerticalArea(casePoints_2)}")