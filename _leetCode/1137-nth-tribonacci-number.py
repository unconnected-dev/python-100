#N-th Tribonacci Number
#https://leetcode.com/problems/n-th-tribonacci-number/description/

caseN_1 = 4
caseN_2 = 25
caseN_3 = 0

if False:
    def tribonacci(n):
        
        a, b, c = 0, 1, 1
        
        for _ in range(n):
            a, b, c = b, c, a + b + c

        return a

if True:
    def tribonacci(n):
        
        def outer():
            a, b, c = 0, 1, 1
            def inner():
                nonlocal a, b, c
                a, b, c = b, c, a + b + c
                return a
            return inner

        trib = outer()
        for _ in range(n-1):
            trib()
            
        return trib() if n > 0 else 0

print(f"{tribonacci(caseN_1)}")
print(f"{tribonacci(caseN_2)}")
print(f"{tribonacci(caseN_3)}")