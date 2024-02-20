#Sort Characters By Frequency
#https://leetcode.com/problems/sort-characters-by-frequency/description/

from collections import Counter


caseS_1 = "tree"
caseS_2 = "cccaaa"
caseS_3 = "Aabb"

if False:
    def frequencySort(s):
        s_set = set(s)
        
        s_dict = {c: s.count(c) for c in s_set}
        f = lambda item: (-item[1], item[0])
        s_dict = sorted(s_dict.items(), key=f)

        result = ""
        for item in s_dict:
            for _ in range(item[1]):
                result += item[0]

        return result

if True:
    def frequencySort(s):
        s_dict = Counter(s)
        s_list = list(s_dict.items())

        f = lambda item: (-item[1], item[0])
        s_list = sorted(s_list, key=f)

        result = [c*n for c,n in s_list]
        
        return ''.join(result)

print(f"{frequencySort(caseS_1)}")
print(f"{frequencySort(caseS_2)}")
print(f"{frequencySort(caseS_3)}")