#Check If Number Has Equal Digit Count And Digit Value
#https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description/

caseNum_1 = "1210"
caseNum_2 = "030"

if True:
    def digitCount(num):
        for i in range(len(num)):
            if (num.count(str(i)) != int(num[i])):
                return False

        return True
    
print(f"{digitCount(caseNum_1)}")
print(f"{digitCount(caseNum_2)}")