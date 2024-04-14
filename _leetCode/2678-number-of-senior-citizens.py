#Number Of Senior Citizens
#https://leetcode.com/problems/number-of-senior-citizens/description/

caseDetails_1 = ["7868190130M7522","5303914400F9211","9273338290F4010"]
caseDetails_2 = ["1313579440F2036","2921522980M5644"]

if False:
    def countSeniors(details) -> int:
        total = 0

        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                total += 1
        
        return total

if True:
    def countSeniors(details) -> int:
        total = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                total += 1

        return total

print(f"{countSeniors(caseDetails_1)}")
print(f"{countSeniors(caseDetails_2)}")