#Largest Odd Number In String
#https://leetcode.com/problems/largest-odd-number-in-string/description/

caseNum_1 = "52"
caseNum_2 = "4206"
caseNum_3 = "35427"

if True:
    def largestOddNumber(num):
        for i in range(len(num) - 1, -1, -1):
            num_i = int(num[i])

            if num_i % 2 != 0:
                return num[:i + 1]  #+1 due to exclusive indexing
                                    #if index was 3, 2 would be included
        
        return ""

print(f"{largestOddNumber(caseNum_1)}")
print(f"{largestOddNumber(caseNum_2)}")
print(f"{largestOddNumber(caseNum_3)}")