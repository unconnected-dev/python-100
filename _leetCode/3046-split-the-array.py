#Split The Array
#https://leetcode.com/problems/split-the-array/description/

caseNums_1 = [1,1,2,2,3,4]
caseNums_2 = [1,1,1,1]

if True:
    def isPossibleToSplit(nums):
        nums.sort()
        a,b=[],[]
        for i in range(0,len(nums),2):
            a.append(nums[i])
            b.append(nums[i+1])
        
        half = len(nums)//2
        if len(set(a)) == half and len(set(b)) == half:
            return True
        else:
            return False

print(f"{isPossibleToSplit(caseNums_1)}")
print(f"{isPossibleToSplit(caseNums_2)}")