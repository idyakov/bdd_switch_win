from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Start Chrome browser:
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

# Open target.com and verify “Your cart is empty”
driver.get('https://www.target.com/')
#cart press button
driver.find_element(By.XPATH, "//div[@class='styles__CartIconDiv-sc-jff2tp-1 bECXM']").click()

expected = 'Your cart is empty'
text = driver.find_element(By.CSS_SELECTOR, "h1[class*='styles__StyledHeading-sc-1xmf98v-0 lfA-Dem']").text
# print(f'The text "{text}" shown in the page (locator_search by class) ')
assert expected == text, f'Expected text {expected}, got {text}'
driver.quit()
print("the verification of the element in the code has been successful.")

# Open target.com and verify “Your cart is empty”