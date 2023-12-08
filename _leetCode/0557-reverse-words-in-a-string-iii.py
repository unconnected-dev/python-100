#Reverse String III
#https://leetcode.com/problems/reverse-words-in-a-string-iii/description/


testCase1 = "Let's take LeetCode contest"
testCase2 = "Mr Ding"

if True:
    def reverseString1(case_):
        splitCase_ = case_.split(" ")

        for i in range(len(splitCase_)):
            word = splitCase_[i]
            splitCase_[i] = word [::-1]

        case_ = " ".join(splitCase_)
        print(f"{case_}")

    reverseString1(testCase1)
    reverseString1(testCase2)