#Declare data type
age: int
name: str
height: float
is_human: bool

def police_check(age: int) -> bool:
    if age > 18:
        return True
    else:
        return False

if police_check(19):
    print("pass")
else:
    print("fail")