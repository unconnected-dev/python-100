from datetime import datetime
import pandas

#Get today
current_time = datetime.now()
today = (current_time.month, current_time.day)

#Check today against birthdays
relative_dates_path = "./032_email/birthday/birthdays.csv"
birthday_data = pandas.read_csv(relative_dates_path)
birthdays_dict = {(data_row.month, data_row.day): data_row for index, data_row in birthday_data.iterrows()}

if today in birthdays_dict:
    print("yes")
else:
    print("no")


# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.




relative_letters_path = "./032_email/birthday/letter_templates"