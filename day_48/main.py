from selenium import webdriver
from selenium.webdriver.common.by import By
#keep chrome opened after code successfully runned
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org")
#product_price = driver.find_element(By.CLASS_NAME, value="a-color-base")
#product_price_cent = driver.find_element(By.CLASS_NAME,value="a-letter-space")
#print(f"The price is {product_price.text}.{product_price_cent.text}$")
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(button.text)
driver.quit()