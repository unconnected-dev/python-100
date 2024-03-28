#Shortest Distance To A Character
#https://leetcode.com/problems/shortest-distance-to-a-character/description/

caseS_1 = "loveleetcode"
caseC_1 = "e"

caseS_2 = "aaab"
caseC_2 = "b"

if True:
    def shortestToChar(s, c):
        i = 0
        res = [float('inf')] * len(s)

        for i in range(len(s)):    
            if s[i] == c:
                left = i
                distance = 0
                while left >= 0 and res[left] > distance:
                    res[left] = distance 
                    distance += 1
                    left -= 1
                
                right = i + 1
                distance = 1
                while right < len(s) and res[right] > distance and s[right] != c:
                    res[right] = distance
                    distance += 1
                    right += 1

        return res

print(f"{shortestToChar(caseS_1, caseC_1)}")
print(f"{shortestToChar(caseS_2, caseC_2)}")