#Count Of Matches In Tournament
#https://leetcode.com/problems/count-of-matches-in-tournament/description/

caseNum_1 = 7
caseNum_2 = 14

if True:
    def numberOfMatches(n):
        c = 0

        while n > 1:
            if n % 2 == 0:
                c += n / 2
                n = n / 2
            else:
                c += (n - 1) / 2
                n = (n - 1) / 2 + 1
        
        return c

print(f"{numberOfMatches(caseNum_1)}")
print(f"{numberOfMatches(caseNum_2)}")