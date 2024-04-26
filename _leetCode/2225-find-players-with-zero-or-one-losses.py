#Find Players With Zero Or One Losses
#https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/

caseMatches_1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
caseMatches_2 = [[2,3],[1,3],[5,4],[6,4]]

if False:
    def findWinners(matches):
        winner_set = set()
        losers_set = set()
        losers = {}
        
        for match in matches:
            winner = match[0]
            loser = match[1]
            
            winner_set.add(winner)
            losers_set.add(loser)
            losers[loser] = losers.get(loser, 0) + 1
        
        loser_arr = [player for player, val in losers.items() if val == 1]
        
        return[sorted(list(winner_set-losers_set)), sorted(loser_arr)]

if True:
    def findWinners(matches):
        winners = {}
        losers = {}
        
        for winner, loser in matches:
            winners[winner] = winners.get(winner, 0) + 1
            losers[loser] = losers.get(loser, 0) + 1

        res = [[],[]]
        for player, val in winners.items():
            if player not in losers:
                res[0].append(player)
        
        for player, val in losers.items():
            if val == 1:
                res[1].append(player)
        
        res[0].sort()
        res[1].sort()
        
        return res
    
print(f"{findWinners(caseMatches_1)}")
print(f"{findWinners(caseMatches_2)}")