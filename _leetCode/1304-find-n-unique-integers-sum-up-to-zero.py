#Find N Unique Integers Sum Up To Zero
#https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/

caseNum_1 = 5
caseNum_2 = 3
caseNum_3 = 1

if True:
    def sumZero(n):
        if n == 1:
            return [0]
        
        numberList = []

        i = 1
        while len(numberList) < n:
            numberList.append(i)
            numberList.append(i * -1)
            
            if len(numberList) > n:
                numberList[len(numberList) - 2] += numberList.pop()
                
            i += 1

        numberList.sort()

        return numberList

print(f"{sumZero(caseNum_1)}")            
print(f"{sumZero(caseNum_2)}")            
print(f"{sumZero(caseNum_3)}")            
