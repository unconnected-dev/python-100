#Find N Unique Integers Sum Up To Zero
#https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/

caseNum_1 = 5
caseNum_2 = 3
caseNum_3 = 1
caseNum_4 = 4

if False:
    def sumZero(n):
        if n == 1:
            return [0]
        
        numberList = []

        i = 1
        while len(numberList) < n:
            #add positive and negative version of number to maintain sum 0
            numberList.append(i)
            numberList.append(i * -1)
            
            #if n is an odd number 1 element needs to be removed
            if len(numberList) > n:
                #add the last element to 2nd to last
                #forcing 0 as last unique number
                #[1, -1, 2, -2, 3, -3] becomes [1, -1, 2, -2, 0]
                numberList[len(numberList) - 2] += numberList.pop()
                
            i += 1

        numberList.sort()

        return numberList
    
if True:
    def sumZero(n):
        if n == 1:
            return [0]
        
        res = [0] * n
        for i in range(1, n):
            res[i] = i
        
        res[0] = -sum(res[1:])

        return res

print(f"{sumZero(caseNum_1)}")            
print(f"{sumZero(caseNum_2)}")            
print(f"{sumZero(caseNum_3)}")            
print(f"{sumZero(caseNum_4)}")            
