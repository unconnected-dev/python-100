#Self Dividing Numbers
#https://leetcode.com/problems/self-dividing-numbers/description/

caseLeft_1 = 1
caseRight_1 = 22

caseLeft_2 = 47
caseRight_2 = 85

if True:
    def selfDividingNumbers(left, right):
        res = []
        for n in range(left, right + 1):

            is_self_dividing = True
            for num in list(str(n)):
                if int(num) == 0 or n % int(num) != 0:
                    is_self_dividing = False
                    break

            if is_self_dividing == True:
                res.append(n)
        
        return res

print(f"{selfDividingNumbers(caseLeft_1, caseRight_1)}")
print(f"{selfDividingNumbers(caseLeft_2, caseRight_2)}")