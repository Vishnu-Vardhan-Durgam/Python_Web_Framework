# page locators
# https://app.vwo.com
# User name --> contact+atb5x@thetestingacademy.com
# Password --> ATBx@1234

from selenium import webdriver
from selenium.webdriver.common.by import By


class DashBoardPage():

    def __init__(self, driver):
        self.driver = driver

    user_logged_in = (By.XPATH, "//span[@data-qa='lufexuloga']")

    def get_user_logged_in(self):
        return self.driver.find_element(*DashboardPage.user_logged_in)

    def user_logged_in_text(self):
        return self.get_user_logged_in().text()

    # page actions
