#Product Sales Analysis I
#https://leetcode.com/problems/product-sales-analysis-i/description/
import pandas

sales_data = {
    'sale_id': [1, 2, 7],
    'product_id': [100, 100, 200],
    'year': [2008, 2009, 2011],
    'quantity': [10, 12, 15],
    'price': [5000, 5000, 9000]
}
sales_dataframe = pandas.DataFrame(sales_data)

product_data = {
    'product_id': [100, 200, 300],
    'product_name': ['Nokia', 'Apple', 'Samsung']
}
product_dataframe = pandas.DataFrame(product_data)

if True:
    def sales_analysis(sales, product):
        merged_ = sales.merge(product, on='product_id', how='left')
        return merged_[['product_name','year','price']]

print(f"{sales_analysis(sales_dataframe, product_dataframe)}")