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
if True:
    def signOfANumber(n):
        return 'Positive' if n > 0 else 'Negative' if n < 0 else 'Zero'
    
    print(f"{signOfANumber(-1)}")
    print(f"{signOfANumber(0)}")
    print(f"{signOfANumber(1)}")