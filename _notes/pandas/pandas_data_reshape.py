import pandas

#Data: Pivot
if False:
    exampleData = {
        'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'],
        'month': ['January', 'February', 'March', 'April', 'May', 'January', 'February', 'March', 'April', 'May'],
        'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
    }

    #The pivot function in Pandas is used to reshape data by pivoting the rows
    #to columns, essentially creating a new DataFrame with a different structure

    #It reshapes the DataFrame based on the values of specified columns
    #One is the index, another to become new columns and a third to populate
    #the values in the cells

    #If there are duplicate entries for the same combination of index and column
    #values, you can specify how to aggregate those values. By default Pandas
    #will raise an error if there are duplicates, unless you provide an aggregation
    #function using the `aggfunc` parameter

    #Pandas will automatically fill missing values with NaN if the combination
    #of index and column doesn't exist in the original DataFrame
    df = pandas.DataFrame(exampleData)
    print(f"Before pivot...")
    print(df)

    df = df.pivot(index="month", columns="city", values="temperature")
    print(f"After pivot...")
    print(df)
    
if False:
    exampleData = {
                    'A': ['foo', 'foo', 'bar', 'bar'],
                    'B': ['one', 'two', 'one', 'two'],
                    'C': [1, 2, 3, 4]
                }
    
    df = pandas.DataFrame(exampleData)

    print(f"Before pivot...")
    print(df)

    pivot_df = df.pivot(index='A', columns='B', values='C')
    print(f"After pivot...")
    print(pivot_df)


#Data: Melt
if False:
    exampleData = {
        'product': ['Umbrella', 'SleepingBag'],
        'quarter_1': [417, 800],
        'quarter_2': [224, 936],
        'quarter_3': [379, 93],
        'quarter_4': [611, 875]
    }

    #The melt function in Pandas is used to transform or reshape a DataFrame
    #from wide format to long format. The function is particuarly useful when 
    #you have data where variables are stored in both rows and columns and you 
    #want to `melt` the DataFrame to bring one or more columns into a single
    #column while keeping other columns intact

    #You need to identify which columns you want to keep intact and which you
    #want to melt

    #You specify the columns that you want to retain as-is using the `id_vars`
    #parameter. These columns will remain in the DataFrame

    #The remaining columns are melted into a single column creating a `variable`
    #column to denote the original column name and a `value` column to contain
    #the values from the melted columns. See example 2 if this is confusing

    #The resulting DataFrame will have a row for each unique combination of the
    #columns specified by `id_vars` along with `variable` and `value` columns
    df = pandas.DataFrame(exampleData)
    print(f"Before melt")
    print(df)

    print(f"After melt")
    melt_df = pandas.melt(df, id_vars=['product'], var_name='quarter', value_name='sales')
    print(melt_df)

if False:
    exampleData = {
        'Name': ['John', 'Mary'],
        'Math': [80, 75],
        'Physics': [85, 88],
        'Chemistry': [90, 92]
        }
    
    df = pandas.DataFrame(exampleData)


    #In this example the columns `Math`, `Physics` and `Chemistry`
    #were melted into a single column `Subject` and the corresponding
    #values were placed in the `Score column`
    print(f"Before melt...")
    print(df)

    melted_df = pandas.melt(df, id_vars=['Name'], var_name='Subject', value_name='Score')
    print(f"After melt...")
    print(melted_df)


#Method Chaining
if False:
    exampleData = {
        'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
        'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
        'age': [98, 50, 6, 45, 100, 26],
        'weight': [464, 41, 328, 463, 50, 349]
    }

    df = pandas.DataFrame(exampleData)


    #Method chaining refers to the practice of applying multiple DataFrame or Series
    #methods sequentially in a single line of code, often without assigning intermediate
    #results to variables

    #Method chaining is facilitated by the fact that most Pandas methods returns a 
    #modified copy of the original DataFrame or Series rather than modifying it in place.
    #This means you can call another method immediately after the first one, and so on,
    #to create a chain of operations

    
    # animals = df[["name", "weight"]]
    # heavy_animals = animals[animals["weight"] > 100]
    # heavy_animals = heavy_animals.sort_values(by="weight", ascending=False)[["name"]]

    #Below is an example of method chaining
    heavy_animals = df[df['weight'] > 100].sort_values(['weight'], ascending=False)[['name']]

    print(f"{heavy_animals}")

if False:
    exampleData = {
                    'A': [1, 2, 3, 4, 5],
                    'B': [10, 20, 30, 40, 50],
                    'C': [100, 200, 300, 400, 500]
                }
    
    df = pandas.DataFrame(exampleData)
    print(f"Before method chain...")
    print(df)

    result = df[df['A'] > 2].sort_values(by='B').reset_index(drop=True)
    print(f"After method chain...")
    print(result)