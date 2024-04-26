from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import then, given, when
from time import sleep


@given('Open Target main page')
def open_target(context):
    context.app.main_page.open_main()


@given("Target Signin button pressed")
def click_sign_in(context):
    context.app.privacy_test.click_sign_in()


@given("Target Signin button popup")
def click_signin_popup(context):
    context.app.privacy_test.click_signin_popup()


@given("Store original window")
def get_current_window(context):
    context.original_window = context.app.privacy_test.get_current_window()


#    context.app.privacy_test.store_original_window()

@given("Click Terms and Cond link")
def click_privacy_page(context):
    context.app.privacy_test.click_tc()


@given("Switch to new window")
def switch_to_new_window(context):
    context.app.privacy_test.switch_to_new_window()


@then("Verify Terms and Cond page opened")
def verify_tc(context):
    context.app.privacy_test.verify_tc('https://www.target.com/c/terms-conditions/-/N-4sr7l')
    sleep(10)

@given("Close current page")
def close_current_page(context):
    context.app.privacy_test.close()


@then("Return to original Target window")
def return_to_original(context):
    context.app.privacy_test.switch_to_window_by_id(context.original_window)
    sleep(10)
