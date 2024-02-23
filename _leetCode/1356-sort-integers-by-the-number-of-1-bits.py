#Sort Integers By The Number Of 1 Bits
#https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/

caseArr_1 = [0,1,2,3,4,5,6,7,8]
caseArr_2 = [1024,512,256,128,64,32,16,8,4,2,1]

if True:
    def sortByBits(arr):
        f = lambda n: (bin(n).count('1'), n)        
        arr.sort(key=f)
        return arr

print(f"{sortByBits(caseArr_1)}")
print(f"{sortByBits(caseArr_2)}")