#Maximum Number Of Coins You Can Get
#https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

casePiles_1 = [2,4,1,2,7,8]
casePiles_2 = [2,4,5]
casePiles_3 = [9,8,7,6,5,1,2,3,4]

if False:
    def maxCoins(piles):
        piles.sort()
        result = 0
        for i in range(len(piles) - 2, len(piles)//3 - 1, -2):
            result += piles[i]
        
        return result

if False:
    def maxCoins(piles):
        piles.sort()
        return sum(piles[-2:(len(piles)//3)-1:-2])

if True:
    def maxCoins(piles):
        return sum(sorted(piles)[len(piles)//3::2])

print(f"{maxCoins(casePiles_1)}")
print(f"{maxCoins(casePiles_2)}")
print(f"{maxCoins(casePiles_3)}")