#Filter odd numbers
if False:
    def filterOddNumbers(*nums):
        return {n:n for n in nums if n % 2 == 0}

    print(f"{filterOddNumbers(1,2,3,4,5,6,7,8,9,10)}")

#Power of index
if False:
    def powerOfIndex(*nums):
        return {n : n ** i for i, n in enumerate(nums)}
    
    print(f"{powerOfIndex(1,2,3,4,5,6,7,8,9,10)}")

#Keys are strings, values are lengths
if False:
    def keysAreStrings(l):
        return {w: len(w) for w in l}

    print(f"{keysAreStrings(['apple', 'banana', 'orange', 'kiwi'])}")

#Word frequency counter
if False:
    def wordFrequency(l):
        return {w: l.count(w) for w in l.split()}
    
    print(f"{wordFrequency('the quick brown fox jumps over the lazy dog')}")

#Character counter
if False:
    def characterCounter(l):
        return {c: l.count(c) for c in l}

    print(f"{characterCounter('hello')}")

#Letter grades
if False:
    def letterGrades(d):
        return {key: 'A' if val >= 90\
                 else 'B' if val >= 80\
                   else 'C' if val >= 70\
                      else 'D' if val >= 60\
                          else 'F' for key, val in d.items()}

    input_scores = {'Alice': 92, 'Bob': 78, 'Charlie': 64, 'David': 88}
    print(f"{letterGrades(input_scores)}")

#Squares dictionary
if False:
    def squares(n):
        return {n: n**n for n in range(n)}
    
    print(f"{squares(11)}")

#Reverse words
if False:
    def reverseWords(words):
        return {word: word[::-1] for word in words}
    
    print(f"{reverseWords(['apple','pear','pot'])}")

#Celsius to farenheit
if False:
    def convertTemperature(temps):
        return {c: (c*9/5) + 32 for c in temps}

    print(f"{convertTemperature([10,20,30])}")