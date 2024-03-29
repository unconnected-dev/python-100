#Filter odd numbers
from math import factorial


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

    print(f"{characterPositions('anexamplestring')}")

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

#Km to miles
if False:
    def kmToMiles(nums):
        return {n:n*0.621371 for n in nums}
    
    nl = [n for n in range(1,11)]
    print(f"{kmToMiles(nl)}")

#Squares
if False:
    def squares(nums):
        return {n: n**2 for n in nums}
    
    nl = [n for n in range(1,11)]
    print(f"{squares(nl)}")

#Cubes
if False:
    def cubes(nums):
        return {n: n**3 for n in nums}
    
    nl = [n for n in range(1,11)]
    print(f"{cubes(nl)}")

#Ascii
if False:
    def ascii(letters):
        return {l: ord(l) for l in letters}
    
    l = list("abcdefghijklmnopqrstuvwxyz")
    print(f"{ascii(l)}")

#Factorals
if False:
    f = lambda n: 1 if n == 0 else n * factorial(n - 1)
    def factorals(nums):
        return {n: f(n) for n in nums}

    nl = [n for n in range(1,11)]
    print(f"{factorals(nl)}")

#Frequency
if False:
    def frequency(words):
        return {w: words.count(w) for w in words}

    wl = ["apple","pear","orange","berry","pear","pear","orange"]
    print(f"{frequency(wl)}")

#Binary
if False:
    def toBinary(nums):
        return {num: bin(num) for num in nums}
    
    wl = [n for n in range(1,11)]
    print(f"{toBinary(wl)}")

#Ascii
if False:
    def toAscii(words):
        return {word: ''.join([str(ord(c)) for c in word]) for word in words}

    wl = ["apple","pear","orange","berry"]
    print(f"{toAscii(wl)}")

#Even or odd
if False:
    def evenOrOdd(nums):
        return {num: "Even" if num % 2 == 0 else "Odd" for num in nums}
    
    nl = [i for i in range(1,11)]
    print(f"{evenOrOdd(nl)}")

#Power of 5
if False:
    def powerOfFive(nums):
        return {num: num ** 5 for num in nums}
    
    nl = [i for i in range(21)]
    print(f"{powerOfFive(nl)}")

#Is prime
if False:
    def checkPrime(n):
        if n <= 1:
            return False
        
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False

        return True
    
    def getPrimes(nums):
        return {n: checkPrime(n) for n in nums}
    
    nl = [i for i in range(2,31)]
    print(f"{getPrimes(nl)}")

#To hex
if False:
    def toHex(nums):
        return {n: hex(n) for n in nums}
    
    nl = [_ for _ in range(1,21)]
    print(f"{toHex(nl)}")