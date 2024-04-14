import pytest
import allure
import time
from tests.PageObjects.katalonLoginPage import KatalonHomePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin():

    @allure.epic("Katalon Home Page")
    @allure.feature("TC#0 --> Katalon Home Page")
    @pytest.mark.usefixtures("setup")
    def test_katalon_login(self, setup):
        driver = setup
        driver.get(self.katalon_url) # -->Optional to import from conftest
        khp = KatalonHomePage(driver)
        khp.katalon_home_page()
        assert "profile.php#login" in driver.current_url
        time.sleep(3)

