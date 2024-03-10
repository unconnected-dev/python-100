#Minimum Bit Flips To Convert Number
#https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/

caseStart_1 = 10
caseGoal_1 = 7

caseStart_2 = 3
caseGoal_2 = 4

caseStart_3 = 10
caseGoal_3 = 82

if False:
    def minBitFlips(start, goal):
        start_list = list(bin(start)[2:])
        goal_list = list(bin(goal)[2:])
        

        start_len = len(start_list)
        goal_len = len(goal_list)

        if start_len > goal_len:
            for _ in range(start_len - goal_len):
                goal_list.insert(0, '0')
        elif goal_len > start_len:
            for _ in range(goal_len - start_len):
                start_list.insert(0, '0')


        res = 0
        for i in range(len(start_list)):
            if start_list[i] != goal_list[i]:
                res += 1

        return res

if True:
    def minBitFlips(start, goal):
        res = start ^ goal
        return sum(1 for c in bin(res)[2:] if c =='1')

print(f"{minBitFlips(caseStart_1, caseGoal_1)}")
print(f"{minBitFlips(caseStart_2, caseGoal_2)}")
print(f"{minBitFlips(caseStart_3, caseGoal_3)}")