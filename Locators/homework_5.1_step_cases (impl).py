from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCarWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButtonOrTextIdFor15280655']")
xpath = "//div[@class='styles__ThreeUpButtonWrapper-sc-11rka0i-0 gfFifD']//button[text()='Add to cart']"
ADD_TO_CART_BTN_POPUP = (By.XPATH, xpath)
loupe_xpath = "//button[@type='submit']"
PRESS_LOUPE = (By.XPATH, loupe_xpath)
WEB_LINK = "https://www.target.com/cart"
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
CROSS_CLOSE_POPUP = (By.XPATH, "//button[contains(@class, 'styles__StyledButton-sc-18jd2v4')]")
DISCOUNT_LIST = (By.XPATH,'//div[@data-component-id="WEB-397697"] //a[@data-test="@web/slingshot-components/CellsComponent/Link"]')

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
#implicit
driver.implicitly_wait(4) #up to 4 sec
# explicit
wait = WebDriverWait(driver, 10)  # Example: 10 seconds timeout
#driver.wait = WebDriverWait(driver, timeout=10)
driver.get('https://www.target.com/l/target-circle/-/N-pzno9')

#Scenarion_1
expected = 6
deals = driver.find_elements(By.XPATH,'//div[@data-component-id="WEB-397697"] //a[@data-test="@web/slingshot-components/CellsComponent/Link"]')
numbers = int(len(deals))
assert expected == numbers
print(f'Expected deals {expected}, got {numbers}. Gongrats! ')

#Scenarion_2
driver.get(WEB_LINK)
driver.find_element(By.ID, 'search').send_keys('car')  # item search
wait.until(EC.element_to_be_clickable(PRESS_LOUPE)).click()  # Press the loop
sleep(5) # I left sleep function here, because without it, it's failed, even if I do implicit wait. I think the Target has this issue.
wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN)).click()  # press the button add to cart
wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN_POPUP)).click()
driver.get('https://www.target.com/cart')
text1 = driver.find_element(By.CSS_SELECTOR, "div[class='styles__StyledHeading-sc-1ge2jts-1 bmsjWz']").text
print(f'The price is {text1} including the taxes and the shipping')

#Scenarion_3
driver.get('https://help.target.com/help')
driver.find_element(By.CSS_SELECTOR, "h2[class='custom-h2']") #Test Target help header
driver.find_element(By.ID, 'j_id0:j_id2:j_id32:name') #Test Target search panel
driver.find_element(By.CSS_SELECTOR, "input[class='btn-sm search-btn']") #Test Target search loop icon
driver.find_element(By.CSS_SELECTOR, "div[class='container clearfix']") #Test Target action steps to do
driver.find_element(By.CSS_SELECTOR, "div[class='salesforceBox txtAC bigbox1']") #Test Target Manage my lines
driver.find_element(By.CSS_SELECTOR, "div[class='grid_4 boxSmallr txtAC bigbox2']") #Test Target Contact us
driver.find_element(By.XPATH, "//h2[text()='Browse all Help pages']") #Test Target Browse all help pages
print("All buttons of the Target pages - passed, within Implicit wait option")

#hw5