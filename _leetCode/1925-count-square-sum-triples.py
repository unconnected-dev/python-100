#Count Square Sum Triples
#https://leetcode.com/problems/count-square-sum-triples/description/

caseN_1 = 5
caseN_2 = 10

if True:
    def countTriples(n):
        l = []
        for n in range(1,n+1):
            l.append(n**2)
        
        a,c = 0,0
        res = 0
        left = 0
        right = len(l) - 1
        while right >= left + 2:
            c = l[right]
            for i in range(right):
                a = l[i]
                if (c - a) in l:
                    res += 1

            right -= 1

        return res
    
print(f"{countTriples(caseN_1)}")
print(f"{countTriples(caseN_2)}")