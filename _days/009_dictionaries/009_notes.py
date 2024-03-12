
#Dictionary
if False:
    programmingDictionary = {
        "Bug": "An error in a program that prevents the program from running as expected.",
        "Function": "A piece of code that you can easily call over and over again.",
    }

    #Adding to dictionary
    programmingDictionary["Loop"] = "The action of doing something over and over again."
    print(programmingDictionary["Loop"])

    #Edit dictionary
    programmingDictionary["Loop"] = "Loop has been edited"
    print(programmingDictionary["Loop"])

    #Create an empty dictionary
    # emptyDictionary = {}

    #Wipe dictionary
    # programmingDictionary = {}
    # print(programmingDictionary)

    
    #Loop through dictionary
    for key in programmingDictionary:
        print(programmingDictionary[key])


#Nesting
if False:
    capitals = {
        "France": "Paris",
        "Germany": "Berlin"
    }

    travelLog = {
        "France": ["Paris", "Lille", "Dijon"],
        "Germany": ["Berlin", "Hamburg", "Stuttgart"]
    }


#Nesting Dictionary in a Dictionary
if False:
    citiesVisited = {
        "France": {"citiesVisited": ["Paris", "Lille", "Dijon"], "totalVisits": 12},
        "Germany": {"citiesVisited": ["Berlin", "Hamburg", "Stuttgart"], "totalVisits": 6}
    }

    print(citiesVisited["France"]["totalVisits"])


#Nesting Dictionary in a List
if False:
    dictionaryList = [
        {
            "country":"France", 
            "citiesVisited": ["Paris", "Lille", "Dijon"], 
            "totalVisits": 12
        },
        {
            "country":"Germany", 
            "citiesVisited": ["Berlin", "Hamburg", "Stuttgart"], 
            "totalVisits": 6
        }
    ]

    for entry in dictionaryList:
        print(entry["country"])