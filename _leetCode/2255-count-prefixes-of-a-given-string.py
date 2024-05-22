#Count Prefixes Of A Given String
#https://leetcode.com/problems/count-prefixes-of-a-given-string/description/

caseWords_1 = ["a","b","c","ab","bc","abc"]
caseS_1 = "abc"

caseWords_2 = ["a","a"]
caseS_2 = "aa"

if True:
    def countPrefixes(words, s):
        total = 0
        for word in words:
            if word == s[0:len(word)]:
                total += 1

        return total
    
print(f"{countPrefixes(caseWords_1, caseS_1)}")
print(f"{countPrefixes(caseWords_2, caseS_2)}")