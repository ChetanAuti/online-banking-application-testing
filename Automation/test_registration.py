from selenium import webdriver
from selenium.webdriver.common.by import By


def open_registration_page():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/register.htm")
    return driver


# TC_REG_01 - Valid Registration
def test_valid_registration():

    driver = open_registration_page()

    driver.find_element(By.ID, "customer.firstName").send_keys("Chetan")
    driver.find_element(By.ID, "customer.lastName").send_keys("Auti")
    driver.find_element(By.ID, "customer.address.street").send_keys("Pune")
    driver.find_element(By.ID, "customer.address.city").send_keys("Pune")
    driver.find_element(By.ID, "customer.address.state").send_keys("Maharashtra")
    driver.find_element(By.ID, "customer.address.zipCode").send_keys("411001")
    driver.find_element(By.ID, "customer.phoneNumber").send_keys("9876543210")
    driver.find_element(By.ID, "customer.ssn").send_keys("123456789")

    driver.find_element(
        By.ID, "customer.username"
    ).send_keys("chetan_reg_20261004")

    driver.find_element(By.ID, "customer.password").send_keys("Test@123")
    driver.find_element(By.ID, "repeatedPassword").send_keys("Test@123")

    driver.find_element(By.CSS_SELECTOR, "input[value='Register']").click()

    assert "Your account was created successfully." in driver.page_source

    driver.quit()


# TC_REG_02 - Blank First Name
def test_blank_first_name():

    driver = open_registration_page()

    driver.find_element(By.ID, "customer.lastName").send_keys("Auti")
    driver.find_element(By.ID, "customer.address.street").send_keys("Pune")
    driver.find_element(By.ID, "customer.address.city").send_keys("Pune")
    driver.find_element(By.ID, "customer.address.state").send_keys("Maharashtra")
    driver.find_element(By.ID, "customer.address.zipCode").send_keys("411001")
    driver.find_element(By.ID, "customer.phoneNumber").send_keys("9876543210")
    driver.find_element(By.ID, "customer.ssn").send_keys("123456789")
    driver.find_element(By.ID, "customer.username").send_keys("blank_first_test")
    driver.find_element(By.ID, "customer.password").send_keys("Test@123")
    driver.find_element(By.ID, "repeatedPassword").send_keys("Test@123")

    driver.find_element(By.CSS_SELECTOR, "input[value='Register']").click()

    assert "First name is required" in driver.page_source

    driver.quit()


# TC_REG_03 - Blank Last Name
def test_blank_last_name():

    driver = open_registration_page()

    driver.find_element(By.ID, "customer.firstName").send_keys("Chetan")

    driver.find_element(By.CSS_SELECTOR, "input[value='Register']").click()

    assert "Last name is required" in driver.page_source

    driver.quit()


# TC_REG_04 - Blank Address
def test_blank_address():

    driver = open_registration_page()

    driver.find_element(By.ID, "customer.firstName").send_keys("Chetan")
    driver.find_element(By.ID, "customer.lastName").send_keys("Auti")

    driver.find_element(By.CSS_SELECTOR, "input[value='Register']").click()

    assert "Address is required" in driver.page_source

    driver.quit()


# TC_REG_06 - Mismatched Passwords
def test_mismatched_passwords():

    driver = open_registration_page()

    driver.find_element(By.ID, "customer.firstName").send_keys("Chetan")
    driver.find_element(By.ID, "customer.lastName").send_keys("Auti")
    driver.find_element(By.ID, "customer.address.street").send_keys("Pune")
    driver.find_element(By.ID, "customer.address.city").send_keys("Pune")
    driver.find_element(By.ID, "customer.address.state").send_keys("Maharashtra")
    driver.find_element(By.ID, "customer.address.zipCode").send_keys("411001")
    driver.find_element(By.ID, "customer.phoneNumber").send_keys("9876543210")
    driver.find_element(By.ID, "customer.ssn").send_keys("123456789")
    driver.find_element(By.ID, "customer.username").send_keys("mismatch_test")
    driver.find_element(By.ID, "customer.password").send_keys("Test@123")
    driver.find_element(By.ID, "repeatedPassword").send_keys("Test@456")

    driver.find_element(By.CSS_SELECTOR, "input[value='Register']").click()

    assert "Passwords did not match" in driver.page_source

    driver.quit()


 # TC_REG_07 - Duplicate Username
def test_duplicate_username():

    driver = open_registration_page()

    driver.find_element(By.ID, "customer.firstName").send_keys("Chetan")
    driver.find_element(By.ID, "customer.lastName").send_keys("Auti")
    driver.find_element(By.ID, "customer.address.street").send_keys("Pune")
    driver.find_element(By.ID, "customer.address.city").send_keys("Pune")
    driver.find_element(By.ID, "customer.address.state").send_keys("Maharashtra")
    driver.find_element(By.ID, "customer.address.zipCode").send_keys("411001")
    driver.find_element(By.ID, "customer.phoneNumber").send_keys("9876543210")
    driver.find_element(By.ID, "customer.ssn").send_keys("123456789")

    # Already registered username
    driver.find_element(By.ID, "customer.username").send_keys("auto_test_98765_2")

    driver.find_element(By.ID, "customer.password").send_keys("Test@123")
    driver.find_element(By.ID, "repeatedPassword").send_keys("Test@123")

    driver.find_element(By.CSS_SELECTOR, "input[value='Register']").click()

    assert "This username already exists." in driver.page_source

    driver.quit()


# TC_REG_08 - Login with New User
def test_login_with_new_user():

    driver = webdriver.Chrome()

    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    driver.find_element(By.NAME, "username").send_keys("auto_test_98765")
    driver.find_element(By.NAME, "password").send_keys("Test@123")

    driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()

    assert "Accounts Overview" in driver.page_source

    driver.quit()