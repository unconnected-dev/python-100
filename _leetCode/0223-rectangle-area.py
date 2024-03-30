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

if True:
    def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        area_1 = (ax1 - ax2) * (ay1 - ay2)
        area_2 = (bx1 - bx2) * (by1 - by2)

        area_3 = ()

print(f"{computeArea(caseAx1_1, caseAy1_1, caseAx2_1, caseAy2_1, caseBx1_1, caseBy1_1, caseBx2_1, caseBy2_1)}")
print(f"{computeArea(caseAx1_2, caseAy1_2, caseAx2_2, caseAy2_2, caseBx1_2, caseBy1_2, caseBx2_2, caseBy2_2)}")