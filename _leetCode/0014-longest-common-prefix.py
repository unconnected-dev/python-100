#Longest Common Prefix
#https://leetcode.com/problems/longest-common-prefix/description/

caseStrs_1 = ["flower","flow","flight"]
caseStrs_2 = ["dog","racecar","car"]

if True:
    def longestCommonPrefix(strs):
        res = strs[0]
        
        for word in strs:
            while not word.startswith(res):
                res = res[:-1]
        
        return res
    
print(f"{longestCommonPrefix(caseStrs_1)}")
print(f"{longestCommonPrefix(caseStrs_2)}")