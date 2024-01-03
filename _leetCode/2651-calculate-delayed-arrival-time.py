#Calculate Delayed Arrival Time
#https://leetcode.com/problems/calculate-delayed-arrival-time/description/

caseArrivalTime_1 = 15
caseDelayedTime_1 = 5

caseArrivalTime_2 = 13
caseDelayedTime_2 = 11

if False:
    def findDelayedArrivalTime(arrivalTime, delayedTime) -> int:
        total = arrivalTime + delayedTime

        while total >= 24:
            total -= 24

        return total

if True:
    def findDelayedArrivalTime(arrivalTime, delayedTime) -> int:
        total = arrivalTime + delayedTime

        if total < 24:
            return total
        else:
            return total - 24

print(f"{findDelayedArrivalTime(caseArrivalTime_1, caseDelayedTime_1)}")
print(f"{findDelayedArrivalTime(caseArrivalTime_2, caseDelayedTime_2)}")