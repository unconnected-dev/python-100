#Basic Function Outputs
print("Basic Function Outputs")

#Return tuple
if False:
    def myTuple():
        return "aString", 20

    s, i = myTuple()
    print(f"{s}")
    print(f"{i}")

#Return list
if False:
    def myList():
        return [1,2,3,4]

    #use * for the remaining values
    a,b,*c = myList()

    print(f"{a}")
    print(f"{b}")
    print(f"{c}")

#Return dictionary
if False:
    def myDict():
        d = dict()
        d["a"] = 1
        d["b"] = 2
        d["c"] = 3
        d["d"] = 4
        return d

    a,b,*c = myDict()
    d = myDict()
    
    print(f"{a}")
    print(f"{b}")
    print(f"{c}")
    print(f"{d}")

#Dictionary functions
if False:
    def add(n1, n2):
        return n1 + n2
    
    def minus(n1, n2):
        return n1 - n2
    
    operations = {
        "+": add,
        "-": minus
    }

    num1 = 10
    num2 = 5

    newOperation = operations[input("Please enter + or -\n")]

    print(f"The result is: {newOperation(num1, num2)}")

#Positional arguments
if False:
    def combo(*numbers):
        print(f"{numbers}")
        total = 0
        for num in numbers:
            total += num
        
        return total
    
    print(f"{combo(1,2,*[3,4])}")

