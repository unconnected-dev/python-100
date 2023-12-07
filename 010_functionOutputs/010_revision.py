#Basic Function Outputs
print("......................................................................")
print("Basic Function Outputs")

#Return tuple
if False:
    def myTuple():
        return "aString", 20

    s, i = myTuple()
    print(f"{s}")
    print(f"{i}")

#Return list
if False:
    def myList():
        return [1,2,3,4]

    #use * for the remaining values
    a,b,*c = myList()

    print(f"{a}")
    print(f"{b}")
    print(f"{c}")

#Return dictionary
if False:
    def myDict():
        d = dict()
        d["a"] = 1
        d["b"] = 2
        d["c"] = 3
        d["d"] = 4
        return d

    a,b,*c = myDict()
    d = myDict()
    
    print(f"{a}")
    print(f"{b}")
    print(f"{c}")
    print(f"{d}")
    

print("-End of script-")