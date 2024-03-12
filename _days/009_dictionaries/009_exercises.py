
#Student Scores
if False:
    studentScores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62
    }

    studentGrades = {}

    for studentName in studentScores:
        score = studentScores[studentName]

        if score >= 91 and score <= 100:
            studentGrades[studentName] = "Outstanding"
        elif score >= 81 and score <= 90:
            studentGrades[studentName] = "Exceeds Expectations"
        elif score >= 71 and score <= 80:
            studentGrades[studentName] = "Acceptable"
        elif score <= 70:
            studentGrades[studentName] = "Fail"
        
    for studentName in studentGrades:
        print(f"{studentName} : {studentGrades[studentName]}")


#Adding Dictionary to List
if False:
    country = input("Add a country name\n")
    visits = int(input("Number of visits\n"))
    listOfCities = eval(input("Create list from formatted string\n"))

    travelLog = [
        {
            "country": "France",
            "visits": 12,
            "cities": ["Paris", "Lille", "Dijon"]
        },
        {
            "country": "Germany",
            "visits": 5,
            "cities": ["Berlin", "Hamburg", "Stuttgart"]
        }
    ]

    def addNewCountry(countryName, visitedTimes, listCities):
        newCountry = {}
        newCountry["country"] = countryName
        newCountry["visits"] = visitedTimes
        newCountry["cities"] = listCities

        travelLog.append(newCountry)


    addNewCountry(country, visits, listOfCities)
    print(f"I've been to {travelLog[2]['country']} {travelLog[2]['visits'] } times")
    print(f"My favorite city was {travelLog[2]['cities'][0]}")