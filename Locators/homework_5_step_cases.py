from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, timeout=15)
driver.get('https://www.target.com/l/target-circle/-/N-pzno9')

expected = 6
deals = driver.find_elements(By.XPATH,'//div[@data-component-id="WEB-397697"] //a[@data-test="@web/slingshot-components/CellsComponent/Link"]')
numbers = int(len(deals))
assert expected == numbers
print(f'Expected deals {expected}, got {numbers}. Gongrats! ')
sleep(3)



driver.get('https://www.target.com/')

driver.find_element(By.ID, 'search').send_keys('russian hat')  # item search

driver.find_element(By.XPATH, "//button[@type='submit']").click()  # prees the loop
sleep(5)
driver.find_element(By.XPATH, "//button[@id='addToCartButtonOrTextIdFor15280655']").click()  # press the button add to cart
sleep(8)
driver.find_element(By.XPATH, "//div[@class='styles__ThreeUpButtonWrapper-sc-11rka0i-0 gfFifD']//button[text()='Add to cart']").click() #press add to cart right menu
sleep(8)
driver.find_element(By.XPATH, "//div[@class='h-margin-t-default']//button[text()='Decline coverage']").click()
sleep(8)
driver.find_element(By.CSS_SELECTOR, "a[href='/cart?prehydrateClick=true']").click()
sleep(5)


text1 = driver.find_element(By.CSS_SELECTOR, "p[class='styles__StyledP-sc-5wqnp5-0 eXiTaW h-text-bold h-text-lg h-text-md']").text
print(f'The price is {text1} including the taxes and the shipping')
sleep(7)

driver.get('https://help.target.com/help')

driver.find_element(By.CSS_SELECTOR, "h2[class='custom-h2']")
print("Target help header - passed")
driver.find_element(By.ID, 'j_id0:j_id2:j_id32:name')
print("Target search panel - passed")
driver.find_element(By.CSS_SELECTOR, "input[class='btn-sm search-btn']")
print("Target search loop icon - passed")
driver.find_element(By.CSS_SELECTOR, "div[class='container clearfix']")
print("Target action steps to do - passed")
driver.find_element(By.CSS_SELECTOR, "div[class='salesforceBox txtAC bigbox1']")
print("Target Manage my lines - passed")
driver.find_element(By.CSS_SELECTOR, "div[class='grid_4 boxSmallr txtAC bigbox2']")
print("Target Contact us - passed")
driver.find_element(By.XPATH, "//h2[text()='Browse all Help pages']")
print("Target Browse all help pages - passed")
sleep(5)
