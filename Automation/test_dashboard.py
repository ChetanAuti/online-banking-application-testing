from selenium import webdriver
from selenium.webdriver.common.by import By


def open_dashboard():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    driver.find_element(By.NAME, "username").send_keys("john")
    driver.find_element(By.NAME, "password").send_keys("demo")
    driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()

    return driver


# TC_DASH_01 - Dashboard loads
def test_dashboard_loads():
    driver = open_dashboard()

    assert "Accounts Overview" in driver.page_source

    driver.quit()


# TC_DASH_02 - Account information display
def test_account_information_display():
    driver = open_dashboard()

    assert "Balance" in driver.page_source
    assert "Account" in driver.page_source

    driver.quit()


# TC_DASH_03 - Navigation links
def test_navigation_links():
    driver = open_dashboard()

    driver.find_element(By.LINK_TEXT, "Transfer Funds").click()

    assert "Transfer Funds" in driver.page_source

    driver.quit()


# TC_DASH_04 - Logout from dashboard
def test_logout_from_dashboard():
    driver = open_dashboard()

    driver.find_element(By.LINK_TEXT, "Log Out").click()

    assert "Username" in driver.page_source
    assert "Password" in driver.page_source

    driver.quit()