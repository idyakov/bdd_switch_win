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
WEB_LINK = "https://www.target.com/p/A-91511634?preselect=91511683"
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
CROSS_CLOSE_POPUP = (By.XPATH, "//button[contains(@class, 'styles__StyledButton-sc-18jd2v4')]")
DISCOUNT_LIST = (By.XPATH,'//div[@data-component-id="WEB-397697"] //a[@data-test="@web/slingshot-components/CellsComponent/Link"]')
COLOR_OPTIONS = (By.CSS_SELECTOR, "div[class*='styles__ButtonWrapper-sc'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapper']")


# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
#implicit
driver.implicitly_wait(4) #up to 4 sec
# explicit
wait = WebDriverWait(driver, 10)  # Example: 10 seconds timeout
#driver.wait = WebDriverWait(driver, timeout=10)

#Scenarion_1
# driver.get(WEB_LINK)
#
# expected_color = ['dark khaki', 'black/gum', 'stone/grey', 'white/gum']
# actual_color = []
# colors = driver.find_elements(By.CSS_SELECTOR, "div[class*='styles__ButtonWrapper-sc'] img")
# for color in colors:
#     color.click()
#     WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located(
#             SELECTED_COLOR
#     ))
#     # Retrieve the text of the selected color and process it
#     selected_color = driver.find_element(By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapper']").text
#     print('Current ', selected_color)
#     processed_color = selected_color.split('\n')[1]  # Assume the second line is the color text
#     actual_color.append(processed_color.strip())  # Strip to clean up any extra whitespace
#
#
# assert expected_color == actual_color, f'Expected {expected_color}, got {actual_color}'
#
# print('The test case works correctly')
#hw5


def verify_product_name_img(context):
    top_products = context.find_elements(*LISTINGS)[:4]

    for product in top_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)
