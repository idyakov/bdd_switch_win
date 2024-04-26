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
driver.implicitly_wait(4) #up to 4 sec

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
WEB_LINK = "https://www.target.com"
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
CROSS_CLOSE_POPUP = (By.XPATH, "//button[contains(@class, 'styles__StyledButton-sc-18jd2v4')]")
DISCOUNT_LIST = (By.XPATH,'//div[@data-component-id="WEB-397697"] //a[@data-test="@web/slingshot-components/CellsComponent/Link"]')


driver.get(WEB_LINK)
driver.find_element(By.ID, 'search').send_keys('tea')  # item search
driver.find_element(By.XPATH, "//button[@type='submit']").click()  # prees the loop
text1 = driver.find_element(By.XPATH, "//a[contains(text(), 'Tazo Passion Herbal Tea - 20ct')]").text  # find the tea string
image1 = driver.find_element(By.XPATH, "//picture/img[@src='https://target.scene7.com/is/image/Target/GUEST_54b6a436-136a-4028-b366-957d14facc5a?qlt=65&fmt=webp&hei=350&wid=350']")
print(f'the icon 1 with text - {text1} has the image')
text2 = driver.find_element(By.XPATH, "//a[contains(text(), 'Tazo Organic Peachy Green Tea - 20ct')]").text  # find the tea string
image2 = driver.find_element(By.XPATH, "//picture/img[@src='https://target.scene7.com/is/image/Target/GUEST_d106451b-c51f-4247-8aa2-4fcbe2cbf55d?qlt=65&fmt=webp&hei=350&wid=350']")
print(f'the icon 2 with text - {text2} has the image')
text3 = driver.find_element(By.XPATH, "//a[contains(text(), 'Pukka Selection Box - 45ct')]").text  # find the tea string
image3 = driver.find_element(By.XPATH, "//picture/img[@src='https://target.scene7.com/is/image/Target/GUEST_e6b25cf3-7b1c-4704-92cb-57772dae43b5?qlt=65&fmt=webp&hei=350&wid=350']")
print(f'the icon 3 with text - {text3} has the image')
print('passed')

#hw5


print_items_name = driver.find_element(By.XPATH, "//a[@data-test='product-title']").text
print(print_items_name)
print_items_img = driver.find_element(By.XPATH, "//div[contains(@class, 'ProductCardImage__PicturePrimary-sc-1y6rvoy-0 gXpSlS')]")
print(print_items_img)

for print_item in print_items_name:
    print(f'text: {print_item}')