#Count Number Of Distinct Integers After Reverse Operations
#https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/description/

caseNum_1 = [1,13,10,12,31]
caseNum_2 = [2,2,2]

if True:
    def countDistinctIntegers(nums):
        my_set = set(nums)
        
        for n in nums:
            new_n = int(str(n)[::-1])
            my_set.add(new_n)

        return len(my_set)
    
print(f"{countDistinctIntegers(caseNum_1)}")
print(f"{countDistinctIntegers(caseNum_2)}")