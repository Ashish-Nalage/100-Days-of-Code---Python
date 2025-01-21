##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_day = now.day
current_month = now.month

df = pandas.read_csv("./Day-032/birthday-wisher-project/birthdays.csv")

matching_row = df[(df.month == current_month) & (df.day == current_day)] # fillterout the row if month and day matches

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if not matching_row.empty:
    name = matching_row.name.item()
    email = matching_row.email.item()
    letter_no = random.randint(1,3)

    with open(f"./Day-032/birthday-wisher-project/letter-templates/letter_{letter_no}.txt", mode="r") as letter_file:
        letter_content = letter_file.read()
        final_letter = letter_content.replace("[NAME]", name)

# 4. Send the letter generated in step 3 to that person's email address.
    my_email = "bromineopxd@gmail.com"
    my_password = "dovdxxeaavavlehf"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(to_addrs=email, 
                            from_addr=my_email, 
                            msg=f"Subject:Happy Birthday\n\n{final_letter}")







