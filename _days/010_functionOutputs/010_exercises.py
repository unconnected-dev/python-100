
#How Many Days
if False: 
#Required for February
    def isLeapYear(year):
        leapYear = False

        if year % 4 == 0:
            if year % 100 != 0:
                leapYear = True
            elif year % 400 == 0:
                leapYear = True

        return leapYear
        

    def daysInMonth(year, month):
        monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        days = monthDays[month - 1]

        if(month == 2 and isLeapYear(year)):
            return 29
        else:
            return days


    inputYear = int(input("Please enter a year\n"))
    inputMonth = int(input("Please enter a month\n"))

    if inputMonth >= 1 and inputMonth <= 12:
        days = daysInMonth(inputYear, inputMonth)
        print(days)
    
    else:
        print("Invalid month")
        
