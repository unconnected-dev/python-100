#Long Pressed Name
#https://leetcode.com/problems/long-pressed-name/description/

caseName_1 = "alex"
caseTyped_1 = "aaleex"

caseName_2 = "saeed"
caseTyped_2 = "ssaaedd"

if False:
    def isLongPressedName(name, typed):
        i, j = 0, 0
        
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            
            elif j > 0 and typed[j-1] == typed[j]:
                j += 1
            else:
                return False
            
        return i == len(name)
    
if True:
    def isLongPressedName(name, typed):
        i = 0
        
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
                
        return i == len(name)
            
print(f"{isLongPressedName(caseName_1, caseTyped_1)}")
print(f"{isLongPressedName(caseName_2, caseTyped_2)}")