#Recyclable And Low Far Products
#https://leetcode.com/problems/recyclable-and-low-fat-products/description/
import pandas

caseData = {
    'product_id': [0, 1, 2, 3, 4],
    'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
    'recyclable': ['N', 'Y', 'Y', 'Y', 'N']
}

caseDataFrame = pandas.DataFrame(caseData)

if False:
    def find_products(products: pandas.DataFrame) -> pandas.DataFrame:
        return products.loc[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y'),['product_id']]

if True:
    def find_products(products: pandas.DataFrame) -> pandas.DataFrame:
        result = products.loc[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
        return result[['product_id']]

print(f"{find_products(caseDataFrame)}")
