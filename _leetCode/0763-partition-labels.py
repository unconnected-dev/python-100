#Partition Labels
#https://leetcode.com/problems/partition-labels/description/

caseS_1 = "ababcbacadefegdehijhklij"
caseS_2 = "eccbbbbdec"

if True:
    def partitionLabels(s):
        left, right = 0, 0
        res = []

        my_set = set()
        while right < len(s):
            right = s.rfind(s[right])
            part = s[left:right+1]

            my_set.clear()
            my_set = set(list(part))
            part_found = True
            for c in my_set:
                if s.rfind(c) > right:
                    right = s.rfind(c)
                    part_found = False
            
            if part_found == True:
                res.append(len(s[left:right+1]))
                right += 1
                left = right

        return res

print(f"{partitionLabels(caseS_1)}")
print(f"{partitionLabels(caseS_2)}")