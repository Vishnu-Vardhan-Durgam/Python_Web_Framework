# page class

# page locators
# page actions
# webdriver - init
# custom functions
# No assertions here


from selenium import webdriver
from selenium.webdriver.common.by import By


class KatalonHomePage(object):

    def __init__(self, driver):
        self.driver = driver

        # page locators

    make_appointment = (By.XPATH, "//a[@id='btn-make-appointment']")  # This is a tuple

    # Return a web elements --> Username

    def get_make_appointment(self):
        return self.driver.find_element(*KatalonHomePage.make_appointment)  # This is unpacking of tuple

    # page actions

    def katalon_home_page(self):
        self.get_make_appointment().click()
