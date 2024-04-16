#Daily Temperatures
#https://leetcode.com/problems/daily-temperatures/description/

caseTemperatures_1 = [73,74,75,71,69,72,76,73]
caseTemperatures_2 = [30,40,50,60]
caseTemperatures_3 = [30,60,90]

#Time limit exceeded
if True:
    def dailyTemperatures(temperatures):
        res = []
        for i in range(0, len(temperatures)):
            c = 0
            found = False
            for j in range(i+1, len(temperatures)):
                c += 1
                if temperatures[i] < temperatures[j]:
                    res.append(c)
                    found = True
                    break
            
            if found == False:
                res.append(0)
        
        return res
    
print(f"{dailyTemperatures(caseTemperatures_1)}")
print(f"{dailyTemperatures(caseTemperatures_2)}")
print(f"{dailyTemperatures(caseTemperatures_3)}")