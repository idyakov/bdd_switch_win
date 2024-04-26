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
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Ftag%3Damazusnavi-20%26hvadid%3D675149238451%26hvpos%3D%26hvnetw%3Dg%26hvrand%3D3490614523007615849%26hvpone%3D%26hvptwo%3D%26hvqmt%3De%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9031336%26hvtargid%3Dkwd-30350333447%26ref%3Dnav_custrec_signin%26hydadcr%3D15245_13597365%26gad_source%3D1&prevRID=QC09NDC6D7ESSHZRVCV1&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(3)
# #step cases
# #Find the logo
#
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")
print("Find the logo - passed")
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
print("Find the string ""- Createaccount"" - passed")
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")
print("Find the string ""- Your name"" - passed")
driver.find_element(By.CSS_SELECTOR, "input#ap_email")
print("Find the string ""- Mobile number or email"" - passed")
driver.find_element(By.CSS_SELECTOR, "input#ap_password")
print("Find the string ""- Password"" - passed")
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")
print("Find the string ""- Re-enter password"" - passed")
driver.find_element(By.CSS_SELECTOR, "input#continue")
print("Find the button ""Continue"" - passed")
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
print("Find the button ""Conditions of Use"" - passed")
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
print("Find the button ""Privacy Notice"" - passed")
driver.find_element(By.XPATH, "//a[@class='a-link-emphasis']")
print("Find the button ""Sign in"" - passed")


print("The locators accurately identify the intended page of Amazon elements and demonstrate efficiency in terms of performance and maintainability")























#
# driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
# print("Test case - passed. Logo has been found")
# #Find email field # selector #ap_email
# driver.find_element(By.XPATH, "//input[@type='email']")
# print("Test case by the type - email - passed. Email field has been found")
# driver.find_element(By.XPATH, "//input[@id='ap_email']")
# print("Test case by ID - ap_email - passed. Email field has been found")
# #Find Cintinue button #
# driver.find_element(By.XPATH, "//input[@id='continue']")
# print("Test case Continue button - by id - passed.")
# driver.find_element(By.XPATH, "//input[@class='a-button-input']")
# print("Test case Continue button - by class - passed.")
# driver.find_element(By.XPATH, "//*[contains(@class, 'a-button-input')]")
# print("Test case Continue button - by contains - passed.")
# driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
# print("Test case Privacy Notice - by Text - passed.")
# driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
# print("Test case <Need help?> - by tag span and the attribute class - passed.")
# driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
# print("Test case <Forgot your password?> - by tag id - passed.")
# driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link' and contains(@href, 'account-issues')]")
# print("Test case <Other issues with Sign-In> - by id - passed.")
# driver.find_element(By.ID, 'createAccountSubmit')
# print("Test case <Create your Amazon account> - by id - passed.")
# driver.find_element(By.XPATH,"//a[@id='createAccountSubmit' and contains(@href, 'ap')]")
# print("Test case <Create your Amazon account> - by id and contains (portion) - passed.")