#Minimum Number Game
#https://leetcode.com/problems/minimum-number-game/description/

caseNums_1 = [5,4,2,3]
caseNums_2 = [2,5]

if True:
    def numberGame(nums):
        rl = []
        while len(nums) > 0:
            alice = min(nums)
            nums.remove(alice)
            bob = min(nums)
            nums.remove(bob)

            rl.append(bob)
            rl.append(alice)

        return rl

print(f"{numberGame(caseNums_1)}")
print(f"{numberGame(caseNums_2)}")