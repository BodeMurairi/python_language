from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#keep chrome opened after code successfully runned



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
#article_count.click()

#all_portals = driver.find_element(By.LINK_TEXT, value="Pages")
#all_portals.click()
search = driver.find_element(By.XPATH, value='//*[@id="searchform"]/div/div/div[1]/input')
#sending keys to the selenium
search.send_keys("Python Programming", Keys.ENTER)