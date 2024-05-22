#Remove All Occurrences Of A Substring
#https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/

caseS_1 = "daabcbaabcbc"
casePart_1 = "abc"

caseS_2 = "axxxxyyyyb"
casePart_2 = "xy"

caseS_3 = "aabababa"
casePart_3 = "aba"

if True:
    def removeOccurrences(s, part):
        while part in s:
            s = s.replace(part, '', 1)
            
        return s
    
print(f"{removeOccurrences(caseS_1, casePart_1)}")
print(f"{removeOccurrences(caseS_2, casePart_2)}")
print(f"{removeOccurrences(caseS_3, casePart_3)}")