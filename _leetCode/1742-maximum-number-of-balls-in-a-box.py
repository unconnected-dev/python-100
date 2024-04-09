#Maximum Number Of Balls In A Box
#https://leetcode.com/problems/maximum-number-of-balls-in-a-box/description/

caseLowLimit_1 = 1
caseHighLimit_1 = 10

caseLowLimit_2 = 5
caseHighLimit_2 = 15

caseLowLimit_3 = 19
caseHighLimit_3 = 28

if False:
    def countBalls(lowLimit, highLimit):
        my_dict = {}

        for n in range(lowLimit, highLimit + 1):
            pos = sum([int(n) for n in str(n)])
            my_dict[pos] = my_dict.get(pos, 0 ) + 1
        
        high = 0
        for key, val in my_dict.items():
            if val > high:
                high = val
        
        return high

if False:
    def countBalls(lowLimit, highLimit):
        my_dict = {}

        for n in range(lowLimit, highLimit + 1):
            pos = 0
            for d in str(n):
                pos += int(d)

            my_dict[pos] = my_dict.get(pos, 0 ) + 1
        
        high = 0
        for val in my_dict.values():
            if val > high:
                high = val
        
        return high
    
if True:
    def countBalls(lowLimit, highLimit):

        def getSumOf(n):
            res = 0
            while n:
                res += n%10
                n //= 10
            return res
        
        my_dict = {}
        for i in range(lowLimit, highLimit+1):
            num = getSumOf(i)
            my_dict[num] = my_dict.get(num, 0) + 1

        return max(my_dict.values())

print(f"{countBalls(caseLowLimit_1, caseHighLimit_1)}")
print(f"{countBalls(caseLowLimit_2, caseHighLimit_2)}")
print(f"{countBalls(caseLowLimit_3, caseHighLimit_3)}")