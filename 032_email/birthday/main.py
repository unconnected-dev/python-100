import smtplib
#https://docs.python.org/3/library/smtplib.html

relative_quotes_path = "./032_email/birthday/quotes.txt"

test_email = "***@***.***"
test_password = "******"

with smtplib.SMTP("smtp.gmail.com") as connection:
    #transport layer security
    connection.starttls()

    connection.login(user=test_email, password=test_password)
    connection.sendmail(from_addr=test_email, to_addrs=test_email, msg="Subject:Hello\n\nThe body text goes here")