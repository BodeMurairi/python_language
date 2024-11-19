from selenium import webdriver
from selenium.webdriver.common.by import By

#........................ set up Selenium................ 
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


#.............................Finding elements
#title = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[1]/div/h2').text 

events_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
event_dictionary = {}

for n in range(len(events_time)):
    event_dictionary[n]:{
        "time": events_time[n].text,
        "name": event_names[n].text
        }

print(event_dictionary)


driver.quit()