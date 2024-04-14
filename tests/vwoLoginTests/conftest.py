import pytest
import time
import os
from selenium import webdriver
from tests.PageObjects.loginPage import LoginPage
from tests.PageObjects.dashboardPage import DashBoardPage
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    username = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")
    base_url = os.getenv("BASE_URL")
    katalon_url = os.getenv("KATALON_URL")
    # driver.get(base_url)

    request.cls.driver = driver
    request.cls.username = username
    request.cls.password = password
    request.cls.base_url = base_url
    request.cls.katalon_url = katalon_url

    yield driver
    driver.quit()
