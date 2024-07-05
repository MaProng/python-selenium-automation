from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get("https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=3600&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&language=en_US&pageId=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fmyh%2Fhouseholds%3Flanguage%3Des&prevRID=P35H0J20BM4P8E0G3A12&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

#amazon logo
driver.find_element(By.CSS_SELECTOR, ".a-icon-logo")

#create account
driver.find_element(By.CSS_SELECTOR, ".a-spacing-small")

#your name
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

#email
driver.find_element(By.CSS_SELECTOR, "#ap_email")

#password
driver.find_element(By.CSS_SELECTOR, "#ap_password")

#password must be at least
driver.find_element(By.CSS_SELECTOR, ".a-alert-content")

#reenter password
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

#continue
driver.find_element(By.CSS_SELECTOR, "#continue")

#condition of use
driver.find_element(By.CSS_SELECTOR, ".a[href*='/gp/help/customer/display.html/ref=ap_register_notification_c']")

#privacy notice
driver.find_element(By.CSS_SELECTOR, ".a[href*='/gp/help/customer/display.html/ref=ap_register_notification_p']")

#sign in
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")