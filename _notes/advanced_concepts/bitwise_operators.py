#Bitwise operators are tools in programming for manipulating individual bits
#within binary representations of data. Unlike traditional arithmetic or
#logical operators that operate on entire numbers or values, bitwise operators
#perform operations at the binary level.

#Bitwise operations are commonly used in tasks related to low-level system
#programming, cryptography, data compression, and optimization.


#Bitwise AND &
#This performs a bitwise AND operation on corresponding bits of two integers.
#It sets each bit to 1 if both bits are 1, otherwise it sets to 0

#Can check for even or odd numbers by Anding with 1
if False:
    result = 2 & 1
    print(f"result of 2: {result}")

    result = 3 & 1
    print(f"result of 3: {result}")

if False:
    a = 5   #Binary: 101
    b = 3   #Binary: 011

    result = a & b #Result: 001 which is the integer 1
    print(f"a: {a}, b: {b}, result: {result}")


#Bitwise OR |
#This performs a bitwise OR operation on corresponding bits of two integers.
#It sets each bit to 1 if at least one of the corresponding bits is 1    
if False:
    a = 5   #Binary: 101
    b = 3   #Binary: 011

    result = a | b  #Result: 111 which is the integer 7
    print(f"a: {a}, b: {b}, result: {result}")


#Bitwise XOR ^
#This performs a bitwise XOR operation on corresponding  bits of two integers.
#This stands for exclusive OR
#It sets each bit to 1 if exactly one of the corresponding bits is 1

#Can compare two values to find differences
if False:
    a = 5   #Binary: 101
    b = 3   #Binary: 011

    result = a ^ b  #Result: 110 which is the integer 6
    print(f"a: {a}, b: {b}, result: {result}")
    

#Bitwise NOT ~
#This performs a bitwise NOT operation on an integer.
#It flips all the bits of the integer converting 1s to 0s and 0s to 1s
if False:
    a = 5   #Binary:101
    
    result = ~a     #Result: 11111111111111111111111111111010 which is the integer -6
    print(f"result: {result}")


#Left shift <<
#This shifts the bits of an integer to the left by a specified number of positions.
#Zeros are shifted into the low-order bits, and the high-order bits that are shfited out are discarded
if False:
    a = 5   #Binary: 101

    result = a << 2     #Result: 10100 which is the integer 20
    print(f"result: {result}")


#Right shift >>
#This shifts the bits of an integer to the right by a specified number of positions.
#Zeros re shifted into thw high-order bits, and the low-order bits that are shifted out are discarded
if False:
    a = 5   #Binary: 101

    result = a >> 2     #Result: 001 which is the integer 1
    print(f"result: {result}")