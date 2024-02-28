#Count Distinct Numbers On Board
#https://leetcode.com/problems/count-distinct-numbers-on-board/description/

caseN_1 = 5
caseN_2 = 3

if False:
    def distinctIntegers(n):
        my_set = set()
        my_set.add(n)

        previous_len = len(my_set)
        while True:
            temp = []
            for n in my_set:
                for i in range(1,n):
                    if n % i == 1:
                        temp.append(i)

            my_set.update(temp)

            if len(my_set) == previous_len:
                break
            
            previous_len = len(my_set)

        return len(my_set)

if True:
    def distinctIntegers(n):
        return n - 1 if n > 1 else 1

print(f"{distinctIntegers(caseN_1)}")
print(f"{distinctIntegers(caseN_2)}")