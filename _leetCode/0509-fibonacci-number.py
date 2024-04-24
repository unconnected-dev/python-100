#Fibonacci Number
#https://leetcode.com/problems/fibonacci-number/description/

caseN_1 = 2
caseN_2 = 3
caseN_3 = 4

if False:
    def fib(n):
        a, b = 0, 1
        
        for _ in range(n):
            a, b = b, a + b

        return a
    
if True:
    def fib(n):
        
        def outer():
            a, b = 0, 1
            def inner():
                nonlocal a,b
                a, b = b, a + b    
                return a
            return inner

        f = outer()
        for _ in range(n - 1):
            f()
            
        return f() if n > 0 else 0

print(f"{fib(caseN_1)}")
print(f"{fib(caseN_2)}")
print(f"{fib(caseN_3)}")