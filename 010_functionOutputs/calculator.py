#Calculator

import os
import logo


#Input functions
def inputNum(nth):
    numValid = False
    num

    while numValid == False:
        num = int(input(f"What is the {nth} number?\n"))

        if type(num) == int:
            numValid = True
        else:
            print("Invalid number")

    return num


def inputOp():
    opValid = False
    op

    while opValid == False:
        print(f"+\n-\n*\n/")
        op = input("Pick an operation: \n")

        if(op != "+" and op != "-" and op != "/" and op != "*"):
            print("Invalid operation")
        else:
            opValid = True

    return op


#Operator functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b


#initial
result = 0
print(logo.logo)
print("")

def mainCalc(useResult):
    num1, num2, operator, r

    if useResult == True:
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

    return r


def main():
    continueCalc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n")