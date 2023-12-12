#Richest Customer Wealth
#https://leetcode.com/problems/richest-customer-wealth/description/

caseAccounts_1 = [[1,2,3],[3,2,1]]
caseAccounts_2 = [[1,5],[7,3],[3,5]]
caseAccounts_3 = [[2,8,7],[7,1,3],[1,9,5]]

if True:
    def richestCustomerWealth(accounts):
        greatestWealth = 0

        for account in accounts:
            accountTotal = sum(account)

            if accountTotal > greatestWealth:
                greatestWealth = accountTotal

        return greatestWealth    

    print(f"{richestCustomerWealth(caseAccounts_1)}")
    print(f"{richestCustomerWealth(caseAccounts_2)}")
    print(f"{richestCustomerWealth(caseAccounts_3)}")