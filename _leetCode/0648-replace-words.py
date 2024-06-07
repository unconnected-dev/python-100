#Replace Words
#https://leetcode.com/problems/replace-words/description/

caseDictionary_1 = ["cat","bat","rat"]
caseSentence_1 = "the cattle was rattled by the battery"

caseDictionary_2 = ["a","b","c"]
caseSentence_2 = "aadsfasf absbs bbab cadsfafs"

if True:
    def replaceWords(dictionary, sentence):
        dictionary.sort(key=len)

        words = sentence.split(" ")
        for i in range(len(words)):

            for d in dictionary:
                if words[i].startswith(d):
                    words[i] = d
                    break

        return ' '.join(words)

print(f"{replaceWords(caseDictionary_1, caseSentence_1)}")
print(f"{replaceWords(caseDictionary_2, caseSentence_2)}")