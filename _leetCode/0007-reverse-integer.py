#Reverse Integer
#https://leetcode.com/problems/reverse-integer/description/

caseX_1 = 123
caseX_2 = -123
caseX_3 = 120

if False:
    def reverse(x) -> int:
        if x >= 0:
            new_x = int(str(x)[::-1])
        else:
            t = str(x)[1::][::-1] 
            new_x = int(t) * -1

        return 0 if new_x > 2147483647 or new_x < -2147483647 else new_x

if False:
    def reverse(x) -> int:
        new_x = int(str(x)[::-1]) if x >= 0 else int(str(x)[1::][::-1]) * -1
        return 0 if new_x > 2147483647 or new_x < -2147483647 else new_x

if True:
    def reverse(x) -> int:
        res = int(str(abs(x))[::-1])
        return (-res if x < 0 else res) if res.bit_length() < 32 else 0

print(f"{reverse(caseX_1)}")
print(f"{reverse(caseX_2)}")
print(f"{reverse(caseX_3)}")