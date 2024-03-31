#Split Strings By Separater
#https://leetcode.com/problems/split-strings-by-separator/description/

caseWords_1 = ["one.two.three","four.five","six"]
caseSeparator_1 = "."

caseWords_2 = ["$easy$","$problem$"]
caseSeparator_2 = "$"

caseWords_3 = ["|||"]
caseSeparator_3 = "|"

if False:
    def splitWordsBySeparator(words, separator):
        wordList = []

        for w in words:
            wordList.extend(filter(bool, w.split(separator)))

        return wordList

if True:
    def splitWordsBySeparator(words, separator):
        res = []

        for word in words:
            sl = word.split(separator)
            for split in sl:
                if split:
                    res.append(split)

        return res

print(f"{splitWordsBySeparator(caseWords_1, caseSeparator_1)}")
print(f"{splitWordsBySeparator(caseWords_2, caseSeparator_2)}")
print(f"{splitWordsBySeparator(caseWords_3, caseSeparator_3)}")