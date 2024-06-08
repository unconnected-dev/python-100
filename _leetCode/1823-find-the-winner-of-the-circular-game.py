#Find The Winner Of The Circular Game
#https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

caseN_1 = 5
caseK_1 = 2

caseN_2 = 6
caseK_2 = 5

if True:
    def findTheWinner(n: int, k: int) -> int:
        nums = [i for i in range(1, n + 1)]

        s = 0
        while len(nums) > 1:
            s = (s + k-1) % len(nums)
            nums.pop(s)
        
        return nums[0]


print(f"{findTheWinner(caseN_1, caseK_1)}")
print(f"{findTheWinner(caseN_2, caseK_2)}")