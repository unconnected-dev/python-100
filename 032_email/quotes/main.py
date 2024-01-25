import random
import datetime as dt
import smtplib
#https://docs.python.org/3/library/smtplib.html


def emailQuote():
    relative_quotes_path = "./032_email/quotes/quotes.txt"
    with open(relative_quotes_path) as quotes_file:
        quotes = quotes_file.readlines()
        quote = random.choice(quotes)


    test_email = "***@***.***"
    test_password = "******"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        #transport layer security
        connection.starttls()

        connection.login(user=test_email, password=test_password)
        connection.sendmail(from_addr=test_email, to_addrs=test_email, msg=f"Subject:Quote for today\n\n{quote}")


current_time = dt.datetime.now()
current_day = current_time.weekday()
if current_day == 0:
    emailQuote()