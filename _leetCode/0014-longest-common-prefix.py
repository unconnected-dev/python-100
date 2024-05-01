#Longest Common Prefix
#https://leetcode.com/problems/longest-common-prefix/description/

caseStrs_1 = ["flower","flow","flight"]
caseStrs_2 = ["dog","racecar","car"]

if False:
    def longestCommonPrefix(strs):
        res = strs[0]
        
        for word in strs:
            while not word.startswith(res):
                res = res[:-1]
        
        return res

if True:
    def longestCommonPrefix(strs):
        min_, max_ = min(strs), max(strs)
        
        for i in range(len(min_)):
            if min_[i] != max_[i]:
                return min_[:i]
        
        return min_
    
print(f"{longestCommonPrefix(caseStrs_1)}")
print(f"{longestCommonPrefix(caseStrs_2)}")