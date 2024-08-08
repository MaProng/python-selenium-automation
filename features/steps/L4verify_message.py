from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@then("Verify 'What can we help you find?' message in the search box is shown")
def verify_search_message(context):
    expected_text = 'What can we help you find?'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[aria-label='What can we help you find? suggestions appear below']").text
    assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'