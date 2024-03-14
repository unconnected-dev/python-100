#Find Customer Referee
#https://leetcode.com/problems/find-customer-referee/description/
import pandas

caseData = {
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['Will', 'Jane', 'Alex', 'Bill', 'Zack', 'Mark'],
    'referee_id': [None, None, 2, None, 1, 2]
}

caseDataFrame = pandas.DataFrame(caseData)

if False:
    def find_customer_referee(customer):
        names = customer.loc[(customer['referee_id'] != 2) | (customer['referee_id'].isna()), ['name']]
        return names

if True:
    def find_customer_referee(customer):
        return customer[(customer['referee_id'] != 2) | (customer['referee_id'].isna())][['name']]

print(f"{find_customer_referee(caseDataFrame).to_markdown(index=False)}")