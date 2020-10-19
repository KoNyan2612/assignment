from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#PATH = "/home/samson/Downloads/geckodriver"
driver = webdriver.Firefox(
    executable_path="/home/samson/Downloads/geckodriver")

driver.get("http://172.17.0.2")
print(driver.title)

search = driver.find_element_by_id("About Us")
search.send_keys(Keys.RETURN)

driver.get("http://172.17.0.2/content/about-us.php")

about = driver.find_element_by_id("PID-ab2-pg")
i = "This is about page."
if i in about.text:
    print(True)

time.sleep(2)

driver.quit()
