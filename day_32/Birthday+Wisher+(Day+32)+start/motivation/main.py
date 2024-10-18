import datetime as dt
import smtplib
import random
open_file = open("/home/bode/Documents/python_langage/day_32/Birthday+Wisher+(Day+32)+start/Birthday Wisher (Day 32) start/quotes.txt")
file_data = open_file.readlines()
current_day = dt.datetime.today().weekday()

week_days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}
day_choosen = week_days[current_day]
my_email = "bodemurairi2@gmail.com"
password = "jhgxuxvcfgemsewq"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password=password)
    connection.sendmail(from_addr= my_email,
                    to_addrs="dmurairimukongya@gmail.com",
                    msg = f"Subject:{day_choosen} motivation\n\n {random.choice(file_data)}")
