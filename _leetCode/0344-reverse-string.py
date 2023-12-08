#Reverse String
#https://leetcode.com/problems/reverse-string/description/

import math

testCase1 = ["h","e","l","l","o"]
testCase2 = ["H","a","n","n","a","h"]

if False:
    def reverseString1(case_):
        for i in range(math.floor(len(case_)/2)):
            c = case_[i]
            case_[i] = case_[len(case_) - 1 - i]
            case_[len(case_) - 1 - i] = c
        
        print(f"{case_}")

    reverseString1(testCase1)
    reverseString1(testCase2)

if True:
    def reverseString2(case_):
        halfway = math.floor(len(case_)/2)
        for i in range(halfway):
            mirrorPoint = len(case_) - 1 - i
            case_[i], case_[mirrorPoint] = case_[mirrorPoint], case_[i]

        print(f"{case_}")
        
    reverseString2(testCase1)
    reverseString2(testCase2)