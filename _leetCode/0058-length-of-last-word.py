#Length Of Last Word
#https://leetcode.com/problems/length-of-last-word/description/

caseString_1 = "Hello World"
caseString_2 = "   fly me   to   the moon  "
caseString_3 = "luffy is still joyboy"
caseString_4 = "a"

if False:
    def lengthOfLastWord(s) -> int:
        last = s.split()

        return len(last[-1])

if True:
    def lengthOfLastWord(s) -> int:
        result = 0
        l = len(s)

        for i in range(l-1, -1, -1):
            if s[i] != " ":
                result += 1
            elif result > 0:
                return result

        return result
    
print(f"{lengthOfLastWord(caseString_1)}")
print(f"{lengthOfLastWord(caseString_2)}")
print(f"{lengthOfLastWord(caseString_3)}")
print(f"{lengthOfLastWord(caseString_4)}")