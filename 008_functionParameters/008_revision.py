#Basic Function Parameters
print("......................................................................")
print("Basic Functions Parameters")

regArr = [0, 1, 5, 7, 0, 8]
noZeroArray = [1, 2, 3, 7, 4, 5]
multipleStartZeroArray = [0, 0, 0, 1, 2, 3]

#0, 1, 5, 7, 0, 8

#left = 0
#right = 1
#1, 0a, 5, 7, 0b, 8

#left = 1
#right = 2
#1, 5, 0a, 7, 0b, 8

#left = 2
#right = 3
#1, 5, 7, 0a, 0b, 8

#left = 3
#right = 4
#1, 5, 7, 0a, 0b, 8

#left = 3
#right = 5
#1, 5, 7, 8, 0b, 0a
def moveZeroesV1(array):
    left = 0
    right = 0

    while(right < len(array)):
        if array[right] != 0:
            #shift the right values to the left
            #left pointer sticks onto a 0 until it can be swapped
            array[left], array[right] = array[right], array[left]
            left+=1
            
        right+=1

    print(f"{array}")


def moveZeroesV2(array):
    #z is the left pointer equivalent
    z = 0

    for i in range(len(array)):
        if array[i] != 0:
            array[z], array[i] = array[i], array[z]
            z+=1

    print(f"{array}")

if False:
    moveZeroesV1(regArr)
    moveZeroesV1(noZeroArray)
    moveZeroesV1(multipleStartZeroArray)

if True:
    moveZeroesV2(regArr)
    moveZeroesV2(noZeroArray)
    moveZeroesV2(multipleStartZeroArray)

print("-End of script-")