#Longest Common Prefix
#https://leetcode.com/problems/longest-common-prefix/description/

caseStrs_1 = ["flower","flow","flight"]
caseStrs_2 = ["dog","racecar","car"]

if False:
    def longestCommonPrefix(strs) -> str:
        res = strs[0]
        
        for word in strs:
            while not word.startswith(res):
                res = res[:-1]

            if len(res) == 0:
                break
            
        return res

if False:
    def longestCommonPrefix(strs) -> str:
        min_, max_ = min(strs), max(strs)
        
        for i in range(len(min_)):
            if min_[i] != max_[i]:
                return min_[:i]
        
        return min_

if True:    
    def longestCommonPrefix(strs) -> str:
        strs.sort()
        first_word, last_word = strs[0], strs[-1]
        res = ""
        for i in range(min(len(first_word), len(last_word))):
            if first_word[i] == last_word[i]:
                res += first_word[i]
            else:
                break
    
        return res
    
print(f"{longestCommonPrefix(caseStrs_1)}")
print(f"{longestCommonPrefix(caseStrs_2)}")