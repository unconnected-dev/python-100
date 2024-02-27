#Add Digits
#https://leetcode.com/problems/add-digits/description/

caseNum_1 = 38
caseNum_2 = 0

if False:
    def addDigits(num):
        while num > 9:
            new_num = 0
            for d in str(num):
                new_num += int(d)
            
            num = new_num
        
        return num

if True:
    def addDigits(num):
        while num > 9:
            new_num = 0
            while num:
                new_num += num%10
                num = num//10
            num = new_num
        
        return num

print(f"{addDigits(caseNum_1)}")
print(f"{addDigits(caseNum_2)}")