#Customer Who Visited But Did Not Make Any Transactions
#https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/
import pandas

visits_data = {
    'visit_id': [1, 2, 4, 5, 6, 7, 8],
    'customer_id': [23, 9, 30, 54, 96, 54, 54]
}
visits_dataframe = pandas.DataFrame(visits_data)

transactions_data = {
    'transaction_id': [2, 3, 9, 12, 13],
    'visit_id': [5, 5, 5, 1, 2],
    'amount': [310, 300, 200, 910, 970]
}
transactions_dataframe = pandas.DataFrame(transactions_data)

if True:
    def find_customers(visits, transactions):
        merge_ = visits.merge(transactions, on='visit_id', how='left')
        merge_ = merge_.loc[merge_['transaction_id'].isna()]

        return merge_.groupby('customer_id', as_index=False).agg(count_no_trans=('visit_id','nunique'))

print(f"{find_customers(visits_dataframe, transactions_dataframe)}")