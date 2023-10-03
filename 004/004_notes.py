import random

if False:
    randomInteger = random.randint(0, 10)
    print(randomInteger)

    randomFloat = random.random()
    print(randomFloat)


#Lists
if False:
    statesOfAmerica = ["Delaware", "Pennsylvania", "New Jersey"]
    print(statesOfAmerica[1])

    print(statesOfAmerica[-1])#Last item in list
    print(statesOfAmerica[-2])

    statesOfAmerica.append("Georgia")
    print(statesOfAmerica)

    #Out of range error
    # print(statesOfAmerica[len(statesOfAmerica)])


#Lists in Lists
if False:
    dirtyDozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

    fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
    vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
    dirtyDozen = [fruits, vegetables]
    print(dirtyDozen)