#List reversal
if False:
    def reverseTheList(l):
        l.reverse()
        return l

    print(f"{reverseTheList([1,2,3,4,5])}")

if False:
    def reverseTheList(l):
        return l[::-1]
    
    print(f"{reverseTheList([1,2,3,4,5])}")

if False:
    def reverseTheList(l):
        rl = []
        for i in range(len(l) - 1, -1, -1):
            rl.append(l[i])
        
        return rl
    
    print(f"{reverseTheList([1,2,3,4,5])}")

#Sum total
if False:
    def sumTotal(*nums):
        total = 0
        for n in nums:
            total += n
        
        return total
    
    print(f"{sumTotal(1,2,3,*[4,5,6])}")

if False:
    def sumTotal(*nums):
        return sum(nums)
    
    print(f"{sumTotal(1,2,3,*[4,5,6])}")

#All elements are unique
if False:
    def areUnique(arg):
        
        while len(arg) > 0:
            el = arg.pop()
            if el in arg:
                return False
        
        return True
    
    print(f"{areUnique([1,2,3,4,5,5])}")

if False:
    def areUnique(arg):
        arg_set = set(arg)
        return len(arg) == len(arg_set)
    
    print(f"{areUnique([1,2,3,4,5])}")

#Return first character of strings
if False:
    def firstCharacter(*s):
        rl = []
        for t in s:
            if isinstance(t, str):
                rl.extend(t.split())
            else:
                rl.append(t)

        for i in range(len(rl)):
            rl[i] = rl[i][0]

        return rl

    print(f"{firstCharacter('multiple words', *['more', 'words'])}")

#Remove all odd numbers
if False:
    def removeAllOdd(nums):
        return list(filter(lambda n: n % 2 != 0 , nums))

    l = []
    for i in range(10):
        l.append(i)
    
    print(f"{removeAllOdd(l)}")

if False:
    def removeAllOdd(nums):
        return [n for n in nums if n % 2 != 0]
    
    l = []
    for i in range(10):
        l.append(i)
    
    print(f"{removeAllOdd(l)}")
    
#2 to 5
if False:
    def twoToFive(nums):
        return nums[2:5]

    l = []
    for i in range(10):
        l.append(i)
    
    print(f"{twoToFive(l)}")
    
#Last three elements
if False:
    def lastThree(nums):
        return nums[-3:]

    print(f"{lastThree([1,2,3,4,5,6])}")

#Every other element
if False:
    def everyOther(nums):
        return nums[::2]
    
    print(f"{everyOther([1,2,3,4,5,6])}")

#Reversed with slice
if False:
    def reverseSliced(nums):
        return nums[len(nums)-1::-1]
    
    print(f"{reverseSliced([1,2,3,4,5,6])}")

#String of odd indicies
if False:
    def oddIndicies(s):
        return s[1::2]

    print(f"{oddIndicies('notimetodie')}")

#Square numbers
if False:
    def squareNumbers(nums):
        return [n**2 for n in nums]
    
    print(f"{squareNumbers([1,2,3,4,5,6])}")

if False:
    def squareNumbers(nums):
        return list(map(lambda n: n ** 2, nums))
    
    print(f"{squareNumbers([1,2,3,4,5,6])}")

if True:
    import random
    def randomlyMix(nums):
        return sorted(nums, key = lambda n: random.randint(0, 5))

    l = []
    for i in range(100):
        l.append(i)

    print(f"{randomlyMix(l)}")