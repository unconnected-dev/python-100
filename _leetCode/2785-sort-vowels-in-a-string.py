#Sort Vowels In A String
#https://leetcode.com/problems/sort-vowels-in-a-string/description/

caseS_1 = "lEetcOde"
caseS_2 = "lYmpH"

if True:
    def sortVowels(s):
        result = list(s)
        vowels = []
        positions = []

        vowels_dict = {"a", "e", "i", "o", "u", "A", "E", "I", "O", ""}

        for i, c in enumerate(s):
            if c in vowels_dict:
                vowels.append(c)
                positions.append(i)
        
        vowels.sort()

        for j in range(len(vowels)):
            result[positions[j]] = vowels[j]

        return ''.join(result)

print(f"{sortVowels(caseS_1)}")
print(f"{sortVowels(caseS_2)}")