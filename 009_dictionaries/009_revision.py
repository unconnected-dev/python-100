#Basic Dictionaries
print("Basic Dictionaries")

#Basic dictionary
if False:
    aDict = {
        "name": "Morgan",
        "age": 86
    }

    #Adding to dictionary
    aDict["Height"] = 1.88

    #Iterating over a dictionary
    for key in aDict:
        print(f"{key}: {aDict[key]}")

#Nesting list into dictionary
if False:
    countryCities = {
        "Japan": ["Tokyo", "Kyoto", "Osaka"],
        "China": ["Hangzhou", "Harbin"],
        "aNumber": 5
    }

    #Iterating through the list
    for key in countryCities:
        if isinstance(countryCities[key], list):
            print(f"-{key}-")
            for city in countryCities[key]:
                print(f"{city}")

#Nesting dictionary in dictionary
if False:
    countryCities = {
        "Japan": {"cities": ["Tokyo", "Kyoto", "Osaka"]},
        "China": {"cities": ["Hangzhou", "Harbin"]},
        "aNumber": 5
    }

    #Iterating through
    for key in countryCities:
        if isinstance(countryCities[key], dict):
            print(f"-{key}-")
            for city in countryCities[key]["cities"]:
                print(f"{city}")


#Nesting dictionary in a list
if False:
    aList = [
        {
            "country": "Japan",
            "cities": ["Tokyo", "Kyoto", "Osaka"]
        },
        {
            "country": "China",
            "cities": ["Hangzhou", "Harbin"]
        }
    ]

    #Iterating through
    for entry in aList:
        print(f"-{entry['country']}-")
        for city in entry["cities"]:
            print(f"{city}")


#Default values
if True:
    myDict = {}

    for _ in range(10):
        myDict[_] = f"{_}..."
    
    for i in range(-5, 5):
        print(f"{myDict.get(i, f'{i} Not found')}")
