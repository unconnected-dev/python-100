#Check If The Sentence Is Pangram
#https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/

caseSentence_1 = "thequickbrownfoxjumpsoverthelazydog"
caseSentence_2 = "leetcode"

if False:
    def checkIfPangram(sentence):
        return len(set(list(sentence))) == 26

if True:
    def checkIfPangram(sentence):
        return len(set(sentence)) == 26
    
print(f"{checkIfPangram(caseSentence_1)}")
print(f"{checkIfPangram(caseSentence_2)}")