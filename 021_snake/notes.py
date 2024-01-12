#Basic Inheritance

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
    
    
extended = ExtendedClass()
extended.action()