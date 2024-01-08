#Draw Square
if False:
    from turtle import Turtle, Screen

    turtleObj = Turtle()
    turtleObj.shape("triangle")
    turtleObj.color("black")

    for i in range(4):
        turtleObj.forward(100)
        turtleObj.right(90)

    screen = Screen()
    screen.exitonclick()


#Dashed Line
if False:
    from turtle import Turtle, Screen

    turtleObj = Turtle()
    turtleObj.shape("triangle")
    turtleObj.color("black")
    
    #Draw Dashed Square
    for i in range(4):
        for i in range(5):
            turtleObj.forward(10)
            turtleObj.penup()
            turtleObj.forward(10)
            turtleObj.pendown()

        turtleObj.right(90)

    screen = Screen()
    screen.exitonclick()


#Draw All Shapes From Triangle to Decagon
if False:
    from turtle import Turtle, Screen
    from random import randint

    turtleObj = Turtle()
    turtleObj.shape("triangle")
    turtleObj.color("black")

    for j in range(3, 11):
        ang = 360 / j

        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
        turtleObj.color(hex_color)

        for i in range(j):
            turtleObj.forward(50)
            turtleObj.right(ang)
    
    screen = Screen()
    screen.exitonclick()


#Random Walk
if False:
    import random
    from random import randint
    from turtle import Turtle, Screen

    def randomColor() -> str:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)

        return hex_color

    def randomDir() -> int:
        directions = [0, 90, 180, 270]
        return random.choice(directions)

    turtleObj = Turtle()
    turtleObj.shape("triangle")
    turtleObj.color("black")

    for i in range(50):
        turtleObj.forward(30)
        turtleObj.setheading(randomDir())
        turtleObj.color(randomColor())

    screen = Screen()
    screen.exitonclick()


#Spirograph
if True:    
    import turtle as t
    from turtle import Turtle, Screen
    import random
    from random import randint

    def randomColor() -> str:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        
        return (r, g, b)

    t.colormode(255)

    turtleObj = Turtle()
    turtleObj.shape("triangle")
    turtleObj.color(randomColor())
    turtleObj.speed(0)
    
    num_of_circles = 30
    for i in range(num_of_circles):
        turtleObj.setheading(turtleObj.heading() + 360/num_of_circles)
        turtleObj.circle(100)
        turtleObj.color(randomColor())

    screen = Screen()
    screen.exitonclick()