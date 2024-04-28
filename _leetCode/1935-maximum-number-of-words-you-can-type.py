#Maximum Number Of Words You Can Type
#https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/

caseText_1 = "hello world"
caseBrokenLetters_1 = "ad"

caseText_2 = "leet code"
caseBrokenLetters_2 = "lt"

caseText_3 = "leet code"
caseBrokenLetters_3 = "e"

if True:
    def canBeTypedWords(text, brokenLetters):
        words = []
        
        for word in text.split():
            app_ = True
            for c in word:
                if c in brokenLetters:
                    app_ = False
                    break
            
            if app_ == True:
                words.append(word)
            
        return len(words)
    
print(f"{canBeTypedWords(caseText_1, caseBrokenLetters_1)}")
print(f"{canBeTypedWords(caseText_2, caseBrokenLetters_2)}")
print(f"{canBeTypedWords(caseText_3, caseBrokenLetters_3)}")