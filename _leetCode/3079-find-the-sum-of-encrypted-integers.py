#Find The Sum Of Encrypted Integers
#https://leetcode.com/problems/find-the-sum-of-encrypted-integers/description/

from typing import List

caseNums_1 = [1,2,3]
caseNums_2 = [10,21,31]

if True:
    def sumOfEncryptedInt(nums: List[int]) -> int:
        res = 0
        
        for n in nums:
            ns = str(n)
            l = len(ns)

            for i in range(9,-1,-1):
                if str(i) in ns:
                    res += int(''.join([str(i)]*l))
                    break
                
        return res    
    
print(f"{sumOfEncryptedInt(caseNums_1)}")
print(f"{sumOfEncryptedInt(caseNums_2)}")