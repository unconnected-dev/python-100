#Day Of The Week
#https://leetcode.com/problems/day-of-the-week/description/
from datetime import datetime

caseDay_1 = 31
caseMonth_1 = 8
caseYear_1 = 2019

caseDay_2 = 18
caseMonth_2 = 7
caseYear_2 = 1999

caseDay_3 = 15
caseMonth_3 = 8
caseYear_3 = 1993

if True:
    def dayOfTheWeek(day, month, year):
        date_ = datetime(year, month, day)
        return date_.strftime("%A")

print(f"{dayOfTheWeek(caseDay_1, caseMonth_1, caseYear_1)}")
print(f"{dayOfTheWeek(caseDay_2, caseMonth_2, caseYear_2)}")
print(f"{dayOfTheWeek(caseDay_3, caseMonth_3, caseYear_3)}")