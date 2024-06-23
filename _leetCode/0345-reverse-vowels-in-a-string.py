#Reverse Vowels In A String
#https://leetcode.com/problems/reverse-vowels-of-a-string/description/


caseS_1 = "hello"
caseS_2 = "leetcode"

if False:
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

if False:    
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        arr = set(["a","e","i","o","u","A","E","I","O","U"])

        left, right = 0, len(s) - 1

        while left < right:

            while left < right and s[left] not in arr:
                left += 1
            
            while right > left and s[right] not in arr:
                right -= 1


            if left > right:
                return ''.join(s)
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)

if True:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        arr = set(["a","e","i","o","u",])
        
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and s[left].lower() not in arr:
                left += 1
            
            while right > left and s[right].lower() not in arr:
                right -= 1

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)


print(f"{reverseVowels(caseS_1)}")
print(f"{reverseVowels(caseS_2)}")