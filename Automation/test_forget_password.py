from selenium import webdriver
from selenium.webdriver.common.by import By


def open_forgot_page():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    driver.find_element(By.LINK_TEXT, "Forgot login info?").click()

    return driver


# TC_FORGOT_01 - Open recovery page
def test_open_recovery_page():
    driver = open_forgot_page()

    assert "Customer Lookup" in driver.page_source

    driver.quit()


# TC_FORGOT_02 - Valid customer lookup
def test_valid_customer_lookup():
    driver = open_forgot_page()

    driver.find_element(By.ID, "firstName").send_keys("John")
    driver.find_element(By.ID, "lastName").send_keys("Smith")
    driver.find_element(By.ID, "address.street").send_keys("1431 Main St")
    driver.find_element(By.ID, "address.city").send_keys("Beverly Hills")
    driver.find_element(By.ID, "address.state").send_keys("CA")
    driver.find_element(By.ID, "address.zipCode").send_keys("90210")
    driver.find_element(By.ID, "ssn").send_keys("123-45-6789")

    driver.find_element(
        By.CSS_SELECTOR,
        "input[value='Find My Login Info']"
    ).click()

    assert "login information" in driver.page_source.lower()

    driver.quit()


# TC_FORGOT_03 - Invalid customer lookup
def test_invalid_customer_lookup():
    driver = open_forgot_page()

    driver.find_element(By.ID, "firstName").send_keys("WrongName999")
    driver.find_element(By.ID, "lastName").send_keys("WrongLast999")
    driver.find_element(By.ID, "address.street").send_keys("Wrong Address")
    driver.find_element(By.ID, "address.city").send_keys("Wrong City")
    driver.find_element(By.ID, "address.state").send_keys("XX")
    driver.find_element(By.ID, "address.zipCode").send_keys("000000")
    driver.find_element(By.ID, "ssn").send_keys("000000000")

    driver.find_element(
        By.CSS_SELECTOR,
        "input[value='Find My Login Info']"
    ).click()

    assert "error" in driver.page_source.lower()

    driver.quit()


# TC_FORGOT_04 - Blank lookup form
def test_blank_lookup_form():
    driver = open_forgot_page()

    driver.find_element(
        By.CSS_SELECTOR,
        "input[value='Find My Login Info']"
    ).click()

    page = driver.page_source.lower()

    assert "required" in page or "error" in page

    driver.quit()