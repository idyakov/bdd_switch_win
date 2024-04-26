$x("//input[@type='email']")
$x("//input[@id='ap_email']")
$x("//input[@name='email']")
$x("//input[@name='password']")
$x("//input[@id='continue']")

#CSS Selector
$$("[aria-label='reset']")



#find by chaled and parent with Class locators
$$("[data-component-title*='BaseDrivers'] div.cell-item-content")


#check the Target top elements 
LISTINGS = (BY.CSS_SELECTOR,"[data-test='@web/site-top-of-funnel/ProductCardWrapper']"