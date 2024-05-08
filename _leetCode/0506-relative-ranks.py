#Relative Ranks
#https://leetcode.com/problems/relative-ranks/description/

caseScore_1 = [5,4,3,2,1]
caseScore_2 = [10,3,8,9,4]

if True:
    def findRelativeRanks(score):
        ranks = sorted(score, reverse=True)
        res = [0] * len(score)
        for i in range(len(score)):
            res[i] = str(ranks.index(score[i]) + 1)
            
            if res[i] == "1":
                res[i] = "Gold Medal"
            elif res[i] == "2":
                res[i] = "Silver Medal"
            elif res[i] == "3":
                res[i] = "Bronze Medal"
                
        return res
    
print(f"{findRelativeRanks(caseScore_1)}")
print(f"{findRelativeRanks(caseScore_2)}")