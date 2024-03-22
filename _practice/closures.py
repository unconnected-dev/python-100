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
if False:
    def greet(name):
        print(f"Hello {name}")

    def function_logger(f):
        def my_func(*args):
            print(f"Calling function {f.__name__}: {args}")
            return f(*args)
        
        return my_func

    log_greet = function_logger(greet)#greet is the function
    log_greet('Alice')

#Timer
if False:
    import time 

    def timer(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Function '{func.__name__}' took {end_time - start_time} seconds to complete.")
            return result
        return wrapper
    
    def example_function(n):
        total = 0
        for i in range(n):
            total += i
        return total
    
    example = timer(example_function)

    result = example(100000)
    print(f"result: {result}")

#Fibonacci
if False:
    def fibonacci():
        a = 0
        b = 1
        def wrapper():
            nonlocal a
            nonlocal b

            t = a + b
            a = b
            b = t
            return t
        return wrapper

    fib = fibonacci()
    for _ in range(10):
        print(f"{fib()}")

if False:
    def fibonacci():
        a, b = 0, 1
        def wrapper():
            nonlocal a, b
            a, b = b, a + b
            return b
        return wrapper

    fib = fibonacci()
    for _ in range(10):
        print(f"{fib()}")

#Prime number checker
if False:
    def primeNumberCheck():
        def wrapper(n):
            for i in range((n//2) + 1):
                if i > 1 and n % i == 0:
                    return False
            return True
        return wrapper
    
    is_prime = primeNumberCheck()

    print(f"{is_prime(1)}")
    print(f"{is_prime(2)}")
    print(f"{is_prime(4)}")
    print(f"{is_prime(5)}")
    print(f"{is_prime(19)}")
    print(f"{is_prime(20)}")
    print(f"{is_prime(21)}")

#Add 5
if False:
    def add_value(v):
        def wrapper(n):
            return v + n
        return wrapper
    
    add_10_to = add_value(10)
    add_7_to = add_value(7)

    print(f"{add_10_to(5)}")
    print(f"{add_7_to(5)}")

#How many times has it been called
if False:
    def call_me():
        times_called = 0
        def wrapper():
            nonlocal times_called
            times_called += 1
            return times_called
        return wrapper
    
    call_ = call_me()

    print(f"{call_()}")
    print(f"{call_()}")
    print(f"{call_()}")

#Greater than threshold
if False:
    def greater_than(v):
        def wrapper(n):
            return n > v
        
        return wrapper
    
    greater_than_10 = greater_than(10)

    print(f"{greater_than_10(5)}")
    print(f"{greater_than_10(11)}")

#Exponential
if False:
    def exponential_of(v):
        def wrapper(n):
            return v ** n
        
        return wrapper
    
    exponential_of_5 = exponential_of(5)
    exponential_of_10 = exponential_of(10)

    print(f"{exponential_of_5(3)}")
    print(f"{exponential_of_10(3)}")

#Time to execute
if False:
    import time

    def timer_to_execute(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            print(f"Time to execute: {end_time - start_time}")
            return result
        return wrapper
    
    def some_function():
        time.sleep(2)
        return "Done"
    
    check_time = timer_to_execute(some_function)

    print(f"{check_time()}")

#Unique id
if False:
    def id_generator(start_id):
        current_id = start_id

        def inner_function():
            nonlocal current_id
            current_id += 1

            return current_id
        
        return inner_function
    
    gen = id_generator(100)

    print(f"{gen()}")
    print(f"{gen()}")
    print(f"{gen()}")

#Cache with max size
if False:
    def cache(max_size):
        cache_dict = {}

        def inner_function(key, value=None):
            if value is None:
                return cache_dict.get(key)
            
            if len(cache_dict) >= max_size:
                cache_dict.popitem()
            cache_dict[key] = value
            return value

        return inner_function
    
    a_cache = cache(2)

    a_cache("a", 1)
    a_cache("b", 2)
    # print(f"{a_cache("a")}")

    #a will remain cached as we are popping
    a_cache("c", 3)
    a_cache("d", 4)
    
    # print(f"{a_cache("c")}")

#Count every call
if False:
    def count_me():
        c = 0
        
        def inner_function():
            nonlocal c
            c+=1
            return c
        
        return inner_function

    count_ = count_me()
    print(f"{count_()}")
    print(f"{count_()}")
    print(f"{count_()}")

#Counter
if False:
    def counter_():
        c = 0

        def inner_function():
            nonlocal c
            c += 1
            return c

        return inner_function

    count_this = counter_()
    print(f"{count_this()}") 
    print(f"{count_this()}") 
    print(f"{count_this()}") 

#Fibonacci
if False:
    def fib():
        a,b = 0,1

        def inner_function():
            nonlocal a,b
            a,b = b,b+a
            return b
        
        return inner_function
    
    call_me = fib()
    for _ in range(10):
        print(f"{call_me()}")

#Average calculator
if False:
    def average_calculator():
        called, total = 0, 0

        def inner_function(num):
            nonlocal called, total
            called += 1
            total += num
            return total/called
        
        return inner_function
    
    avg = average_calculator()
    print(f"{avg(50)}")
    print(f"{avg(150)}")

#Multiplier function
if False:
    def multiplier_function(n):
        by = n

        def inner_function(num):
            nonlocal by
            return num * by
        
        return inner_function
    
    mult_by_2 = multiplier_function(2)
    mult_by_5 = multiplier_function(5)

    print(f"{mult_by_2(10)}")
    print(f"{mult_by_5(10)}")

#Power of
if False:
    def power_function(p):
        power_of = p

        def inner_function(num):
            nonlocal power_of
            return num ** power_of
        
        return inner_function
    
    power_of_2 = power_function(2)
    power_of_5 = power_function(5)

    print(f"{power_of_2(4)}")
    print(f"{power_of_5(4)}")