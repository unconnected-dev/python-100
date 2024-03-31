#Remove Trailing Zeros From A String
#https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/

caseNum_1 = "51230100"
caseNum_2 = "123"

if False:
    def removeTrailingZeros(num):
        pos = None

        for i in range(len(num) - 1, 0, -1):
            if num[i] == "0":
                pos = i
            else:
                break
        
        if pos == None:
            return num
        else:
            return num[:pos]
        
if False:
    def removeTrailingZeros(num):
        return num.rstrip("0")

if True:
    def removeTrailingZeros(num):
        for i in range(len(num)-1,-1,-1):
            if num[i] != '0':
                return num[0:i+1]

print(f"{removeTrailingZeros(caseNum_1)}")
print(f"{removeTrailingZeros(caseNum_2)}")