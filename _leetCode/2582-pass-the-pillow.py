#Pass The Pillow
#https://leetcode.com/problems/pass-the-pillow/description/

caseN_1 = 4
caseTime_1 = 5

caseN_2 = 3
caseTime_2 = 2

if True:
    def passThePillow(n, time) -> int:
        point = 1
        pos = -1
        
        while time > 0:
            
            if point == 1 or point == n:
                pos *= -1
            
            point += (1 * pos)
            
            time -= 1
            
        return point
    
    
print(f"{passThePillow(caseN_1, caseTime_1)}")
print(f"{passThePillow(caseN_2, caseTime_2)}")