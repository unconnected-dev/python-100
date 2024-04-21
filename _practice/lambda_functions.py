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
if False:
    def toBinary(nums):
        f = lambda n: bin(n)
        return list(map(f, nums))

    print(f"{toBinary([1,2,3,4,5,6])}")

#Square or cube
if False:
    def squareOrCube(nums):
        f = lambda n: n**2 if n%2==0 else n**3
        return list(map(f, nums))
    
    print(f"{squareOrCube([n for n in range(1,11)])}")

#Primes
if False:
    def isPrime(n):
        if n < 2:
            return False
        
        for i in range(2, n//2 + 1):
            if n%i==0:
                return False
        
        return True
    

    def isPrimes(nums):
        f = lambda n: isPrime(n)
        return list(map(f, nums))
    
    print(f"{isPrimes([n for n in range(1,11)])}")

#Multiples
if False:
    def makeMultiples(n):
        return [n*i for i in range(1, 11)]

    def mapMultiples(nums):    
        f = lambda n: makeMultiples(n)
        return list(map(f, nums))
    
    print(f"{mapMultiples([n for n in range(1,11)])}")

#Divisors
if False:
    def mapDivisors(nums):
        f = lambda n: [i for i in range(1,11) if n % i == 0]
        return list(map(f, nums))
    
    print(f"{mapDivisors([i for i in range(1,11)])}")

#Square or cube
if False:
    def squareOrCube(nums):
        f = lambda n: n**2 if n %2==0 else n**3
        return list(map(f, nums))

    print(f"{squareOrCube([i for i in range(1,10)])}")

#Upper lower
if False:
    def upperLower(words):
        f = lambda w: w[1].upper() if w[0]%2==1 else w[1].lower()
        return ''.join(map(f, enumerate(words)))
    
    print(f'{upperLower(["apple","pear","tea","four"])}')

#Camel case
if False:
    def camelCase(words):
        f = lambda w: w.capitalize()
        result =  ''.join(map(f, words))
        return result[0].lower() + result[1:]
    
    print(f'{camelCase(["apple","pear","tea","four"])}')

#Power of index
if False:
    def powerOf(nums):
        f = lambda n: [f"{n[0]} ** {n[1]}", n[1] ** n[0]]
        return list(map(f, enumerate(nums)))
    
    print(f"{powerOf([i for i in range(1,11)])}")

#Square of a number
if False:
    def squareOf(nums):
        f = lambda n: n**2
        return list(map(f,nums))
    
    print(f"{squareOf([n for n in range(1,6)])}")

#Check if a number is even
if False:
    def isEven(nums):
        f = lambda n: n % 2 == 0
        return list(map(f,nums))
    
    print(f"{isEven([n for n in range(1,6)])}")

#Sum of two nums
if False:
    def sumOf(nums):
        f = lambda pair: sum(pair)
        return list(map(f, nums))
    
    print(f"{sumOf([[1,2],[3,4],[5,6]])}")

if False:
    def sumOf(nums):
        f = lambda a, b: a + b
        #The * will unpack each array of two numbers
        return list(map(lambda x: f(*x), nums))

    print(sumOf([[1,2],[3,4],[5,6]]))

#Sort tuples by the second element
if False:
    def sortTuples(manyTuples):
        f = lambda tuple: tuple[1]
        return sorted(manyTuples,key=f)
    
    print(f"{sortTuples([(1,2),(8,9),(6,7),(4,5)])}")

#Filter a list of numbers and return only the positive ones
if False:
    def positives_only(nums):
        f = lambda n: n % 2 == 0
        return list(filter(f, nums))
    
    print(f"{positives_only([n for n in range(1,6)])}")

#Power of two
if False:
    def power_of_two(nums):
        f = lambda n: n ** 2
        return list(map(f, nums))
    
    print(f"{power_of_two([n for n in range(1, 11)])}")
    
#Alternate power
if False:
    def alternate_power(nums):
        f = lambda n: n**2 if n%2==0 else n**3
        return list(map(f, nums))
    
    print(f"{alternate_power([n for n in range(1, 11)])}")
    
#Filter odd numbers
if False:
    def filter_odds(nums):
        f = lambda n: n%2==0
        return list(filter(f, nums))

    print(f"{filter_odds([n for n in range(1, 11)])}")

#Convert to binary
if False:
    def convert_to_binary(nums):
        f = lambda n: bin(n)
        return list(map(f, nums))
    
    print(f"{convert_to_binary([n for n in range(1, 11)])}")