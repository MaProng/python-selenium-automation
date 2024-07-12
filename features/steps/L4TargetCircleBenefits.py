from selenium.webdriver.common.by import By
from behave import given, then

@given('Open Target Circle main page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')

@then('Verify TargetCircle has {amount} benefits')
def verify_benefits(context, amount):
    amount = int(amount)
    benefits = context.driver.find_elements(By.CSS_SELECTOR, "//div[@class='cell-item-content']")
    assert len(benefits) == amount, f'Expected {amount} benefits but got {len(benefits)}'