#Last Stone Weight
#https://leetcode.com/problems/last-stone-weight/description/

caseStones_1 = [2,7,4,1,8,1]
caseStones_2 = [1]

if True:
    def lastStoneWeight(stones):
        while len(stones) != 1 and len(stones) != 0:
            stones.sort(reverse = True)

            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
            else:
                newStone = (stones.pop(0) - stones.pop(0))
                stones.append(newStone)

        if len(stones) == 1:
            return stones[0]
        else:
            return 0
            
    print(f"{lastStoneWeight(caseStones_1)}")
    print(f"{lastStoneWeight(caseStones_2)}")