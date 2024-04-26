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
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Fhomepage.html%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')


#Enter whisky in the search field
#driver.find_element(By.ID, 'ap-credential-autofill-hint').send_keys('whisky')
#Click search btn
driver.find_element(By.XPATH, "//input[@type='email']")
sleep(10)
"//input[@type='email']"
$x("//input[@type='email']")

$x("//input[@id='ap_email']")
$x("//input[@name='email']")
$x("//input[@name='password']")
$x("//input[@id='continue']")
$x("//input[@class='a-button-input']")