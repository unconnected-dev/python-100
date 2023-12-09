#Two Sum
#https://leetcode.com/problems/two-sum/description/

testCase1 = [2,7,11,15]
testVal1 = 9

testCase2 = [3,2,4]
testVal2 = 6

testCase3 = [3,3]
testVal3 = 6

if False:
    def twoSum1(case_, targetVal_):
        storedIndicies = dict()

        for index, num in enumerate(case_):
            target_minus_num = targetVal_ - num

            if target_minus_num in storedIndicies:
                print(f"{index}, {storedIndicies[target_minus_num]}")
                break
            else:
                storedIndicies[num] = index

    twoSum1(testCase1, testVal1)
    twoSum1(testCase2, testVal2)
    twoSum1(testCase3, testVal3)

if False:
    def twoSum2(case_, targetVal_):
        n = len(case_)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if case_[i] + case_[j] == targetVal_:
                    print(f"[{i}, {j}]")
                    break
    
    twoSum2(testCase1, testVal1)
    twoSum2(testCase2, testVal2)
    twoSum2(testCase3, testVal3)