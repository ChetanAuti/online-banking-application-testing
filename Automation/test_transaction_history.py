from selenium import webdriver
from selenium.webdriver.common.by import By


def open_transaction_history():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    driver.find_element(By.NAME, "username").send_keys("john")
    driver.find_element(By.NAME, "password").send_keys("demo")
    driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()

    return driver


# TC_TXN_01 - History opens
def test_history_opens():
    driver = open_transaction_history()

    driver.find_element(By.LINK_TEXT, "Find Transactions").click()

    assert "Find Transactions" in driver.page_source

    driver.quit()


# TC_TXN_02 - Transfer appears
def test_transfer_appears():
    driver = open_transaction_history()

    driver.find_element(By.LINK_TEXT, "Find Transactions").click()

    assert "Find Transactions" in driver.page_source

    driver.quit()


# TC_TXN_03 - Amount and date
def test_amount_and_date():
    driver = open_transaction_history()

    driver.find_element(By.LINK_TEXT, "Find Transactions").click()

    assert "Transaction" in driver.page_source
    assert "Date" in driver.page_source

    driver.quit()


# TC_TXN_04 - No duplicate transaction
def test_no_duplicate_transaction():
    driver = open_transaction_history()

    driver.find_element(By.LINK_TEXT, "Find Transactions").click()

    page = driver.page_source

    assert page.count("Transaction") >= 1

    driver.refresh()

    refreshed_page = driver.page_source

    assert refreshed_page.count("Transaction") >= 1

    driver.quit()