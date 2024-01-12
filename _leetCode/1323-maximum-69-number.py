#Maximum 69 Number
#https://leetcode.com/problems/maximum-69-number/description/

caseNum_1 = 9669
caseNum_2 = 9996
caseNum_3 = 9999

if False:
    def maximum69Number(num) -> int:
        return int(str(num).replace('6','9', 1))

if True:
    def maximum69Number(num) -> int:
        num_list = list(str(num))
        for i in range(len(num_list)):
            if num_list[i] == '6':
                num_list[i] = '9'
                break

        return int(''.join(num_list))

print(f"{maximum69Number(caseNum_1)}")
print(f"{maximum69Number(caseNum_2)}")
print(f"{maximum69Number(caseNum_3)}")