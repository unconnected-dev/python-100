#Fill Missing Data
#https://leetcode.com/problems/fill-missing-data/description/
import pandas

caseData = {
    "name": ["Wristwatch", "WirelessEarbuds", "GolfClubs", "Printer"],
    "quantity": [None, None, 779, 849],
    "price": [135, 821, 9319, 3051]
}

caseDataFrame = pandas.DataFrame(caseData)

if True:
    def fillMissingValues(products):
        products["quantity"] = products["quantity"].fillna(0)
        return products
    
print(f"{fillMissingValues(caseDataFrame)}")