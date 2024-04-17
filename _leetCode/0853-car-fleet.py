#Car Fleet
#https://leetcode.com/problems/car-fleet/description/

caseTarget_1 = 12
casePosition_1 = [10,8,0,5,3]
caseSpeed_1 = [2,4,1,1,3]

caseTarget_2 = 10
casePosition_2 = [3]
caseSpeed_2 = [3]

caseTarget_3 = 100
casePosition_3 = [0,2,4]
caseSpeed_3 = [4,2,1]

if True:
    def carFleet(target, position, speed):
        position_speed = [[p,s] for p, s in zip(position, speed)]
        position_speed.sort(reverse=True)
        stack = []
        
        for p, s in position_speed:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
        
    
print(f"{carFleet(caseTarget_1, casePosition_1, caseSpeed_1)}")
print(f"{carFleet(caseTarget_2, casePosition_2, caseSpeed_2)}")
print(f"{carFleet(caseTarget_3, casePosition_3, caseSpeed_3)}")