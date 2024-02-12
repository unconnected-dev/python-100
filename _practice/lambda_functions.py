#Sort list of tuples
if False:
    def sortTuples(t):
        f = lambda a: a[1]
        return sorted(t, key=f)

    print(f"{sortTuples([('a',1),('b',3),('c',2)])}")

#Filter even numbers
if False:
    def filterEven(nums):
        is_even = lambda n: n % 2 == 0 
        return list(filter(is_even, nums))

    l = []
    for i in range(20):
        l.append(i)

    print(f"{filterEven(l)}")

#Map function to square
if False:
    def squareMe(nums):
        f = lambda n: n**2
        return list(map(f, nums))

    print(f"{squareMe([1,2,3,4,5,6,7,8,9])}")

#Convert c to f
if False:
    def celsiusToFernheit(temps):
        f = lambda n: (n * 9/5) + 32
        return list(map(f, temps))

    print(f"{celsiusToFernheit([10,20,30])}")

#Convert a list of strings to uppercase
if False:
    def toUpperCase(l):
        f = lambda w: w.upper()
        return list(map(f, l))

    print(f"{toUpperCase(['apple','fruit','gray'])}")

#Compute length of each word in a list of strings
if False:
    def calcLen(l):
        f = lambda w: len(w)
        return sum(map(f, l))
    
    print(f"{calcLen(['apple','fruit','pair'])}")

#Compute the square root of each number in a list
if False:
    def calcSquareRoots(nums):
        f = lambda n: n ** 0.5
        return list(map(f, nums))
    
    print(f"{calcSquareRoots([4,25,36])}")

#Convert a list of integers to their corresponding binary representation
if True:
    def toBinary(nums):
        f = lambda n: bin(n)
        return list(map(f, nums))

    print(f"{toBinary([1,2,3,4,5,6])}")