#Sorting The Sentence
#https://leetcode.com/problems/sorting-the-sentence/description/

caseS_1 = "is2 sentence4 This1 a3"
caseS_2 = "Myself2 Me1 I4 and3"

if False:
    def sortSentence(s):
        ls = s.split()
        rs = [None for i in range(9)]
        
        for w in ls:
            w_ = w[:-1]
            n_ = w[-1]
            rs[int(n_)] = w_

        return ' '.join([w for w in rs if w != None])

if False:
    def sortSentence(s):
        list_of_words = s.split()
        func_ = lambda word: int(word[-1])
        list_of_words = sorted(list_of_words, key=func_)
        
        return ' '.join([w[:-1] for w in list_of_words])

if True:
    def sortSentence(s):
        ls = s.split()
        res = [''] * len(ls)

        for word in ls:
            w = word[:-1]
            i = word[-1]
            res[int(i)-1] = w
        
        return ' '.join(res)

print(f"{sortSentence(caseS_1)}")
print(f"{sortSentence(caseS_2)}")