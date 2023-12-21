#Destination City
#https://leetcode.com/problems/destination-city/description/

casePaths_1 = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
casePaths_2 = [["B","C"],["D","B"],["C","A"]]
casePaths_3 = [["A","Z"]]

if True:
    def destinationCity(paths) -> str:
        myDict = dict()

        for path in paths:
            myDict[path[0]] = path[1]

        destination = ""
        goto = paths[0][0]
    
        while destination == "":
            if goto in myDict:
                goto = myDict[goto]
            else:
                destination = goto
        
        return goto

    print(f"{destinationCity(casePaths_1)}")
    print(f"{destinationCity(casePaths_2)}")
    print(f"{destinationCity(casePaths_3)}")