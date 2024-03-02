#Average Selling Price
#https://leetcode.com/problems/average-selling-price/description/
import pandas

price_data = {
    'product_id': [1, 1, 2, 2],
    'start_date': ['2019-02-17', '2019-03-01', '2019-02-01', '2019-02-21'],
    'end_date': ['2019-02-28', '2019-03-22', '2019-02-20', '2019-03-31'],
    'price': [5, 20, 15, 30]
}
price_data_frame = pandas.DataFrame(price_data)

product_data = {
    'product_id': [1, 1, 2, 2],
    'purchase_date': ['2019-02-25', '2019-03-01', '2019-02-10', '2019-03-22'],
    'units': [100, 15, 200, 30]
}
product_data_frame = pandas.DataFrame(product_data)

if True:
    def average_selling_price(prices, units_sold):
        merged_ = units_sold.merge(prices, on='product_id', how='left')
        merged_['matching'] = (merged_['purchase_date'] >= merged_['start_date']) & (merged_['purchase_date'] <= merged_['end_date'])
        merged_ = merged_[merged_['matching'] == True]
        merged_['total_spent'] = merged_['units'] * merged_['price']
        merged_ = merged_.groupby('product_id').agg(total_spent=('total_spent',lambda x: sum(x)),total_units=('units',lambda x: sum(x))).reset_index()
        merged_['average_price'] = round(merged_['total_spent'] / merged_['total_units'],2)

        prices = pandas.DataFrame(columns=['product_id'], data=prices['product_id'].unique())
        return prices.merge(merged_[['product_id','average_price']],on='product_id', how='left').fillna(0)

print(f"{average_selling_price(price_data_frame, product_data_frame)}")