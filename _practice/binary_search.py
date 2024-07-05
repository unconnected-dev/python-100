#Basic binary search
if False:
    def a_search(n, nums):
        print(f"nums: {nums}")        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == n:
                return mid
            elif nums[mid] > n:
                right = mid - 1
            else:
                left = mid + 1

        return f"{n} not in {nums}"


    case_nums_1 = [n for n in range(4, 21)]
    case_n_1 = 15

    case_nums_2 = [n for n in range(5,19)]
    case_n_2 = 15
    print(f"{a_search(case_n_1, case_nums_1)}")
    print(f"{a_search(case_n_2, case_nums_2)}")
    
#Last occurence
if True:
    def find_last_occurrence(arr, target):
        left, right = 0, len(arr) - 1
        res = -1
        
        while left <= right:
            mid = (left + right) //2
            if arr[mid] == target:
                res = mid
                left = mid + 1  #move to the right to find the last occurence
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return res
    
    arr = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7]
    target = 5
    print(f"{find_last_occurrence(arr, target)}")