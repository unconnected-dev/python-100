#Maximum Value Of A String In An Array
#https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/description/

caseStrs_1 = ["alic3","bob","3","4","00000"]
caseStrs_2 = ["1","01","001","0001"]

if True:
    def maximumValue(strs) -> int:
        max_val = 0

        for i in range(len(strs)):
            try:
                val = int(strs[i])
            except ValueError:
                if len(strs[i]) > max_val:
                    max_val = len(strs[i])
            else:
                if val > max_val:
                    max_val = val
            
        return max_val

print(f"{maximumValue(caseStrs_1)}")
print(f"{maximumValue(caseStrs_2)}")