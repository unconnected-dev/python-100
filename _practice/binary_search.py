
if True:
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