#Top K Frequent Elements
#https://leetcode.com/problems/top-k-frequent-elements/description/
import collections

caseNums_1 = [1,1,1,2,2,3]
caseK_1 = 2

caseNums_2 = [1]
caseK_2 = 1

if False:
    def topKFrequent(nums, k):
        count_ = collections.Counter(nums)
        f= lambda item: -item[1]
        sorted_ = dict(sorted(count_.items(), key=f))

        res = []
        for key, value in sorted_.items():
            if len(res) < k:
                res.append(key)

        return res
    
if True:
    def topKFrequent(nums, k):
        count_ = collections.Counter(nums)
        sorted_ = dict(sorted(count_.items(), key=lambda item: -item[1]))

        res = []
        for key in sorted_.keys():
            if len(res) < k:
                res.append(key)

        return res


print(f"{topKFrequent(caseNums_1, caseK_1)}")
print(f"{topKFrequent(caseNums_2, caseK_2)}")