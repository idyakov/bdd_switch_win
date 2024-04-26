from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # def __init__(self, driver):
    #     self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def close(self):
        self.driver.close()

    def get_current_window(self):
        current_window = self.driver.current_window_handle
        print('Current:', current_window)
        print('All windows:', self.driver.window_handles)
        return current_window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles  # (Win1, Win2, ...)
        print('All windows ID:', self.driver.window_handles)
        print('Switching to second window with ID. :', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        print('Switching back to ... page_id (original): ', window_id)
        self.driver.switch_to.window(window_id)

class PrivacyTest(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.default_pw = 'Password'
