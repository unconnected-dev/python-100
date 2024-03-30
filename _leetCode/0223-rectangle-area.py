#Rectangle Area
#https://leetcode.com/problems/rectangle-area/description/

caseAx1_1 = -3
caseAy1_1 = 0
caseAx2_1 = 3
caseAy2_1 = 4
caseBx1_1 = 0
caseBy1_1 = -1
caseBx2_1 = 9
caseBy2_1 = 2


caseAx1_2 = -2
caseAy1_2 = -2
caseAx2_2 = 2
caseAy2_2 = 2
caseBx1_2 = -2
caseBy1_2 = -2
caseBx2_2 = 2
caseBy2_2 = 2


caseAx1_3 = 0
caseAy1_3 = 0
caseAx2_3 = 0
caseAy2_3 = 0
caseBx1_3 = -1
caseBy1_3 = -1
caseBx2_3 = 1
caseBy2_3 = 1


caseAx1_4 = -2
caseAy1_4 = -2
caseAx2_4 = 2
caseAy2_4 = 2
caseBx1_4 = 3
caseBy1_4 = 3
caseBx2_4 = 4
caseBy2_4 = 4

if True:
    def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        area_1 = (ax2 - ax1) * (ay2 - ay1)
        area_2 = (bx2 - bx1) * (by2 - by1)
        
        overlap_width = min(ax2, bx2) - max(ax1, bx1)
        overlap_height = min(ay2, by2) - max(ay1, by1)
        overlap_area = max(overlap_width, 0) * max(overlap_height, 0)
        
        total_area = area_1 + area_2 - overlap_area
        
        return total_area

print(f"{computeArea(caseAx1_1, caseAy1_1, caseAx2_1, caseAy2_1, caseBx1_1, caseBy1_1, caseBx2_1, caseBy2_1)}")#45
print(f"{computeArea(caseAx1_2, caseAy1_2, caseAx2_2, caseAy2_2, caseBx1_2, caseBy1_2, caseBx2_2, caseBy2_2)}")#16
print(f"{computeArea(caseAx1_3, caseAy1_3, caseAx2_3, caseAy2_3, caseBx1_3, caseBy1_3, caseBx2_3, caseBy2_3)}")#4
print(f"{computeArea(caseAx1_4, caseAy1_4, caseAx2_4, caseAy2_4, caseBx1_4, caseBy1_4, caseBx2_4, caseBy2_4)}")#4