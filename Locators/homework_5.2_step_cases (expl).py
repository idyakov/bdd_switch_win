from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.wait = WebDriverWait(driver, timeout=10)

# open the url
driver.get('https://www.yep.com/')
#driver.get('https://www.target.com/')
# populate search field
search = driver.find_element(By.XPATH, "//input[@type='search']")
search.clear()
search.send_keys('Mail')
#
# # wait for 4 sec
# sleep(4)
driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
# click search button
#driver.find_element(By.XPATH, "//button[@type='submit']").click()

# verify search results
assert 'mail' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()

#Test passed by Ilya on 03.18.24
#
#hw5