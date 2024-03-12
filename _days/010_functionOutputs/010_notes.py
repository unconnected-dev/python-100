
#Return
if False:
    def myFunction():
        return 3 * 2

    print(myFunction())


#Multiple Returns
if False:
    def anotherFunction(arg):
        #Early break
        if(type(arg) != int):
            return 
        
        if(arg == 1):
            return True
        
        return False

    print(f"{anotherFunction(2)} is the number check line")
    print(f"{anotherFunction('')} should be empty")


#Format Name
#Docstrings
if False:
    def formatName(firstName, lastName):
        """Take a first and last name and format it to 
        return capitalized version of the name combined"""
        return f"{firstName.capitalize()} {lastName.capitalize()}"

    print(formatName("paul", "BENNETT"))