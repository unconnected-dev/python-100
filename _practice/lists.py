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
    