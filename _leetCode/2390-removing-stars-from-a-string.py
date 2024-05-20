#Removing Stars From A String
#https://leetcode.com/problems/removing-stars-from-a-string/description/

caseS_1 = "leet**cod*e"
caseS_2 = "erase*****"

if True:
    def removeStars(s: str) -> str:
        my_stack = []

        for c in s:
            if c == "*":
                my_stack.pop()
            else:
                my_stack.append(c)
        
        return ''.join(my_stack)
    
print(f"{removeStars(caseS_1)}")
print(f"{removeStars(caseS_2)}")