#Reverse Vowels In A String
#https://leetcode.com/problems/reverse-vowels-of-a-string/description/


caseS_1 = "hello"
caseS_2 = "leetcode"

if True:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        arr = set(["a","e","i","o","u","A","E","I","O","U"])
        def isVowel(c):
            return c in arr

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and isVowel(s[left]) == False:
                left += 1
            
            while right > left and isVowel(s[right]) == False:
                right -= 1


            if left > right:
                return ''.join(s)
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)
    
print(f"{reverseVowels(caseS_1)}")
print(f"{reverseVowels(caseS_2)}")