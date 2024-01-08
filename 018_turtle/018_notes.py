#Regular Import
if False:
    from turtle import Turtle, Screen

    turtleObj = Turtle()

    screen = Screen()
    screen.exitonclick()

#Import All
#Avoid using
if False:
    from turtle import * 

    turtleObj = Turtle()
    
#ALias
if False:
    import turtle as t

    turtleObj = t.Turtle()

#Tuples
a_tuple = (5, 10, 15)
print(f"{a_tuple[1]}")

#You cannot change a tuple
#Immutable
# a_tuple[2] = 0