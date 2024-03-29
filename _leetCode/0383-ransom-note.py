#Ransom Note
#https://leetcode.com/problems/ransom-note/description/
import collections

caseRansomNote_1 = "a"
caseMagazine_1 = "b"

caseRansomNote_2 = "aa"
caseMagazine_2 = "ab"

caseRansomNote_3 = "aa"
caseMagazine_3 = "aab"

if False:
    def ransomNote(ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        
        aDict = dict()

        #Count up letters in magazine
        for c in list(magazine):
            if c in aDict:
                aDict[c] += 1
            else:
                aDict[c] = 1
        
        #Count down letters in ransomnote
        for c in list(ransomNote):
            if c in aDict and aDict[c] > 0:
                aDict[c] -= 1
            else:
                return False
        
        return True

if True:
    def ransomNote(ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        
        note_count = collections.Counter(ransomNote)
        magazine_count = collections.Counter(magazine)

        for c, count in note_count.items():
            if c not in magazine_count or count > magazine_count[c]:
                return False
            
        return True
        
print(f"{ransomNote(caseRansomNote_1, caseMagazine_1)}")
print(f"{ransomNote(caseRansomNote_2, caseMagazine_2)}")
print(f"{ransomNote(caseRansomNote_3, caseMagazine_3)}")