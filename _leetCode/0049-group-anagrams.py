#Group Anagrams
#https://leetcode.com/problems/group-anagrams/description/
import collections

caseStrs_1 = ["eat","tea","tan","ate","nat","bat"]
caseStrs_2 = [""]
caseStrs_3 = ["a"]

#Time Exceeded 
if False:
    def groupAnagrams(strs):
        res = []
        res.append([strs[0]])

        if len(strs) > 1:
            for i in range(1, len(strs)):
                found = False
                w_count = collections.Counter(strs[i])

                for j in range(len(res)):

                    if len(res[j][0]) != len(strs[i]):
                        continue
                    
                    s_count = collections.Counter(res[j][0])

                    if s_count == w_count:
                        res[j].append(strs[i])
                        found = True
                        break

                if found == False:    
                    res.append([strs[i]])

        return res

if True:
    def groupAnagrams(strs):
        res = {}

        for word in strs:
            k = ''.join(sorted(word))
            
            if k in res:
                res[k].append(word)
            else:
                res[k] = [word]
        
        return list(res.values())

print(f"{groupAnagrams(caseStrs_1)}")
print(f"{groupAnagrams(caseStrs_2)}")
print(f"{groupAnagrams(caseStrs_3)}")