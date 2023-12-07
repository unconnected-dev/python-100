#Basic Dictionaries
print("......................................................................")
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

print("-End of script-")