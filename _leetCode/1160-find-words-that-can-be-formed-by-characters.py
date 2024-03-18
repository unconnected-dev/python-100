#Find Characters That Can Be Formed By Characters
#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
import collections

caseWords_1 = ["cat","bt","hat","tree"]
caseChars_1 = "atach"

caseWords_2 = ["hello","world","leetcode"]
caseChars_2 = "welldonehoneyr"

if False:
    def countCharacters(words, chars):
        count = 0
        chars_dict = collections.Counter(chars)
        
        for word in words:
            word_dict = collections.Counter(word)

            valid = True
            for key, val in word_dict.items():
                if val > chars_dict.get(key, 0):
                    valid = False
                    break

            if valid == True:
                count += len(word)

        return count

if True:
    def countCharacters(words, chars):
        count = 0
        chars_dict = collections.Counter(chars)

        for word in words:
            if len(word) > len(chars):
                continue

            word_dict = collections.Counter(word)

            valid = True
            for key, val in word_dict.items():
                if val > chars_dict.get(key, 0):
                    valid = False
                    break

            if valid == True:
                count += len(word)

        return count

print(f"{countCharacters(caseWords_1, caseChars_1)}")
print(f"{countCharacters(caseWords_2, caseChars_2)}")