#Merge Two 2D Arrays By Summing Values
#https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/

caseNums1_1 = [[1,2],[2,3],[4,5]]
caseNums2_1 = [[1,4],[3,2],[4,1]]

caseNums1_2 = [[2,4],[3,6],[5,5]]
caseNums2_2 = [[1,3],[4,3]]

if True:
    def solution(nums1, nums2):
        myDict = dict()

        for i in range(len(nums1)):
                myDict[f"{nums1[i][0]}"] = nums1[i][1]

        for i in range(len(nums2)):
            if myDict.get(f"{nums2[i][0]}") is not None:
                myDict[f"{nums2[i][0]}"] += nums2[i][1]
            else:
                myDict[f"{nums2[i][0]}"] = nums2[i][1]

        sortedList = sorted(myDict.items())
        
        myList = []
        for value in sortedList:
             myList.append([value[0], value[1]])

        return myList
    
print(f"{solution(caseNums1_1, caseNums2_1)}")
print(f"{solution(caseNums1_2, caseNums2_2)}")