from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

cart_icon = (By.XPATH, "//[@data-test='@web/CartLink']")
cart_empty_message = (By.CSS_SELECTOR, "//div[@data-test='boxEmptyMsg']")
account_dropdown_page = (By.CSS_SELECTOR, "//div[@class='styles_baseCell__zb2BN styles_bottom__6vPQ_']")
sign_in_button = (By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']")
sign_in_dropdown_button = (By.XPATH, "//span[@class='sc-859e7637-0 hHZPQy']")
target_account_sign_in = (By.CSS_SELECTOR, "//div[@data-test='content-wrapper']")

@given('Open target.com')
def open_target(context):
    context.driver.get('https://www.target.com/')
@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(*cart_icon).click()
    context.driver.wait.until(EC.visibility_of_element_located(cart_empty_message))
@then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    context.driver.wait.until(EC.visibility_of_element_located(cart_empty_message))
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "//div[@data-test='boxEmptyMsg']").text
    assert expected_text in actual_text, f"Expected, {expected_text} is not in {actual_text}"
    print('TEST PASSED')



@when('Click on Sign in')
def click_sign_in(context):
    context.driver.find_element(*sign_in_button).click()
    context.driver.wait.until(EC.visibility_of_element_located(account_dropdown_page))
@when('Click Sign in from dropdown')
def click_sign_in_dropdown(context):
    context.driver.find_element(*sign_in_dropdown_button).click()
    context.driver.wait.until(EC.visibility_of_element_located(target_account_sign_in))
@then('Verify Sign in form opened')
def verify_sign_in(context):
    var = context.driver.find_element(By.CSS_SELECTOR,'form')
    if var is None:
        print('TEST NOT PASSED')
    else:
        print('TEST PASSED !!! FORM OPENED')
