#Reshape Data: Pivot
#https://leetcode.com/problems/reshape-data-pivot/description/
import pandas

caseData = {
    "city": ["Jacksonville", "Jacksonville", "Jacksonville", "Jacksonville", "Jacksonville", "ElPaso", "ElPaso", "ElPaso", "ElPaso", "ElPaso"],
    "month": ["January", "February", "March", "April", "May", "January", "February", "March", "April", "May"],
    "temperature": [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
}

caseDataFrame = pandas.DataFrame(caseData)

if True:
    def pivotTable(weather):
        weather = weather.pivot(index="month", columns="city", values="temperature")
        return weather
    
print(f"{pivotTable(caseDataFrame).to_markdown(index=False)}")