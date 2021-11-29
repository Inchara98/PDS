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
        self.driver.find_element_by_id(self.data.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.Submit_button).click()

    def clickLogout(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.button_logout_id).click()


    def setUserNameFake(self,FakeUsername):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.textbox_username_id).send_keys(FakeUsername)

    def setPasswordFake(self,FakePassword):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.textbox_password_id).send_keys(FakePassword)

    def EmptyUsername(self,Empty):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.textbox_username_id).send_keys(Empty)

    def EmptyPassword(self,Empty):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.textbox_password_id).send_keys(Empty)
