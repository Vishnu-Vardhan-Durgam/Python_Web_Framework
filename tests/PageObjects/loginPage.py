# page class

# page locators
# page actions
# webdriver - init
# custom functions
# No assertions here

#  -------------
#  pip install selenium - to install selenium
#  -------------
# pip install pytest - to install pytest
#  -------------
# pip install allure-pytest - to install allure
#  -------------
#  pip install python-dotenv  - to install dotenv
#  -------------
# pip install pytest-xdist  - to run testcases parallely
#  -------------
#  pytest -n -auto {path} -s -v - to run test cases parallely
#  -------------
#  pytest -n -auto {path}_* - to run all the test cases parallely with different class
#  -------------


from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

        # page locators

    username = (By.ID, "login-username")
    password = (By.NAME, "password")
    submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")

    # free_trial = (By.XPATH, "//a[normalize-space()='Start a free trial']")
    # sso_login = (By.XPATH, "//button[normalize-space()='Sign in using SSO']")
    # remember_checkbox = (By.XPATH, "//button[normalize-space()='Sign in using SSO']")

    # Return a web elements --> Username

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    # def get_free_trial(self):
    #     return self.driver.find_element(*LoginPage.free_trial)

    # page actions

    def login_to_vwo(self, user, pwd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()

    def get_error_message_text(self):
        return self.get_error_message().text

    # def click_free_trial(self):
    #     self.get_free_trial.click()
