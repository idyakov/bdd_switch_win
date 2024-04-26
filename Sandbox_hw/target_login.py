from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
print("Test case - open the Target web page - passed")

# Click search btn
driver.find_element(By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()
print("Test case - button SignIn is shown - passed")
sleep(2)
driver.find_element(By.XPATH, "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl']").click()
print("Test case - click popup button SignIn - passed")
sleep(1)
driver.find_element(By.XPATH, "//input[@autocomplete='username webauthn']")

driver.find_element(By.XPATH, "//div[@class='styles__InputWrapper-sc-17c8y80-0 bUAMkG styles__AuthInput-sc-q9vn5-0 eeoYPi']")

driver.find_element(By.ID, 'username').send_keys('dyak.ilya@gmail.com')
print("Test case - type your username - passed")
sleep(1)
driver.find_element(By.XPATH, "//input[@autocomplete='current-password']").send_keys('password_here')

text = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
print(f'The text {text} shown in the page ')
print("Test case - type your username - passed")
print('Locators are built correctly and point to the correct webelements')
print('Test case runs and works correctly')
