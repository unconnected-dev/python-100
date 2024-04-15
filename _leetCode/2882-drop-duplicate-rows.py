#Drop Duplicate Rows
#https://leetcode.com/problems/drop-duplicate-rows/description/
import pandas

caseData = {
    "customer_id": [1, 2, 3, 4, 5, 6],
    "name": ["Ella", "David", "Zachary", "Alice", "Finn", "Violet"],
    "email": ["emily@example.com", "michael@example.com", "sarah@example.com", "john@example.com", "john@example.com", "alice@example.com"]
}

caseDataFrame = pandas.DataFrame(caseData)

if False:
    def dropDuplicateEmails(customers):
        #keep, will keep the first occurence
        #inplace, will modify the selected DataFrame rather than returning a new copy 
        customers.drop_duplicates(subset=["email"], keep="first", inplace=True)
        return customers

if False:
    def dropDuplicateEmails(customers):
        result = customers.drop_duplicates(subset='email', keep='first')
        return result

if True:
    def dropDuplicateEmails(customers):
        customers.drop_duplicates(subset='email', inplace=True)
        return customers

print(f"{dropDuplicateEmails(caseDataFrame).to_markdown(index=False)}")