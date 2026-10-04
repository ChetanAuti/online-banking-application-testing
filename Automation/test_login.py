from selenium import webdriver
from selenium.webdriver.common.by import By


def open_login_page():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    return driver


# TC_LOGIN_01 - Valid Login
def test_valid_login():

    driver = open_login_page()

    driver.find_element(By.NAME, "username").send_keys("john")
    driver.find_element(By.NAME, "password").send_keys("demo")
    driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()

    assert "Accounts Overview" in driver.page_source

    driver.quit()


# TC_LOGIN_02 - Invalid Password
def test_invalid_password():

    driver = open_login_page()

    driver.find_element(By.NAME, "username").send_keys("john")
    driver.find_element(By.NAME, "password").send_keys("Wrong@123")
    driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()

    # Application currently accepts wrong password
    assert "Accounts Overview" not in driver.page_source

    driver.quit()


# TC_LOGIN_03 - Invalid Username
def test_invalid_username():

    driver = open_login_page()

    driver.find_element(By.NAME, "username").send_keys("wronguser999")
    driver.find_element(By.NAME, "password").send_keys("demo")
    driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()

    error_message = driver.find_element(
        By.XPATH,
        "//*[contains(text(),'The username and password could not be verified.')]"
    ).text

    assert error_message == "The username and password could not be verified."

    driver.quit()


# TC_LOGIN_05 - Blank Username
def test_blank_username():

    driver = open_login_page()

    driver.find_element(By.NAME, "password").send_keys("demo")
    driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()

    assert "Please enter a username and password." in driver.page_source

    driver.quit()


# TC_LOGIN_07 - Both Username and Password Blank
def test_both_blank():

    driver = open_login_page()

    driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()

    assert "Please enter a username and password." in driver.page_source

    driver.quit()


# TC_LOGIN_08 - Password Masking
def test_password_masking():

    driver = open_login_page()

    password_field = driver.find_element(By.NAME, "password")

    assert password_field.get_attribute("type") == "password"

    driver.quit()


# TC_LOGIN_09 - Forgot Login Information
def test_forgot_login_info():

    driver = open_login_page()

    driver.find_element(By.LINK_TEXT, "Forgot login info?").click()

    assert "Customer Lookup" in driver.page_source

    driver.quit()