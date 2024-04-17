#Make The String Great
#https://leetcode.com/problems/make-the-string-great/description/

caseS_1 = "leEeetcode"
caseS_2 = "abBAcC"
caseS_3 = "s"
caseS_4 = "Pp"

if True:
    def makeGood(s):
        sl = []
        
        for c in s:
            sl.append(c)
            if len(sl) >= 2:
                if sl[-2] != sl[-1] and (sl[-2].capitalize() == sl[-1] or sl[-2].lower() == sl[-1]):
                    sl.pop() 
                    sl.pop()
        
        return ''.join(sl) 
    
print(f"{makeGood(caseS_1)}")
print(f"{makeGood(caseS_2)}")
print(f"{makeGood(caseS_3)}")
print(f"{makeGood(caseS_4)}")