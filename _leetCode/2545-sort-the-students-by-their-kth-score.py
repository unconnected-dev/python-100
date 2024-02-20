#Sort The Students By Their Kth Score
#https://leetcode.com/problems/sort-the-students-by-their-kth-score/description/

caseScores_1 = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
caseK_1 = 2

caseScores_2 = [[3,4],[5,6]]
caseK_2 = 0

if True:
    def sortTheStudents(score, k):
        f = lambda s: s[k]
        return sorted(score, key=f, reverse=True)

print(f"{sortTheStudents(caseScores_1, caseK_1)}")
print(f"{sortTheStudents(caseScores_2, caseK_2)}")