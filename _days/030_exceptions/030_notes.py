#Exceptions

#Different errors
#File not found
# with open("a_file.txt") as file:
#     file.read()

#Key error
# a_dict = {"key":"value"}
# value = a_dict["nokey"]

#Index error
# fruit_list = ["apple", "berry"]
# fruit = fruit_list[3]

#Type error
# text = "abc"
# print(text + 5)


if False:
    relative_file_path = "./030_exceptions/data.txt"
    try: 
        file = open(relative_file_path)
        
        # a_dict = {"key" : "value"}
        # value = a_dict["nokey"]
        
    #You should not use bare except clauses as they look to catch any error
    # except:
    except FileNotFoundError:
        print("Exception fired")
        file = open(relative_file_path, "w")#creates an empty file
    except KeyError as error_message:
        print("There was a key error")
        print(f"{error_message} does not exist")
        
    #In case there were no errors
    else:
        content = file.read()
        print(content)
    #Runs no matter what
    finally:
        file.close()
        print("File was closed")
        
#Raising errors
# raise KeyError("This is a custom error message")
        
if False:
    height = 5
    weight = 65
    
    if height > 3:
        raise ValueError("People aren't usually over 3 meters")
    
    bmi = weight / height ** 2
    print(f"BMI: {bmi}")

