#Counter
if False:
    def countFunc():
        c = 0
        def increment():
            nonlocal c
            c += 1
            return c
        
        return increment
    
    count_var = countFunc()
    print(f"{count_var()}")
    print(f"{count_var()}")
    print(f"{count_var()}")

#Average calculator
if False:
    def calcFunc():
        count = 0
        total = 0
        def average_calculator(n):
            nonlocal count
            nonlocal total
            count += 1
            total += n
            return total/count
        return average_calculator
    
    avg = calcFunc()
    print(avg(10))
    print(avg(20))