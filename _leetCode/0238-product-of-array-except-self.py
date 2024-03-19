#Product Of Array Except Self
#https://leetcode.com/problems/product-of-array-except-self/description/

caseNums_1 = [1,2,3,4]
caseNums_2 = [-1,1,0,-3,3]
caseNums_3 = [0,0]

if True:
    def productExceptSelf(nums):
        
        run = 1
        pre_ = []
        post_ = []
        res = []

        for i in range(len(nums)):
            run *= nums[i]
            pre_.append(run)

        run = 1
        for i in range(len(nums)-1,-1,-1):
            run *= nums[i]
            post_.append(run)
        post_ = post_[::-1]

        for i in range(len(nums)):
            a = pre_[i-1] if (i-1) >= 0 else 1
            b = post_[i+1] if len(post_) > (i+1) else 1
            res.append(a * b)
        
        return res

print(f"{productExceptSelf(caseNums_1)}")
print(f"{productExceptSelf(caseNums_2)}")
print(f"{productExceptSelf(caseNums_3)}")