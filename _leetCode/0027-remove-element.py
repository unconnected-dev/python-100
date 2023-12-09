#Remove Element
#https://leetcode.com/problems/remove-element/description/

testCase1 = [3,2,2,3]
testVal1 = 3

testCase2 = [0,1,2,2,3,0,4,2]
testVal2 = 2

if True:
    def removeElement(case_, val_):
        i = 0
        
        while i < len(case_):
            if case_[i] == val_:
                case_.pop(i)
                continue
            
            i += 1

        print(f"{case_}")

    removeElement(testCase1, testVal1)
    removeElement(testCase2, testVal2)