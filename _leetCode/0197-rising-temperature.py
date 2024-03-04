#Rising Temperature
#https://leetcode.com/problems/rising-temperature/description/
import pandas

caseData = {
    'id': [1, 2, 3, 4],
    'recordDate': pandas.to_datetime(['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04']),
    'temperature': [10, 25, 20, 30]
}

caseDataFrame = pandas.DataFrame(caseData)

if True:
    def rising_temperature(weather):
        weather.sort_values(by='recordDate', inplace=True)

        date_diff = weather['recordDate'].diff().dt.days
        temp_diff = weather['temperature'].diff()
        
        return weather[(date_diff == 1) & (temp_diff > 0)][['id']]

print(f"{rising_temperature(caseDataFrame)}")