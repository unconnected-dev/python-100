#Fizz Buzz
#https://leetcode.com/problems/fizz-buzz/description/

caseNum_1 = 3
caseNum_2 = 5
caseNum_3 = 15

if True:
    def fizzBuzz(num):
        str = []

        for i in range(0,num+1):
            tStr = ""

            if i%3 == 0:
                tStr += "Fizz"

            if i%5 == 0:
                tStr += "Buzz"
            
            if tStr == "":
                tStr = i
            
            str.append(tStr)
            
        print(f"{str}")
    
    fizzBuzz(caseNum_1)
    fizzBuzz(caseNum_2)
    fizzBuzz(caseNum_3)