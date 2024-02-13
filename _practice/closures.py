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

#Multiplier function
if False:
    def multiplier(m):
        mult = m
        def by(n):
            nonlocal mult
            return mult * n
        return by
    
    double = multiplier(2)
    print(f"{double(5)}")
    triple = multiplier(3)
    print(f"{triple(5)}")

#Password generator
if False:
    import random
    def password_generator():
        chars = "abcdefghijklmnopqrstuvwxyz"
        def gen(n):
            nonlocal chars
            password = [random.choice(chars) for i in range(n)]
            return ''.join(password)
        return gen
    
    generate_password = password_generator()
    print(generate_password(5))
    print(generate_password(10))


