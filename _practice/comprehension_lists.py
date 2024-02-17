#Filter odd numbers
if False:
    def filterOddNumbers(*nums):
        return [n for n in nums if n % 2 != 0]

    ran = []
    for i in range(10):
        ran.append(i)

    print(f"{filterOddNumbers(1, 2, 3, 4, *ran)}")

#Double even numbers
if False:
    def doubleEvenNumbers(*nums):
        return [n*2 for n in nums if n % 2 == 0]
    
    ran = []
    for i in range(7):
        ran.append(i)

    print(f"{doubleEvenNumbers(10, 20, *ran)}")

#Extract initials
if False:
    def extractInitials(*s):
        str_ = []
        for t in s:
            if isinstance(t, str):
                str_.extend(t.split())
            else:
                str_.append(t)

        return [l[0].upper() for l in str_]

    words = ["apple", "fruit", "bob"]
    
    print(f"{extractInitials(*words, 'a long string')}")

#Vowel counter
if False:
    def countVowels(*s):
        words = []
        for arg in s:
            if isinstance(arg, str):
                words.extend(arg.split())
            else:
                words.append(arg)
            
        vowels = ["a","e","i","o","u"]
        return len([c for word in words for c in word if c in vowels])

    print(f"{countVowels('test', *['a', 'other', 'array'], 'this i s a string')}")

#Flatten a list of lists
if False:
    def flattenLists(l):
        return [n for a in l for n in a]

    print(f"{flattenLists([[1, 2], [3, 4], [5, 6]])}")

#Combining two lists
if False:
    def combine(a, b):
        #zip creates tuples
        return [item for pair in zip(a,b) for item in pair]

    print(f"{combine([1,2,3],['a','b','c'])}")

#Sum of squares
if False:
    def sumOfSquares(nums):
        return sum([n**2 for n in nums])
    
    l = []
    for i in range(11):
        l.append(i)

    print(f"{sumOfSquares(l)}")

#Prime numbers
if False:
    def findPrimes(nums):
        
        def is_prime(n):
            if n <= 1:
                return False

            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        return [n for n in nums if is_prime(n)]

    l = []
    for i in range(101):
        l.append(i)

    print(f"{findPrimes(l)}")

#Nested comprehensions
if False:
    def nestedComprehensions(matrix):
        return [[row[col] for row in matrix] for col in range(len(matrix[0]))]

    print(f"{nestedComprehensions([[1,2,3],[4,5,6]])}")


#Linux test
if False:
    def testComprehension():
        return [i for i in range(0, 10) if i % 2 == 0]
    
    print(f"{testComprehension()}")

#Odd numbers
if False:
    def oddNumbers():
        return [i for i in range(0, 11) if i % 2 == 1]
    
    print(f"{oddNumbers()}")

#Square numbers
if False:
    def squareNumbers():
        return [i**2 for i in range(1,11)]
    
    print(f"{squareNumbers()}")

#Even cubes
if False:
    def evenCubes():
        return [i**3 for i in range(1, 21) if i % 2 == 0]
    
    print(f"{evenCubes()}")

#Length of words
if False:
    def lengthOfWords(words):
        return [len(w) for w in words]
    
    lw = ["example", "fruit", "a long string"]
    print(f"{lengthOfWords(lw)}")

#Square or cube
if False:
    def squareOrCube(nums):
        return [n**2 if n%2==0 else n**3 for n in nums]
    
    nl = [n for n in range(1,11)]
    print(f"{squareOrCube(nl)}")