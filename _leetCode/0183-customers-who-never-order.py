#Customers Who Never Order
#https://leetcode.com/problems/customers-who-never-order/description/
import pandas

customersData = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max']
}

customersDataFrame = pandas.DataFrame(customersData)

ordersData = {
    'id': [1, 2],
    'customerId': [3, 1]
}

ordersDataFrame = pandas.DataFrame(ordersData)

if True:
    def find_customers(customers: pandas.DataFrame, orders: pandas.DataFrame) -> pandas.DataFrame:
        #~ negates the condition
        return customers[~customers['id'].isin(orders['customerId'])][['name']].rename(columns={'name': 'Customers'})
    
print(f"{find_customers(customersDataFrame, ordersDataFrame)}")