#Count Elements With Maximum Frequency
#https://leetcode.com/problems/count-elements-with-maximum-frequency/description/
from collections import Counter

caseNums_1 = [1,2,2,3,1,4]
caseNums_2 = [1,2,3,4,5]

if False:
    def maxFrequencyElements(nums):
        max_ = max(nums)
        count = [0] * (max_ + 1)
        
        for n in nums:
            count[n] += 1
        
        max_freq = max(count)
        res = 0
        for n in count:
            if n == max_freq:
                res += n
        
        return res

if False:
    def maxFrequencyElements(nums):
        count = []
        num_set = set(nums)
        for n in num_set:
            count.append(nums.count(n))
        
        max_ = max(count)
        res = 0
        for n in count:
            if n == max_:
               res += n
        
        return res 

if True:
    def maxFrequencyElements(nums):
        count = Counter(nums)
        max_ = max(count[n] for n in count)

        return sum(count[n] for n in count if count[n] == max_)
        
print(f"{maxFrequencyElements(caseNums_1)}")
print(f"{maxFrequencyElements(caseNums_2)}")