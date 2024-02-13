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

#Multiplier withs state
if False:
    def multiplier_with_state(n):
        total = 0
        # mult = n
        
        def multiply(m):
            nonlocal total
            t = n * m
            total += t
            return t

        def get_total():
            return total
        
        return multiply, get_total
    
    multiply, get_total = multiplier_with_state(2)
    print(multiply(3))
    print(multiply(4))
    print(multiply(5))
    print(get_total())

#Memorization
if False:
    def memorize():
        myDict = dict()

        def add(a, b):
            if f'{a}_{b}' in myDict:
                return myDict.get(f'{a}_{b}')
            else:
                t = a + b
                myDict[f'{a}_{b}'] = t
                return t
        return add
    
    memorize_add = memorize()
    print(memorize_add(1,2))
    print(memorize_add(1,2))

if False:
    def add(a,b):
        return a + b
    
    def memorize(f):
        myDict = dict()

        def my_func(a,b):
            if f'{a}_{b}' in myDict:
                return myDict.get(f'{a}_{b}')
            else:
                t = f(a,b)
                myDict[f'{a}_{b}'] = t
                return t

        return my_func
    
    memorize_add = memorize(add)
    print(memorize_add(1,2))
    print(memorize_add(1,2))

#Function logger
if True:
    def greet(name):
        print(f"Hello {name}")

    def function_logger(f):
        def my_func(*args):
            print(f"Calling function {f.__name__}: {args}")
            return f(*args)
        
        return my_func

    log_greet = function_logger(greet)#greet is the function
    log_greet('Alice')