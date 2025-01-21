import smtplib    
import datetime as dt 
import random

# tapping into the todays day of week
now = dt.datetime.now()
day_of_week = now.weekday()


# checking if its monday
if day_of_week == 5:
    
    # making list of quotes.txt and tapping into random quote
    with open("./Day-032/monday-motivation-project/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        all_quotes_striped = [line.strip() for line in all_quotes]
        quote_of_the_day = random.choice(all_quotes_striped)

    # sending mail 
    my_email = "bromineopxd@gmail.com"
    my_password = "dovdxxeaavavlehf"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="brominexd02@gmail.com", 
                            msg=f"Subject:Monday Motivational\n\n{quote_of_the_day}")

