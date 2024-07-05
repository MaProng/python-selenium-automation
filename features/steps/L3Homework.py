from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target.com')
def open_target(context):
    context.driver.get('https://www.target.com/')
@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//[@data-test='@web/CartLink']").click()
    sleep(7)
@then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    sleep(7)
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "//div[@data-test='boxEmptyMsg']").text
    assert expected_text in actual_text, f"Expected, {expected_text} is not in {actual_text}"
    print('TEST PASSED')



@when('Click on Sign in')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
    sleep(6)
@when('Click Sign in from dropdown')
def click_sign_in_dropdown(context):
    context.driver.find_element(By.XPATH, "//span[@class='sc-859e7637-0 hHZPQy']").click()
    sleep(6)
@then('Verify Sign in form opened')
def verify_sign_in(context):
    var = context.driver.find_element(By.CSS_SELECTOR,'form')
    if var is None:
        print('TEST NOT PASSED')
    else:
        print('TEST PASSED !!! FORM OPENED')