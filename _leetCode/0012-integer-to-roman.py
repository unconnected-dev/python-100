#Integer To Roman
#https://leetcode.com/problems/integer-to-roman/description/


caseNum_1 = 3
caseNum_2 = 58
caseNum_3 = 1994

if False:
    def integerToRoman(num) -> str:
        m = [
            [1000, "M"],
            [900, "CM"],
            [500, "D"],
            [400, "CD"],
            [100, "C"],
            [90, "XC"],
            [50, "L"],
            [40, "XL"],
            [10, "X"],
            [9, "IX"],
            [5, "V"],
            [4, "IV"],
            [1, "I"],
        ]

        r = ""

        for [dn, str] in m:
            while (num/dn) >= 1:
                r += str
                num -=dn

        return r

if True:
    def integerToRoman(num) -> str:
        res = ""
        while (num > 0):
            if(num >=1000):
                res+="M"
                num-=1000

            elif(num >=900):
                res+="CM"
                num-=900

            elif(num >=500):
                res+="D"
                num-=500

            elif(num >=400):
                res+="CD"
                num-=400

            elif(num >=100):
                res+="C"
                num-=100

            elif(num >=90):
                res+="XC"
                num-=90

            elif(num >=50):
                res+="L"
                num-=50

            elif(num >=40):
                res+="XL"
                num-=40

            elif(num >=10):
                res+="X"
                num-=10

            elif(num >=9):
                res+="IX"
                num-=9

            elif(num >=5):
                res+="V"
                num-=5
            
            elif(num >=4):
                res+="IV"
                num-=4

            elif(num >=1):
                res+="I"
                num-=1        

        return res
        
print(f"{integerToRoman(caseNum_1)}")
print(f"{integerToRoman(caseNum_2)}")
print(f"{integerToRoman(caseNum_3)}")