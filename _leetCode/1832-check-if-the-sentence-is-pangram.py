#Check If The Sentence Is Pangram
#https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/

caseSentence_1 = "thequickbrownfoxjumpsoverthelazydog"
caseSentence_2 = "leetcode"

if False:
    def checkIfPangram1(sentence):
        return len(set(list(sentence))) == 26
    
    print(f"{checkIfPangram1(caseSentence_1)}")
    print(f"{checkIfPangram1(caseSentence_2)}")

if True:
    def checkIfPangram2(sentence):
        return len(set(sentence)) == 26
    
    print(f"{checkIfPangram2(caseSentence_1)}")
    print(f"{checkIfPangram2(caseSentence_2)}")