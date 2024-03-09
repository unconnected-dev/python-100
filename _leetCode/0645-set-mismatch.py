#Set Mismatch
#https://leetcode.com/problems/set-mismatch/description/

caseNums_1 = [1,2,2,4]
caseNums_2 = [1,1]
caseNums_3 = [2,2]
caseNums_4 = [3,2,3,4,6,5]#1

if True:
    def findErrorNums(nums):
        my_dict = {}
        a = 0
        b = 0
        for n in nums:
            if n in my_dict:
                a = n
                break
            else:
                my_dict[n] = 1

        for i in range(1,len(nums)+1):
            if i not in nums:
                b = i
                break
        
        return [a,b]
            
print(f"{findErrorNums(caseNums_1)}")
print(f"{findErrorNums(caseNums_2)}")
print(f"{findErrorNums(caseNums_3)}")
print(f"{findErrorNums(caseNums_4)}")