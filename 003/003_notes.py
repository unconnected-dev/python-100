
if False:
    print("Welcome to the rollercoaster")
    height = int(input("What is your height in cm?\n"))

    if height >= 120:
        print("You can ride the rollercoaster")
        age = int(input("What is your age?\n"))

        bill = 0
        if age < 12:
            print("Child tickets are $5")
            bill += 5
        elif age <= 18:
            print("Youth tickets are $7")
            bill += 7
        elif age >= 45 and age <= 55:
            print("Have a free ride on us")
        else:
            print("Adult tickets are $12")
            bill += 12

        photoRequested = input("Do you want a photo taken? Y/N\n")
        if photoRequested == "Y" or photoRequested == "y":
            bill += 3
        
        print(f"Please pay ${bill}")

    else:
        print("You can't ride the rollercoaster")


