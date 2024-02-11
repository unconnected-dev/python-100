#Decorators
#A decorator is a function that takes another function as it's argument
#and returns a new function (the wrapper) that adds behavior
#before and after the original function is called

#Basic decorator
if False:
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    @my_decorator           #say_hello = my_decorator(say_hello)
    def say_hello():
        print("Hello!")

    say_hello()             #when say_hello is called, the wrapper function is invoked

#Logging
if False:
    #Decorators can log information about function calls
    def log_function_call(func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned {result}")
            return result
        return wrapper

    @log_function_call
    def add(a, b):
        return a + b

    add(3, b=4)

#Timing
if False:
    #Decorators can measure the time taken by a function to execute
    import time
    def timeit(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} took {end_time - start_time:.2f} seconds to run")
            return result
        return wrapper

    @timeit
    def slow_function():
        time.sleep(2)

    slow_function()

#Memorization/Caching
if True:
    #Decorators can cache function results to avoid redundant computations
    def memoize(func):
        cache = {}

        def wrapper(*args):
            if args not in cache:
                cache[args] = func(*args)
            
            print(f"current cache: {cache}")
            return cache[args]

        return wrapper

    @memoize
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    print(fibonacci(5))