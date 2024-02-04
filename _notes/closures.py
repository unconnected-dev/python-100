#Closures

#Basic closure
if False:
    def outer_function(x):
        def inner_function(y):
            return x + y
        return inner_function
    
    closure = outer_function(10)    #sets closure to be the inner_function with x being 10
    result = closure(5)             #calls the inner_function
    print(f"{result}")

#Data encapsulation
if False:
    #The counter increments each time it is called
    #It is not accessible from outside the function
    #It is essentially private and cannot be modified outside of the function

    def counter():
        count = 0
        def increment():
            nonlocal count
            count += 1
            return count
        return increment
    
    counter_var = counter()     #sets counter_car to be increment
    print(f"{counter_var()}")   #1
    print(f"{counter_var()}")   #2

#Function factories
if False:
    #Uses closures to create and return functions dynamically
    #Factory implies creating functions on-the-fly with specific configuration
    #Allows you to create a family of related functions with shared characteristics

    def power_of(n):
        def exponentiate(x):
            return x ** n
        return exponentiate
    
    square = power_of(2)        #sets square to be exponentiate with n being 2
    cube = power_of(3)          #sets cube to be exponentiate with n being 3

    result_square = square(4)
    result_cube = cube(4)

    print(f"result_square: {result_square}")
    print(f"result_cube: {result_cube}")

#Callbacks
if False:
    def callback_factory(prefix):
        def callback(message):
            print(f"{prefix}: {message}")

        return callback

    callback_info = callback_factory("Info")    #sets callback_info to be callback with prefix being "Info"
    callback_error = callback_factory("Error")  #sets callback_error to be callback with prefix being "Error"

    callback_info("Processing complete.")       
    callback_error("Critical error occurred.")

#Event handling system
if False:
    class EventDispatcher:
        def __init__(self) -> None:
            self._listeners = {}
        
        def add_listener(self, event_name, callback):
            if event_name not in self._listeners:
                self._listeners[event_name] = []
            self._listeners[event_name].append(callback)

        def trigger_event(self, event_name, data=None):
            if event_name in self._listeners:
                for callback in self._listeners[event_name]:
                    callback(data)

    #Define callback functions    
    def on_message_received(message):
        print(f"Message Received: {message}")

    def on_data_updated(data):
        print(f"Data Updated: {data}")

    event_dispatcher = EventDispatcher()

    #Register callbacks for specific events via event_name
    event_dispatcher.add_listener("message", on_message_received)
    event_dispatcher.add_listener("data_updated", on_data_updated)

    event_dispatcher.trigger_event("message", "Hello world")
    event_dispatcher.trigger_event("data_updated", {"temperature": 25, "humidity": 60})