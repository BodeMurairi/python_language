import smtplib
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
from dotenv import load_dotenv
import os
import lxml

load_dotenv()

url = "https://www.amazon.com/s?k=Instant+Pot+Duo+Plus+9-in-1+Electric+Pressure+Cooker%2C+Slow+Cooker%2C+Rice+Cooker%2C+Steamer%2C+Saut%C3%A9%2C+Yogurt+Maker%2C+Warmer+%26+Sterilizer%2C+Includes+App+With+Over+800+Recipes%2C+Stainless+Steel%2C+3+Quart&crid=GEV8P8W311DD&sprefix=instant+pot+duo+plus+9-in-1+electric+pressure+cooker%2C+slow+cooker%2C+rice+cooker%2C+steamer%2C+saut%C3%A9%2C+yogurt+maker%2C+warmer+%26+sterilizer%2C+includes+app+with+over+800+recipes%2C+stainless+steel%2C+3+quart%2Caps%2C575&ref=nb_sb_noss"

headers = {
    "User-Agent": os.environ["user_Agent"],
    "Accept-Language": os.environ["accept_Language"]
}


response = requests.get(url, headers=headers)
website_price = response.text
soup = BeautifulSoup(website_price, "lxml")
#print(soup.prettify())
element_price = soup.find(class_= "a-offscreen").getText()
print(element_price)
price = float(element_price.split("$")[1])
print(price)
#...............................SEND EMAIL........................
buy_price = 100
email_address = os.environ["email_adress"]
email_password = os.environ["email_password"]
if price <= buy_price:
    message = f"Your violin is on sale for {price}$"
    
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(email_address, email_password)
        connection.sendmail(
            from_addr=email_address,
            to_addrs=os.environ["to_address"],
            msg=f"Subject:Amazon Price Alert!\n\n {message}\n{url}".encode("utf-8")
        )
    