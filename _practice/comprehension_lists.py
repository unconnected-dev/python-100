#Filter odd numbers
if False:
    def filterOddNumbers(*nums):
        return [n for n in nums if n % 2 != 0]

    ran = []
    for i in range(10):
        ran.append(i)

    print(f"{filterOddNumbers(1, 2, 3, 4, *ran)}")

#Double even numbers
if False:
    def doubleEvenNumbers(*nums):
        return [n*2 for n in nums if n % 2 == 0]
    
    ran = []
    for i in range(7):
        ran.append(i)

    print(f"{doubleEvenNumbers(10, 20, *ran)}")

#Extract initials
if False:
    def extractInitials(*s):
        str_ = []
        for t in s:
            if isinstance(t, str):
                str_.extend(t.split())
            else:
                str_.append(t)

        return [l[0].upper() for l in str_]

    words = ["apple", "fruit", "bob"]
    
    print(f"{extractInitials(*words, 'a long string')}")

#Vowel counter
if True:
    def countVowels(*s):
        words = []
        for arg in s:
            if isinstance(arg, str):
                words.extend(arg.split())
            else:
                words.append(arg)
            
        vowels = ["a","e","i","o","u"]
        return len([c for word in words for c in word if c in vowels])

    print(f"{countVowels('test', *['a', 'other', 'array'], 'this i s a string')}")