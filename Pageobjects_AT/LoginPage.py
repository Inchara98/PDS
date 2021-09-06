import time
from selenium.webdriver.support.select import Select
from Locators.Locators import Locator_Path

class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.textbox_username_id).send_keys(username)


    def setPassword(self,password):
        self.data = Locator_Path()
        self.driver.find_element_by_xpath(self.data.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.data = Locator_Path()
        self.driver.find_element_by_xpath(self.data.button_login_xpath).click()

    def clickLogout(self):
        self.data = Locator_Path()
        self.driver.find_element_by_class_name(self.data.button_logout_class_name).click()
