import pytest
import allure
import time
from tests.PageObjects.loginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin(object):

    @allure.epic("VWO Login Test")
    @allure.feature("TC#1 --> VWO App Negative Test Case")
    @pytest.mark.usefixtures("setup")
    def test_vwologin_negative(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user="admin", pwd="admin")
        time.sleep(5)
        error_message = loginPage.get_error_message_text()
        assert error_message == "Your email, password, IP address or location did not match"
        time.sleep(2)

    @allure.epic("VWO Login Test")
    @allure.feature("TC#1 --> VWO App Positive Test Case")
    @pytest.mark.usefixtures("setup")
    def test_vwo_login_positive(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user=self.username, pwd=self.password)
        time.sleep(5)
        assert 'Dashboard' != 'Login - VWO'
        time.sleep(2)
