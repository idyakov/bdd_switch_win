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

#Search by ID
driver.find_element(By.ID, )

#Search by Xpath
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")


#by multiple attributes
# Formula in the console > $x("//input[@placeholder='Search Amazon' and @type='text' and @name='field-keywords']")
driver.find_element(By.XPATH,"//input[@placeholder='Search Amazon' and @type='text' and @name='field-keywords']")


driver.find_element(By.XPATH, "//input[@class='nav-search-label nav-progressive-content']")


# search by text and attributes
#by text $x("//a[text()='Best Sellers']") code in Chrome
driver.find_element(By.XPATH, "//a[@class='nav-a ' and text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[@text()='Best Sellers']")

driver.find_element(By.XPATH, "//select[contains(@class, 'seach-dropdown')]")