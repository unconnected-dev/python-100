#Happy Number
#https://leetcode.com/problems/happy-number/description/

caseN_1 = 19
caseN_2 = 2
caseN_3 = 7
caseN_4 = 4

if False:
    def isHappy(n):
        my_set = set()
        my_set.add(n)

        while True:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in my_set or n == 1:
                break
            
            my_set.add(n)
        return n == 1

if True:
    def isHappy(n):
        my_set = set()

        while n != 1:
            if n in my_set:
                return False
            
            my_set.add(n)
            n = sum([int(i) ** 2 for i in str(n)])

        return True

print(f"{isHappy(caseN_1)}")
print(f"{isHappy(caseN_2)}")
print(f"{isHappy(caseN_3)}")
print(f"{isHappy(caseN_4)}")