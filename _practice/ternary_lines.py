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

    print(f"{checkStringLength("some characters")}") 
    print(f"{checkStringLength("no")}") 

#Age classifier
if False:
    def classify(age):
        return 'Child' if age < 18 else 'Adult' if age >= 18 and age <= 65 else 'Senior'

    print(f"{classify(17)}") 
    print(f"{classify(18)}") 
    print(f"{classify(65)}") 
    print(f"{classify(66)}") 

if True:
    def checkStringGreater(s, n):
        return True if len(s) > n else False
    
    print(f"{checkStringGreater("test string", 5)}")
    print(f"{checkStringGreater("test string", 10)}")