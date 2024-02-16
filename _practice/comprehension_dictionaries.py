#Filter odd numbers
if False:
    def filterOddNumbers(*nums):
        return {n:n for n in nums if n % 2 == 0}

    print(f"{filterOddNumbers(1,2,3,4,5,6,7,8,9,10)}")

#Power of index
if False:
    def powerOfIndex(*nums):
        return {n : n ** i for i, n in enumerate(nums)}
    
    print(f"{powerOfIndex(1,2,3,4,5,6,7,8,9,10)}")

#Keys are strings, values are lengths
if False:
    def keysAreStrings(l):
        return {w: len(w) for w in l}

    print(f"{keysAreStrings(['apple', 'banana', 'orange', 'kiwi'])}")

#Word frequency counter
if False:
    def wordFrequency(l):
        return {w: l.count(w) for w in l.split()}
    
    print(f"{wordFrequency('the quick brown fox jumps over the lazy dog')}")

#Character counter
if False:
    def characterCounter(l):
        return {c: l.count(c) for c in l}

    print(f"{characterCounter('hello')}")

#Letter grades
if False:
    def letterGrades(d):
        return {key: 'A' if val >= 90\
                 else 'B' if val >= 80\
                   else 'C' if val >= 70\
                      else 'D' if val >= 60\
                          else 'F' for key, val in d.items()}

    input_scores = {'Alice': 92, 'Bob': 78, 'Charlie': 64, 'David': 88}
    print(f"{letterGrades(input_scores)}")

#Squares dictionary
if False:
    def squares(n):
        return {n: n**n for n in range(n)}
    
    print(f"{squares(11)}")

#Reverse words
if False:
    def reverseWords(words):
        return {word: word[::-1] for word in words}
    
    print(f"{reverseWords(['apple','pear','pot'])}")

#Celsius to farenheit
if False:
    def convertTemperature(temps):
        return {c: (c*9/5) + 32 for c in temps}

    print(f"{convertTemperature([10,20,30])}")

#Cube even numbers
if False:
    def cubeEvenNumbers(nums):
        return{n: n**3 for n in nums if n % 2 == 0}

    nl = [n for n in range(21)]
    print(f"{cubeEvenNumbers(nl)}")

#Even / False
if False:
    def evenOrFalse(nums):
        return{n: 'Even' if n % 2 == 0 else 'Odd' for n in nums}
    
    nl = [n for n in range(1, 11)]
    print(f"{evenOrFalse(nl)}")

#Strings length
if False:
    def stringsLengths(words):
        return {w: len(w) for w in words}

    wl = ["apple", "pear", "pot"]
    print(f"{stringsLengths(wl)}")

#Character positions
if False:
    def characterPositions(s):
        return{c: ind for ind, c in enumerate(s)}

    print(f"{characterPositions("anexamplestring")}")

#List divisiors
if False:
    def listDivisors(nums):
        return {n: [i for i in range(1, 11) if n % i == 0] for n in nums}
    
    nl = [n for n in range(1, 11)]
    print(f"{listDivisors(nl)}")

#Primes
if False:
    def checkPrime(n):
        if n < 2:
            return False
        
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        
        return True

    def isPrime(nums):
        return {n: checkPrime(n) for n in nums}

    nl = [n for n in range(1, 11)]
    print(f"{isPrime(nl)}")

#List multiples
if False:
    def listMultiples(nums):
        return {n: [i * n for i in range(1, 11)] for n in nums}
    
    nl = [n for n in range(1, 11)]
    print(f"{listMultiples(nl)}")

#To hex
if False:
    def toHex(nums):
        return {n: hex(n) for n in nums}
    
    nl = [n for n in range(1, 11)]
    print(f"{toHex(nl)}")

#Square or cube it
if False:
    def squareOrCube(nums):
        return {n: n**2 if n % 2 == 0 else n ** 3 for n in nums}
    
    nl = [n for n in range(1, 11)]
    print(f"{squareOrCube(nl)}")