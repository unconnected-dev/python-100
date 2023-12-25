#Decode The Message
#https://leetcode.com/problems/decode-the-message/description/

caseKey_1 = "the quick brown fox jumps over the lazy dog"
caseMessage_1 = "vkbs bs t suepuv"

caseKey_2 = "eljuxhpwnyrdgtqkviszcfmabo"
caseMessage_2 = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"

if True:
    def decodeTheMessage(key, message) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        myDict = dict()
        myDict[" "] = " "
        i = 0

        for c in key:
            if c not in myDict:
                myDict[c] = alphabet[i]
                i += 1

        returnString = ""
        for c in list(message):
            returnString += myDict[c]

        return returnString
    
    print(f"{decodeTheMessage(caseKey_1, caseMessage_1)}")
    print(f"{decodeTheMessage(caseKey_2, caseMessage_2)}")