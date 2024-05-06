#Add To Array Form Of Integer
#https://leetcode.com/problems/add-to-array-form-of-integer/description/

caseNum_1 = [1,2,0,0]
caseK_1 = 34

caseNum_2 = [2,7,4]
caseK_2 = 181

caseNum_3 = [2,1,5]
caseK_3 = 806

if True:
    def addToArrayForm(num, k):
        s = ''.join(map(str,num))
        a = int(s)+k
        
        return [int(i) for i in str(a)]
    
print(f"{addToArrayForm(caseNum_1, caseK_1)}")
print(f"{addToArrayForm(caseNum_2, caseK_2)}")
print(f"{addToArrayForm(caseNum_3, caseK_3)}")
    