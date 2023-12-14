#Count The Number Of Consistent Strings
#https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

caseAllowed_1 = "ab"
caseWords_1 = ["ad","bd","aaab","baa","badab"]

caseAllowed_2 = "abc"
caseWords_2 = ["a","b","c","ab","ac","bc","abc"]

caseAllowed_3 = "cad"
caseWords_3 = ["cc","acd","b","ba","bac","bad","ac","d"]

if True:
    def countTheNumberOfConsistentStrings(allowed, words):
        mySet = set(list(allowed))
        consistent = 0

        for word in words:
            consistent += 1

            for c in word:
                if c not in mySet:
                    consistent -= 1
                    break
        
        print(f"{consistent}")

    countTheNumberOfConsistentStrings(caseAllowed_1, caseWords_1)
    countTheNumberOfConsistentStrings(caseAllowed_2, caseWords_2)
    countTheNumberOfConsistentStrings(caseAllowed_3, caseWords_3)
