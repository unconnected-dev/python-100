#Valid Palindrome
#https://leetcode.com/problems/valid-palindrome/description/
import re

caseS_1 = "A man, a plan, a canal: Panama"
caseS_2 = "race a car"
caseS_3 = " "
caseS_4 = "Marge, let's \"[went].\" I await {news} telegram."

if False:
    def isPalindrome(s) -> bool:
        s = s.lower().replace(" ", "").replace("!","").replace("?","").replace(".","").replace(",","").replace(":","").replace("@","").replace("#","").replace("_","").replace('"',"").replace("'","").replace("{","").replace("}","").replace("[","").replace("]","").replace("-","").replace(";","").replace("(","").replace(")","").replace("`","")
        return s == s[::-1]

if False:
    def isPalindrome(s) -> bool:
        pattern = r'[^a-zA-Z0-9]+'
        s = re.sub(pattern, '', s.lower())
        return s == s[::-1]

if False:
    def isPalindrome(s) -> bool:
        res = ""
        for c in s:
            if c.isalnum(): 
                res += c.lower()
        
        return res == res[::-1]

if False:
    def isPalindrome(s) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            #Skip over special characters
            while left < right and s[left].isalnum() == False:
                left += 1
            
            while right > left and s[right].isalnum() == False:
                right -= 1

            #Actual letter / number comparison
            if left > right or s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True

if True:
    def isPalindrome(s) -> bool:
        s = ''.join(c.lower() for c in s if s.isalnum())
        return s == s[::-1]

print(f"{isPalindrome(caseS_1)}")
print(f"{isPalindrome(caseS_2)}")
print(f"{isPalindrome(caseS_3)}") 
print(f"{isPalindrome(caseS_4)}") 