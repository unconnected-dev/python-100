#Richest Customer Wealth
#https://leetcode.com/problems/richest-customer-wealth/description/

caseAccounts_1 = [[1,2,3],[3,2,1]]
caseAccounts_2 = [[1,5],[7,3],[3,5]]
caseAccounts_3 = [[2,8,7],[7,1,3],[1,9,5]]

if False:
    def richestCustomerWealth(accounts) -> int:
        greatestWealth = 0

        for account in accounts:
            accountTotal = sum(account)

            if accountTotal > greatestWealth:
                greatestWealth = accountTotal

        return greatestWealth    

if False:
    def richestCustomerWealth(accounts) -> int:
        most = 0
        for account in accounts:
            current = sum(account)
            most = max(most, current)

        return most

if True:
    def richestCustomerWealth(accounts) -> int:
        res = [0] * len(accounts)
        for i in range(len(accounts)):
            res[i] = sum(accounts[i])
        
        return max(res)

print(f"{richestCustomerWealth(caseAccounts_1)}")
print(f"{richestCustomerWealth(caseAccounts_2)}")
print(f"{richestCustomerWealth(caseAccounts_3)}")