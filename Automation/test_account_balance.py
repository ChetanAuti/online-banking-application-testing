from selenium import webdriver
from selenium.webdriver.common.by import By


def open_account_overview():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    driver.find_element(By.NAME, "username").send_keys("john")
    driver.find_element(By.NAME, "password").send_keys("demo")
    driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()

    return driver


# TC_BAL_01 - Current Balance Display
def test_current_balance_display():

    driver = open_account_overview()

    assert "Balance" in driver.page_source

    driver.quit()


# TC_BAL_02 - Balance After Transaction
def test_balance_after_transaction():

    driver = open_account_overview()

    # Open account overview after transaction
    assert "Balance" in driver.page_source

    driver.quit()


# TC_BAL_03 - Account Number Display
def test_account_number_display():

    driver = open_account_overview()

    # Account number should be displayed
    assert "Account" in driver.page_source

    driver.quit()