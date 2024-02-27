#Fibonacci Number
#https://leetcode.com/problems/fibonacci-number/description/

caseN_1 = 2
caseN_2 = 3
caseN_3 = 4

if True:
    def fib(n):
        a, b = 0, 1
        
        for _ in range(n):
            a, b = b, a + b

        return a
    
print(f"{fib(caseN_1)}")
print(f"{fib(caseN_2)}")
print(f"{fib(caseN_3)}")