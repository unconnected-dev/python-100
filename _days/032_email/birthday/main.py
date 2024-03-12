from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "***@***.***"
MY_PASSWORD = "******"

#Get today
current_time = datetime.now()
today = (current_time.month, current_time.day)

#Check today against birthdays
relative_dates_path = "./032_email/birthday/birthdays.csv"
birthday_data = pandas.read_csv(relative_dates_path)
birthdays_dict = {(data_row.month, data_row.day): data_row for index, data_row in birthday_data.iterrows()}


if today in birthdays_dict:
    #Pick a random letter
    relative_letters_path = f"./032_email/birthday/letter_templates/letter_{random.randint(1, 3)}.txt"
    
    #Replace the text in the letter
    with open(relative_letters_path, "r") as letter_file:
        letter_contents = letter_file.read()
        persons_name = birthdays_dict[today]["name"]
        letter_contents= letter_contents.replace("[NAME]", persons_name)
        print(letter_contents)

    # with smtplib.SMTP("smpt.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(MY_EMAIL, MY_PASSWORD)
    #     connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Happy Birthday\n\n{letter_contents}")
else:
    print("Not today...")