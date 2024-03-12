
#Data Types
if False:
    #String
    aString = "Hello"

    #Subscripting
    print(aString[0])
    print(aString[len(aString) - 1])

    #Large Integers
    #Underscore is used as a way to show a number with commas for thousands etc to break up visually
    #In print below will show 123456789
    print(123_456_789)

    #Float
    #Can also use underscore
    print(3.14159)


#Mathmatical Operators
if False:
    #Converts type to float
    print(type(6 / 3))

    #Power of
    print(type(2 ** 2))

    #Priority is PEMDAS
    #Parentheses    ()
    #Exponents      **
    #Multiplication *   Multiplication and division are the same priority
    #Division       /   Whichever is most left is calculated first
    #Addition       + 
    #Subtraction    -

    #7.0
    print(3 * 3 + 3 / 3 - 3)

    #3.0
    print(3 * (3 + 3) / 3 - 3)

    #Round numbers
    print(round(8 / 3, 2))

    #Use double / for floor
    print(8//3)


#f-string
if False:
    score = 0
    height = 1.8
    winning = True

    print(f"Your score is {score}. Your height is {height}. You are winning is {winning}")


#Type Conversion
if False:
    # num_char = len(input("What is your name?\n"))
    #num_char is not converted
    # print("Your name as " + num_char + " characters.")

    #To check a variable type
    # print(type(num_char))
    #To convert a variable type
    # print("Your name as " + str(num_char) + " characters.")


    print(70 + float("100.5"))  #170.5
    print(str(70) + str(100))   #70100