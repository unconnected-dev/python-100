#Basic Inheritance

#General convention
#Single underscore '_' is considered protected 
#Double underscore '__' is considered private

class BaseClass:
    def __init__(self) -> None:
        self.class_name = "Base"

    def action(self) -> None:
        print(f"Base Action")

    def print_name(self) -> None:
        print(f"{self.class_name}")


class ExtendedClass(BaseClass):
    def __init__(self) -> None:
        super().__init__()
        self.class_name = "Extended"

    def action(self) -> None:
        super().action()
        print(f"Extended Action")
    
    
# extended = ExtendedClass()
# extended.action()
        
#Slicing
#This also works with tuples
k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(k[2:])#Start from point
print(k[1:8:2])#Increase increments
print(k[::-1])#Reverse iterating