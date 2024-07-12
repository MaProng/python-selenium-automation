from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Serch for {watermelon}')
def watermelon_search(context, watermelon):
    context.driver.find_element(By.ID, 'search').send_keys(watermelon)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)

@then('Add product in to cart')
def add_watermelon(context):
    context.driver.find_element(By.ID, 'addToCartButtonOrTextIdFor15013952').click()
    sleep(3)
    context.driver.find_element(By.ID, 'addToCartButtonOrTextIdFor15013952').click()
    sleep(3)

@then('Verify product is in the cart')
def verify_product(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    sleep(3)