#Reshape Data: Melt
#https://leetcode.com/problems/reshape-data-melt/description/
import pandas

caseData = {
    "product": ["Umbrella", "SleepingBag"],
    "quarter_1": [417, 800],
    "quarter_2": [224, 936],
    "quarter_3": [379, 93],
    "quarter_4": [611, 875]
}

caseDataFrame = pandas.DataFrame(caseData)

if True:
    def meltTable(report):
        report = pandas.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')
        return report
    
print(f"{meltTable(caseDataFrame).to_markdown(index=False)}")