#Various nesting within dictionaries

#Nesting list into dictionary
if False:
    country_cities = {
        "Japan": ["Tokyo", "Kyoto", "Osaka"],
        # "China": ["Harbin", "Shanghai"],
        "error": 5
    }

    #Iterating through
    #country is the key
    for country in country_cities:
        #Confirm the key is associated with a list
        if isinstance(country_cities[country], list):
            #List all cities available
            print(f"Unsorted...")
            for city in country_cities[country]:
                print(f"{city}")

            #Sort the list
            country_cities[country].sort()
            print(f"Sorted...")
            for city in country_cities[country]:
                print(f"{city}")

#Nesting dictionary into dictionary
if False:
    country_cities = {
        "Japan": {"cities": ["Tokyo", "Kyoto", "Osaka"]},
        # "China": {"cities": ["Hangzhou", "Harbin"]},
        "error": 5
    }

    #Iterating through
    #country is the key
    for country in country_cities:
        #Confirm the key is associated with a dictionary
        if isinstance(country_cities[country], dict):
            #List all cities available
            print(f"Unsorted...")
            for city in country_cities[country]["cities"]:
                print(f"{city}")

            #Sort the list        
            country_cities[country]["cities"].sort()
            print(f"Sorted...")
            for city in country_cities[country]["cities"]:
                print(f"{city}")

#Nesting dictionary into list
if False:
    countries_list = [
        {
            "country_name": "Japan",
            "city_names": ["Tokyo", "Kyoto", "Osaka"]
        },
        {
            "country_name": "China",
            "city_names": ["Hangzhou", "Harbin"]
        }
    ]

    for country in countries_list:
        print(f'{country["country_name"]}')
        country["city_names"].sort()
        for city in country["city_names"]:
            print(f"{city}")

        print(f"")