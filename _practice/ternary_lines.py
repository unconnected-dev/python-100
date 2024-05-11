from math import factorial

#Check even or odd
if False:
    for i in range(0, 10):
        result = "Even" if i % 2 == 0 else "Odd"
        print(f"{i} is {result}")

#Return absolute value
if False:
    l = []
    for i in range(-5, 5):
        l.append(i)

    for n in l:
        result = n if n >= 0 else n * -1
        print(f"abs: {result}")

#Grade letter
if False:
    grade = 77

    result = 'A' if grade >= 90 else \
            'B' if grade >= 80 else \
            'C' if grade >= 70 else \
            'D' if grade >= 60 else \
            'F'
    
    print(f"{result}")

#Maximum of three numbers
if False:
    a = 2
    b = 3
    c = 10

    result = a if a > b and a > c else \
            b if b > a and b > c else \
            c
    
    print(result)

#Sign of a number
if False:
    def signOfANumber(n):
        return 'Positive' if n > 0 else 'Negative' if n < 0 else 'Zero'
    
    print(f"{signOfANumber(-1)}")
    print(f"{signOfANumber(0)}")
    print(f"{signOfANumber(1)}")

#Grade checker
if False:
    def gradeChecker(n):
        return 'Passed' if n >= 60 else 'Failed'
    
    print(f"{gradeChecker(59)}")
    print(f"{gradeChecker(60)}")
    print(f"{gradeChecker(61)}")

#Absolute
if False:
    def absolute(n):
        return n if n >= 0 else n * -1
    
    print(f"{absolute(-1)}")
    print(f"{absolute(1)}")

#Sign check
if False:
    def signCheck(n):
        return 'Positive' if n > 0 else 'Negative' if n < 0 else 'Zero'
    
    print(f"{signCheck(-1)}")
    print(f"{signCheck(0)}")
    print(f"{signCheck(1)}")

#String length
if False:
    def checkStringLength(s):
        return 'Short' if len(s) <= 5 else 'Long'

    print(f"{checkStringLength('some characters')}") 
    print(f"{checkStringLength('no')}") 

#Age classifier
if False:
    def classify(age):
        return 'Child' if age < 18 else 'Adult' if age >= 18 and age <= 65 else 'Senior'

    print(f"{classify(17)}") 
    print(f"{classify(18)}") 
    print(f"{classify(65)}") 
    print(f"{classify(66)}") 

#Greater than
if False:
    def checkStringGreater(s, n):
        return True if len(s) > n else False
    
    print(f"{checkStringGreater('test string', 5)}")
    print(f"{checkStringGreater('test string', 10)}")

#Even or odd
if False:
    def evenOrOdd(n):
        return True if n % 2 == 0 else False
    
    print(f"{evenOrOdd(1)}")
    print(f"{evenOrOdd(2)}")
    print(f"{evenOrOdd(3)}")

#Return max
if False:
    def returnMax(a,b):
        return a if a >= b else b
    
    print(f"{returnMax(1,2)}")
    print(f"{returnMax(2,1)}")
    print(f"{returnMax(3,3)}")

#Find minimum of three numbers
if False:
    def findMin(a,b,c):
        return a if a < b and a < c else b if b < c else c
    
    print(f"{findMin(1,2,3)}")
    print(f"{findMin(4,2,3)}")
    print(f"{findMin(4,5,3)}")

#Leap year
if False:
    def isLeapYear(year):
        return True if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else False

    print(f"{isLeapYear(1999)}")
    print(f"{isLeapYear(2000)}")
    print(f"{isLeapYear(2004)}")

#Vowel or consonant
if False:
    def vowelOrConsonant(c):
        return 'Vowel' if c in 'aeiouAEIOU' else 'Consonant'
    
    print(f"{vowelOrConsonant('a')}")
    print(f"{vowelOrConsonant('U')}")
    print(f"{vowelOrConsonant('b')}")

#Positive, negative or zero
if False:
    def numberIs(n):
        return 'Positive' if n > 0 else 'Negative' if n < 0 else 'Zero'
    
    print(f"{numberIs(-1)}")
    print(f"{numberIs(0)}")
    print(f"{numberIs(1)}")

#Factorial
if False:
    def factorialTime(n):
        return 1 if n == 1 else factorial(n)
    
    print(f"{factorialTime(4)}")
    print(f"{factorialTime(1)}")

#Prime time
if False:
    def primeTime(n):
        nl = [num for num in range(2,int(n*0.5))]
        return True if all(n%num != 0 for num in nl) else False
    
    print(f"{primeTime(3)}")
    print(f"{primeTime(5)}")
    print(f"{primeTime(6)}")

#Square root
if True:
    def squareRootIs(n):
        return n**0.5 if n >= 0 else 'What?'

    print(f"{squareRootIs(-1)}")
    print(f"{squareRootIs(0)}")
    print(f"{squareRootIs(10)}")