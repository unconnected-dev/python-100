#Classes

#Instance and class variables
if False:
    class MyClass:
        shared_variable = "this is shared among instances"      #Shared among all instances and will be the same
                                                                #They are static
        def __init__(self, instance_variable) -> None:
            self.instance_variable = instance_variable          #Instance specific
    
    a_class = MyClass(1)
    b_class = MyClass(2)

    print(f"{a_class.shared_variable}")
    print(f"{a_class.instance_variable}")
    print(f"{b_class.shared_variable}")
    print(f"{b_class.instance_variable}")


#Inheritance
if False:
    class MyBaseClass:
        def __init__(self, instance_variable) -> None:
            self.instance_variable = instance_variable

        def __init_subclass__(cls) -> None:                     #Method to define in parent class
            print(f"Subclassing {cls}")                         #that is called when a child class is created
            
        def a_method(self):
            print(f"Base class method")

        def get_instance_variable(self):
            return self.instance_variable
        
    class ExtendedBaseClass(MyBaseClass):
        def __init__(self, instance_variable) -> None:
            super().__init__(instance_variable)
        
        def a_method(self):
            print(f"Extended class method")
            super().a_method()

    a_class = ExtendedBaseClass("word")
    a_class.a_method()
    var_ = a_class.get_instance_variable()
    print(f"{var_}")

#Private variables in classes
if False:
    class Person:
        def __init__(self, name, age) -> None:
            #Single underscore indicates protected
            #Double underscore indicates private
            #But python doesn't have actual private like other languages
            self.__name = name
            self.__age = age

        def get_details(self):
            return f"{self.__name}, {self.__age}"
        
        def set_age(self, new_age):
            self.__age = new_age if new_age > 0 else self.__age

            if new_age <= 0:
                print(f"Value: {new_age} is not valid")
        
        def _protected_method(self):
            print(f"This is a protected method")

        def __private_method(self):
            print(f"This is a private method")

    person = Person("Bob", 22)
    # details = person.get_details()
    # print(f"{details}")

    person._protected_method()
    # person.__private_method()   #Gives an attribute error


    #Accessing privates
    #It is possible to access private variables using name mangling
    #_classname__variable
    #This is bad practice
    # print(person.__name)        #Gives an attribute error
    # print(person._Person__name) #Output: "Bob"

#Polymorphism
if False:
    class Shape:
        def area(self):
            pass

    class Circle(Shape):
        def area(self, radius):
            return 3.14 * radius**2

    class Square(Shape):
        def area(self, side):
            return side**2

    a_circle = Circle()
    print(f"{a_circle.area(5)}")

    a_square = Square()
    print(f"{a_square.area(5)}")

#Static methods
if False:
    #Can be used for functions related to the class but not tied specifically to instance data
    #Can help with readability grouping related functions within the class 
    class Logger():
        log_entries = []

        #Need to add the decorator over the method
        @staticmethod
        def log(message):
            Logger.log_entries.append(message)

        @staticmethod
        def get_log():
            for log in Logger.log_entries:
                print(log)

    a_logger = Logger()
    b_logger = Logger()

    a_logger.log("test message")
    b_logger.get_log()

#Property decorators
if False:
    #Allows you to implement getter, setter and delete methods
    class MyClass:
        def __init__(self) -> None:
            self._my_attribute = 0

        @property
        def my_property(self):
            return self._my_attribute

        @my_property.setter
        def my_property(self, value):
            self._my_attribute = value

        @my_property.deleter
        def my_property(self):
            del self._my_attribute
    
    obj1 = MyClass()
    obj2 = MyClass()

    obj1.my_property = 42                       #Calls the setter
    print(obj1.my_property)                     #Calls the property (getter)
    print(obj2.my_property)         
    del obj1.my_property                        #Calls the deleter