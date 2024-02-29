#Minimum Amount Of Time To Collect Garbage
#https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/

caseGarbage_1 = ["G","P","GP","GG"]
caseTravel_1 = [2,4,3]

caseGarbage_2 = ["MMM","PGM","GP"]
caseTravel_2 = [3,10]

if True:
    def garbageCollection(garbage, travel):
        total_time = 0
        trucks = ["M","P","G"]

        for truck in trucks:
            temp_time = 0
            remove_time = 0
            garbage_found = False

            for i in range(len(garbage)):
                if truck in garbage[i]:
                    temp_time += garbage[i].count(truck)
                    garbage_found = True
                
                if garbage_found == True:
                    remove_time = 0
                    garbage_found = False
                
                if i < len(travel):
                    temp_time += travel[i]
                    remove_time += travel[i]

            if garbage_found == False:
                temp_time -= remove_time

            total_time += temp_time
            
        return total_time

print(f"{garbageCollection(caseGarbage_1, caseTravel_1)}")
print(f"{garbageCollection(caseGarbage_2, caseTravel_2)}")