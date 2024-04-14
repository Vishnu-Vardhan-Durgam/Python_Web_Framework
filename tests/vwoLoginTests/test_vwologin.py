# assertions are here
# https://app.vwo.com
# User name --> contact+atb5x@thetestingacademy.com
# Password --> ATBx@1234


import pytest
import allure
import time
from selenium import webdriver
from tests.PageObjects.loginPage import LoginPage
from tests.PageObjects.dashboardPage import DashBoardPage
from dotenv import load_dotenv


@pytest.fixture
def setup():  # start the webdriver  # call the page  # verify
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver

@allure.epic("VWO Login Test")
@allure.feature("TC#1 --> VWO App Negative Test Case")
def test_vwologin_negative(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login_to_vwo(user="admin", pwd="admin")
    time.sleep(5)
    error_message = loginPage.get_error_message_text()
    assert error_message == "Your email, password, IP address or location did not match"
    time.sleep(3)


@allure.epic("VWO Login Test")
@allure.feature("TC#1 --> VWO App Positive Test Case")
def test_vwologin(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login_to_vwo(user="contact+atb5x@thetestingacademy.com", pwd="ATBx@1234")
    time.sleep(5)

    # assert "Dashboard" not in 'Login - VWO'
    time.sleep(3)
