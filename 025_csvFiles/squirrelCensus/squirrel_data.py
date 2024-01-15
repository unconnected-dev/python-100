import pandas

relative_path_name = "./025_csvFiles/squirrelCensus/squirrel_data.csv"
with open(relative_path_name) as squirrel_data_file:
    
    squirrel_data = pandas.read_csv(squirrel_data_file)
    gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
    cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
    black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
    
    # print(f"Gray: {gray_squirrels_count}")
    # print(f"Cinnamon: {cinnamon_squirrels_count}")
    # print(f"Black: {black_squirrels_count}")

    squirrel_dict = {
        "Fur Color":["Gray","Cinnamon","Black"],
        "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
    }

    new_data = pandas.DataFrame(squirrel_dict)
    new_data.to_csv("./025_csvFiles/squirrelCensus/squirrel_count_data.csv")