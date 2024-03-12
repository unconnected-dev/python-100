
#Scope
#Local scope will override global scope
#Variables outside functions can be accessed inside but can't be reassigned
if False:
    enemies = 1

    def increaseEnemies():
        enemies = 2
        print(f"enemies inside: {enemies}")

    increaseEnemies()
    print(f"enemies outside: {enemies}")


#Local Scope
if False:
    def drinkPotion():
        potionStrength = 2
        print(potionStrength)
    
    drink()
    print(potionStrength)


#Global Scope
#Gist is be aware of namespace
if False:
    playerHealth = 10

    def drinkPotion():
        potionStrength = 2
        print(playerHealth)
    
    drinkPotion()

#No Block Scope
#If, while, for can't contain a variable
#Only a new function applies the local scope
if False:
    gameLevel = 3
    enemies = ["Skeleton", "Zombie", "Alien"]
    if gameLevel < 5:
        newEnemy = enemies[0]

    print(newEnemy)

    def newEnemyFunc():
        aNewEnemy = "Monster"
    
    #This cannot access within the above function
    # print(aNewEnemy)


#Allowing Global Scope
#Don't try to modify global scope
if False:
    enemies = "Skeleton"

    def newEnemy():
        #This is a bad idea
        global enemies 
        enemies = "Zombie"
        print(f"The enemy is a {enemies}")
    
    newEnemy()
    print(f"The enemy is a {enemies}")

    #This is a better way
    def newEnemyAssign():
        return "Monster"
    
    enemies = newEnemyAssign()
    print(f"The enemy is a {enemies}")


#Global Constants
#Upper case the variable with _
PI = 3.14159
URL = "http://google.com"