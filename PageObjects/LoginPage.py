from selenium import webdriver
from Utilities.readProperties import ReadConfig
from Locators.Locators import Locator_Path

class LoginPage:
    textbox_username = "username"
    textbox_password = "password"
    button_login = "login"
    button_logout = "logout"
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    FakeUsername = ReadConfig.getUser()
    FakePassword = ReadConfig.getpassword()
    Empty = ReadConfig.getEmpty()




    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username).send_keys(username)

    def setUserNameFake(self,FakeUsername):
        self.driver.find_element_by_id(self.textbox_username).send_keys(FakeUsername)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password).send_keys(password)


    def setPasswordFake(self,FakePassword):
        self.driver.find_element_by_id(self.textbox_password).send_keys(FakePassword)

    def EmptyUsername(self,Empty):
        self.driver.find_element_by_id(self.textbox_username).send_keys(Empty)

    def EmptyPassword(self,Empty):
        self.driver.find_element_by_id(self.textbox_password).send_keys(Empty)


    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login).click()

    def clickLogout(self):
        self.driver.find_element_by_id(self.button_logout).click()

    def login_PDS(self):
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

    def RealUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username).send_keys(username)