#How Many Numbers Are Smaller Than The Current Number
#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

caseNums_1 = [8,1,2,2,3]
caseNums_2 = [6,5,4,8]
caseNums_3 = [7,7,7,7]

if False:
    def howManyNumbersAreSmallerThanTheCurrentNumber(nums):
        ind = []
        sortedNums = nums.copy()
        sortedNums.sort()
        
        for num in nums:
            ind.append(sortedNums.index(num))

        return ind

if False:
    def howManyNumbersAreSmallerThanTheCurrentNumber(nums):
        nums_sorted = sorted(nums)
        return [nums_sorted.index(n) for n in nums]
    
#Tried using a map to make things more efficient in the case 
#of searhcing for repeated numbers
if True:
    def howManyNumbersAreSmallerThanTheCurrentNumber(nums):
        my_map = {}

        res = []
        for n in nums:
            if n in my_map:
                res.append(my_map.get(n))
            else:
                count = 0
                for j in nums:
                    if j < n:
                        count += 1
                my_map[n] = count
                res.append(count)
        return res

print(f"{howManyNumbersAreSmallerThanTheCurrentNumber(caseNums_1)}")
print(f"{howManyNumbersAreSmallerThanTheCurrentNumber(caseNums_2)}")
print(f"{howManyNumbersAreSmallerThanTheCurrentNumber(caseNums_3)}")