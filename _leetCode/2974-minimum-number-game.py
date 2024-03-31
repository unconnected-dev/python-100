#Minimum Number Game
#https://leetcode.com/problems/minimum-number-game/description/

caseNums_1 = [5,4,2,3]
caseNums_2 = [2,5]

if False:
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

if False:
    def numberGame(nums):
        nums.sort()

        for i in range(0, len(nums), 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        
        return nums

if True:
    def numberGame(nums):
        nums.sort()
        res = [0] * len(nums)
        for i in range(0, len(nums), 2):
            res[i], res[i+1] = nums[i+1], nums[i]
        
        return res

print(f"{numberGame(caseNums_1)}")
print(f"{numberGame(caseNums_2)}")