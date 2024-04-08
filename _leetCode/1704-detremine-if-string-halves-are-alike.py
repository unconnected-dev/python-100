#Determine If String Halves Are Alike
#https://leetcode.com/problems/determine-if-string-halves-are-alike/description/

caseS_1 = "book"
caseS_2 = "textbook"

if False:
    def halvesAreAlike(s):
        h1 = s[:len(s)//2]
        h2 = s[len(s)//2:]
        
        vowels = "aeiouAEIOU"
        result = 0
        for i in range(len(h1)):
            if h1[i] in vowels:
                result += 1
            if h2[i] in vowels:
                result -= 1

        return result == 0

if True:
    def halvesAreAlike(s):
        h1 = s[:len(s)//2]
        h2 = s[len(s)//2:]

        vowels = set(["a","e","i","o","u","A","E","I","O","U"])
        result = 0

        for i in range(len(h1)):
            if h1[i] in vowels:
                result += 1
            if h2[i] in vowels:
                result -= 1

        return result == 0

print(f"{halvesAreAlike(caseS_1)}")
print(f"{halvesAreAlike(caseS_2)}")