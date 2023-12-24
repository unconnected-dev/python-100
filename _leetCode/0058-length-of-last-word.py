#Length Of Last Word
#https://leetcode.com/problems/length-of-last-word/description/

caseString_1 = "Hello World"
caseString_2 = "   fly me   to   the moon  "
caseString_3 = "luffy is still joyboy"

if True:
    def lengthOfLastWord(s) -> int:
        last = s.split()

        return len(last[-1])
    
    print(f"{lengthOfLastWord(caseString_1)}")
    print(f"{lengthOfLastWord(caseString_2)}")
    print(f"{lengthOfLastWord(caseString_3)}")