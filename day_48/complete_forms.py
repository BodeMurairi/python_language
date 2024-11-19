from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#keep chrome opened after code successfully runned



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.XPATH, value='/html/body/form/input[1]')
first_name.send_keys("Bode", Keys.ENTER)
last_name = driver.find_element(By.XPATH, value='/html/body/form/input[2]')
last_name.send_keys("Murairi", Keys.ENTER)
email_address = driver.find_element(By.XPATH, value='/html/body/form/input[3]')
email_address.send_keys("bodemurairi2@gmail.com", Keys.ENTER)
submit_button = driver.find_element(By.XPATH, value='/html/body/form/button')
submit_button.click()