#Find And Replace Pattern
#https://leetcode.com/problems/find-and-replace-pattern/description/

caseWords_1 = ["abc","deq","mee","aqq","dkd","ccc"]
casePattern_1 = "abb"

caseWords_2 = ["a","b","c"]
casePattern_2 = "a"

if True:
    def findAndReplacePattern(words, pattern):
        res = []
        for word in words:
            my_hash = {}
            my_set = set()
            add_word = True
            
            for i in range(len(word)):
                if pattern[i] not in my_hash and word[i] not in my_set:
                    my_hash[pattern[i]] = word[i]
                    my_set.add(word[i])
                    continue
                
                elif my_hash.get(pattern[i]) != word[i]:
                    add_word = False
                    break
            
            if add_word == True:
                res.append(word)
        
        return res

print(f"{findAndReplacePattern(caseWords_1, casePattern_1)}")
print(f"{findAndReplacePattern(caseWords_2, casePattern_2)}")