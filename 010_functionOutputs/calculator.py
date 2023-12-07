#Calculator
import logo


#Input functions
def inputNum(nth):
    numValid = False
    num = 0

    while numValid == False:
        num = int(input(f"What is the {nth} number?\n"))

        if type(num) == int:
            numValid = True
        else:
            print("Invalid number, please try again")

    return num


def inputOp():
    opValid = False
    op = ""

    while opValid == False:
        print(f"+\n-\n*\n/")
        op = input("Pick an operation: \n")

        if(op != "+" and op != "-" and op != "/" and op != "*"):
            print("Invalid operation, please try again")
        else:
            opValid = True

    return op


#Operator functions
def add(a, b):
    print(f"{a} + {b}")
    return a + b

def sub(a, b):
    print(f"{a} - {b}")
    return a - b

def mult(a, b):
    print(f"{a} * {b}")
    return a * b

def div(a, b):
    print(f"{a} / {b}")
    return a / b


def mainCalc(useResult, result):
    num1 = 0
    num2 = 0
    operator = ""
    r = 0

    if useResult == True:
        print(f"Continuing with {result}")
        num1 = result
    else:
        num1 = inputNum("first")

    operator = inputOp()
    num2 = inputNum("second")

    match operator:
        case "+":
            r = add(num1, num2)
        case "-":
            r = sub(num1, num2)
        case "*":
            r = mult(num1, num2)
        case "/":
            r = div(num1, num2)

    print(f"{r}")
    input("Press Enter to continue...")
    return r


def main(continueCalc, result):
    if(continueCalc == 'y'):
        result = mainCalc(True, result)
    else:
        result = mainCalc(False, result)

    return result


continueCalc = ""
result = 0
while True:
    print(logo.logo)
    print("")
    
    result = main(continueCalc, result)

    continueCalc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n")