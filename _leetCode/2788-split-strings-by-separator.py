#Split Strings By Separater
#https://leetcode.com/problems/split-strings-by-separator/description/

caseWords_1 = ["one.two.three","four.five","six"]
caseSeparator_1 = "."

caseWords_2 = ["$easy$","$problem$"]
caseSeparator_2 = "$"

caseWords_3 = ["|||"]
caseSeparator_3 = "|"

if True:
    def splitWordsBySeparator(words, separator):
        wordList = []

        for w in words:
            wordList.extend(filter(bool, w.split(separator)))

        return wordList

print(f"{splitWordsBySeparator(caseWords_1, caseSeparator_1)}")
print(f"{splitWordsBySeparator(caseWords_2, caseSeparator_2)}")
print(f"{splitWordsBySeparator(caseWords_3, caseSeparator_3)}")