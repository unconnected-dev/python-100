
#Average Height
if False:
    input = "151 145 179"
    studentHeights = input.split(" ")

    totalHeight = 0

    for height in studentHeights:
        totalHeight += int(height)

    averageHeight = totalHeight / len(studentHeights)

    print(f"The average height is: {round(averageHeight, 2)}")


#High Score
if False:
    input = "78 65 89 86 55 91 64 89"
    studentScores = input.split(" ")

    highScore = 0

    for score in studentScores:
        if int(score) > highScore:
            highScore = int(score)

    print(f"The highest score in the class is: {highScore}")


#Add All Even Numbers
if False:
    max = int(input("What do you want to count to?\n"))
    buildStr = ""
    total = 0

    # for i in range(1, max + 1):
        # if i % 2 == 0:
    for i in range(2, max + 1, 2):
        buildStr += f"{i} + "
        total += i

    buildStr = buildStr[:-2]
    print(buildStr)
    print(f"The total is: {total}")


#FizzBuzz
if False:
    target = 100
    for i in range(1, target + 1):
        response = ""
        if i % 3 == 0:
            response += "Fizz"
        if i % 5 == 0:
            response += "Buzz"

        if response != "":
            print(response)
        else:
            print(f"{i}")    
