#Remove Duplicates From Sorted Array
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

testCase1 = [1,1,2]
testCase2 = [0,0,1,1,1,2,2,3,3,4]

if False:
    def removeDuplicates(case_):
        i = 0

        aSet = set(case_)
        case_.clear()

        for num in aSet:
            case_.append(num)

        print(f"{case_}")

    removeDuplicates(testCase1)
    removeDuplicates(testCase2)

if False:
    def removeDuplicatesWithPointer(case_):
        i = 0

        while i + 1 < len(case_):
            if case_[i] == case_[i+1]:
                case_.pop(i)
            else:
                i += 1
                
        print(f"{case_}")
    
    removeDuplicatesWithPointer(testCase1)
    removeDuplicatesWithPointer(testCase2)