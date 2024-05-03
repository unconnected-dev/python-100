#Compare Version Numbers
#https://leetcode.com/problems/compare-version-numbers/description/

caseVersion1_1 = "1.01"
caseVersion2_1 = "1.001"

caseVersion1_2 = "1.0"
caseVersion2_2 = "1.0.0"

caseVersion1_3 = "0.1"
caseVersion2_3 = "1.1"

if True:
    def compareVersion(version1, version2):
        v1_list = version1.split(".")
        v2_list = version2.split(".")

        l = max(len(v1_list),len(v2_list))

        for i in range(l):
            v1 = int(v1_list[i]) if i < len(v1_list) else 0
            v2 = int(v2_list[i]) if i < len(v2_list) else 0

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        
        return 0

print(f"{compareVersion(caseVersion1_1, caseVersion2_1)}")
print(f"{compareVersion(caseVersion1_2, caseVersion2_2)}")
print(f"{compareVersion(caseVersion1_3, caseVersion2_3)}")
