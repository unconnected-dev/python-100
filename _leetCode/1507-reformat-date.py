#Reformat Date
#https://leetcode.com/problems/reformat-date/description/

caseDate_1 = "20th Oct 2052"
caseDate_2 = "6th Jun 1933"
caseDate_3 = "26th May 1960"

if False:
    def reformatDate(date):
        month_dict = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }

        date_split = date.split()

        day_number = date_split[0][:-2]
        if int(day_number) < 10:
            day_number = "0" + day_number

        month = month_dict[date_split[1]]
        year = date_split[2]
        result = "" 
        result += year + "-" 
        result += month + "-"
        result += day_number
        return result
    

if True:
        def reformatDate(date):
            month_dict = {
                "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
            }

            date_split = date.split()

            day_number = date_split[0][:-2]
            if int(day_number) < 10:
                day_number = "0" + day_number

            return f"{date_split[2]}-{month_dict[date_split[1]]}-{day_number}"

print(f"{reformatDate(caseDate_1)}")
print(f"{reformatDate(caseDate_2)}")
print(f"{reformatDate(caseDate_3)}")