#Valid Palindrome
#https://leetcode.com/problems/valid-palindrome/description/
import re

caseS_1 = "A man, a plan, a canal: Panama"
caseS_2 = "race a car"
caseS_3 = " "
caseS_4 = "Marge, let's \"[went].\" I await {news} telegram."

if False:
    def isPalindrome(s):
        s = s.lower().replace(" ", "").replace("!","").replace("?","").replace(".","").replace(",","").replace(":","").replace("@","").replace("#","").replace("_","").replace('"',"").replace("'","").replace("{","").replace("}","").replace("[","").replace("]","").replace("-","").replace(";","").replace("(","").replace(")","").replace("`","")
        return s == s[::-1]

if False:
    def isPalindrome(s):
        pattern = r'[^a-zA-Z0-9]+'
        s = re.sub(pattern, '', s.lower())
        return s == s[::-1]

if True:
    def isPalindrome(s):
        res = ""
        for c in s:
            if c.isalnum() : res += c.lower()
        
        return res == res[::-1]

print(f"{isPalindrome(caseS_1)}")
print(f"{isPalindrome(caseS_2)}")
print(f"{isPalindrome(caseS_3)}") 
print(f"{isPalindrome(caseS_4)}") 