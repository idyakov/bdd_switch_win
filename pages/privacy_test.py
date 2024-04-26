from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class PrivacyTest(Page):
    SIGN_IN_BUTTON_MAIN_PAGE = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    SING_IN_POPUP = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
    TARGET_EMAIL = (By.CSS_SELECTOR, "[id*='username']")  # input email
    TARGET_PASSWORD = (By.CSS_SELECTOR, "[id*='password']")  # input password
    CLICK_SIGN_IN_USER = (By.CSS_SELECTOR,
                          "button[class='styles__StyledBaseButtonInternal-sc-ysboml-0 "
                          "styles__ButtonPrimary-sc-5fh6rr-0 styles__SignInButton-sc-q9vn5-4 hBqTSs bEdlr gCsDNn']")
    TARGET_VERIFY_ACCOUNT = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    # click button SIgn in with password
    TARGET_NAME_VERIFICATION = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    TARGET_TERM_COND = (By.CSS_SELECTOR, 'a[aria-label="terms & conditions - opens in a new window"]')
    TARGET_PRIVACY_POLICY = (By.CSS_SELECTOR, 'a[aria-label="privacy policy - opens in a new window"]')

    def click_sign_in(self):
        self.click(*self.SIGN_IN_BUTTON_MAIN_PAGE)

    def click_signin_popup(self):
        self.click(*self.SING_IN_POPUP)

    # def store_original_window(self):
    #     self.click(*self.SING_IN_POPUP)

    def click_tc(self):
        self.click(*self.TARGET_TERM_COND)
        sleep(5)

    def verify_tc(self, expected_url):
        print(expected_url)
        self.wait.until(EC.url_contains(expected_url), message=f'URL verified')

    def close_current_page(self):
        self.click(*self.TARGET_VERIFY_ACCOUNT)
        sleep(5)

    def return_to_original(self):
        self.click(*self.TARGET_VERIFY_ACCOUNT)
        sleep(5)
