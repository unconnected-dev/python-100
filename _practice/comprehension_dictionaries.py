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