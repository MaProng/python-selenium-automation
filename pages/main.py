CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")


@given('Open Target main page')
def open_target(context):
    context.app.main_page.open_main()


@when('Click Sign in from dropdown')
def click_sign_in_dropdown(context):
    context.app.side_menu_page.click_sign_in_dropdown()
    #context.wait.until(EC.element_to_be_clickable(SIGN_IN_DROPDOWN)).click()


@then('Verify Sign in form opened')
def verify_sign_in(context):
    context.app.sign_in_form_page.verify_sign_in()
    #context.driver.find_element(*SIGN_IN_FORM)


@when('Click on Sign in')
def click_sign_in(context):
    #context.wait.until(EC.element_to_be_clickable(SIGN_IN_BUTTON)).click()
    context.app.header.click_sign_in()


@when("Search for {item}")
def search_product(context, item):
    context.app.header.search_product(item)


@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_go_to_cart()


@then('Verify header in shown')
def verify_header_shown(context):


@when('Adding product to cart')
def add_to_cart(context):
    context.app.search_result_page.click_add_to_cart_button()
    context.app.product_side_bar.add_to_cart_product()
    context.app.product_side_bar.view_cart_click()


@then('Verify product in our cart in cart page')
def verify_product(context):
    context.app.cart_page.verify_product()