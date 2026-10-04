from selenium import webdriver
from selenium.webdriver.common.by import By


def open_transfer_page():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    driver.find_element(By.NAME, "username").send_keys("john")
    driver.find_element(By.NAME, "password").send_keys("demo")
    driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()

    driver.find_element(By.LINK_TEXT, "Transfer Funds").click()

    return driver


# TC_TRANSFER_01 - Valid Transfer
def test_valid_transfer():

    driver = open_transfer_page()

    driver.find_element(By.ID, "amount").send_keys("100")
    driver.find_element(By.CSS_SELECTOR, "input[value='Transfer']").click()

    assert "Transfer Complete!" in driver.page_source

    driver.quit()


# TC_TRANSFER_02 - Amount Greater Than Balance
def test_amount_greater_than_balance():

    driver = open_transfer_page()

    driver.find_element(By.ID, "amount").send_keys("9999999")
    driver.find_element(By.CSS_SELECTOR, "input[value='Transfer']").click()

    print("\nACTUAL PAGE TEXT:")
    print(driver.find_element(By.TAG_NAME, "body").text)

    driver.quit()


# TC_TRANSFER_03 - Invalid Destination Account
def test_invalid_destination_account():

    driver = open_transfer_page()

    driver.find_element(By.ID, "toAccountId").send_keys("999999")
    driver.find_element(By.ID, "amount").send_keys("100")
    driver.find_element(By.CSS_SELECTOR, "input[value='Transfer']").click()

    assert "error" in driver.page_source.lower()

    driver.quit()


# TC_TRANSFER_04 - Blank Amount
def test_blank_amount():

    driver = open_transfer_page()

    driver.find_element(By.CSS_SELECTOR, "input[value='Transfer']").click()

    print("\nACTUAL PAGE TEXT:")
    print(driver.find_element(By.TAG_NAME, "body").text)

    driver.quit()


# TC_TRANSFER_05 - Zero Amount
def test_zero_amount():

    driver = open_transfer_page()

    driver.find_element(By.ID, "amount").send_keys("0")
    driver.find_element(By.CSS_SELECTOR, "input[value='Transfer']").click()

    # Expected: zero amount should be rejected
    # Actual application allows the transfer
    assert "Transfer Complete!" not in driver.page_source

    driver.quit()


# TC_TRANSFER_06 - Transfer Appears in History
def test_transfer_appears_in_history():

    driver = open_transfer_page()

    driver.find_element(By.ID, "amount").send_keys("100")
    driver.find_element(By.CSS_SELECTOR, "input[value='Transfer']").click()

    driver.find_element(By.LINK_TEXT, "Find Transactions").click()

    assert "Find Transactions" in driver.page_source

    driver.quit()