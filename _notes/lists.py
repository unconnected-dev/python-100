#Lists
import random
import copy

#Referencing elements in the list
if False:
    nums = []
    for i in range(11):
        nums.append(i)
    
    print(f"nums : {nums}")
    print(f"{nums[-1]}")                                                        #last item in list
    print(f"{nums[-2]}")

#Remove elements from a list
if False:
    nums = []
    for i in range(11):
        nums.append(i)
    
    print(f"nums: {nums}")
    
    #Remove will remove the first instance of a specific value for the list
    #If value is not present it raises a ValueError
    nums.remove(5)
    print(f"nums after remove: {nums}")

    #Pop will remove and return the element at a specific index
    #If no index is given it does the last element of the list
    #If index is out of range it raises an IndexError
    nums.pop(5)
    print(f"nums after pop: {nums}")

#Iterating over list
if False:
    nums = []
    for i in range(11):
        nums.append(random.randint(0,100))

    # for num in nums:
    #     print(f"{num}")

    # for i in range(len(nums)):
    #     print(f"{nums[i]}")

    for i, val in enumerate(nums):
        print(f"i: {i}, val: {val}")

#Finding index of an element
if False:
    my_list = [10, 20, 30, 40, 50]
    index_of_30 = my_list.index(30)
    print(f"list: {my_list}")
    print(f"index: {index_of_30}")

#List slicing
if False:
    nums = []
    for i in range(11):
        nums.append(random.randint(0,100))

    sliced_list = nums[1:4]                                                     #4 will include up to index 3
    print(f"nums: {nums}")                                                      #due to exclusive indexing
    print(f"sliced_list: {sliced_list}")

#Comprehension list and spread operator
if False:
    nums1 = []
    nums2 = []
    for i in range(11):
        nums1.append(random.randint(0, 100))    
        nums2.append(random.randint(0, 100))
    
    combined_nums = nums1 + nums2
    print(f"combined_nums: {combined_nums}")

    nested_nums = [nums1, nums2]                                                #this puts two lists into another list
    print(f"nested_nums: {nested_nums}")

    nums_comprehension_list = [num for nums in nested_nums for num in nums]     #using a comprehension list to put list elements
    print(f"nums_comprehension_list: {nums_comprehension_list}")                #into a single list

    nums_spread = [*nums1, *nums2]                                              # * is spread operator
    print(f"nums_spreadL: {nums_spread}")                                       #output is the same as the comprehension list

#Shallow copy lists
if False:
    original_list = [[1, 2, 3], [4, 5, 6]]
    shallow_copied_list = copy.copy(original_list)

    shallow_copied_list[0][0] = 100

    #Both the original and the shallow copy are affected
    print(original_list)        #Output: [[100, 2, 3], [4, 5, 6]]
    print(shallow_copied_list)  #Output: [[100, 2, 3], [4, 5, 6]]

#Deep copy lists
if False:
    original_list = [[1, 2, 3], [4, 5, 6]]
    deep_copied_list = copy.deepcopy(original_list)

    deep_copied_list[0][0] = 100

    #Only the deep copy is affected, the original remains unchanged
    print(original_list)      #Output: [[1, 2, 3], [4, 5, 6]]
    print(deep_copied_list)   #Output: [[100, 2, 3], [4, 5, 6]]