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

driver.find_element(By.ID, 'search').send_keys('russian hat') #item search
sleep(2)
driver.find_element(By.XPATH, "//button[@type='submit']").click() #prees the loop
sleep(5)
driver.find_element(By.XPATH, "//button[@id='addToCartButtonOrTextIdFor88282075']").click() #press the button add to cart
sleep(8)
driver.find_element(By.XPATH, "//div[@class='ReactModal__Content ReactModal__Content--after-open styles__StyledReactModal-sc-10966vp-0 cfemXU']//button[text()='Add to cart']").click()
sleep(8)
driver.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()
sleep(5)
item = driver.find_element(By.CSS_SELECTOR, "div[data-test='cartItem-title']").text
print(f'Here is your item - {item}. Go ahead, American boy, wear it and meet a winter time.')
sleep(3)
text1 = driver.find_element(By.CSS_SELECTOR, "div[class='styles__StyledHeading-sc-1ge2jts-1 bmsjWz']").text
print(f'The total price {text1} including the taxes and the shipping ')
sleep(10)