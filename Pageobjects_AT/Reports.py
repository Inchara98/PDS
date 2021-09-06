import time

from selenium.webdriver import ActionChains

from Locators.Locators import Locator_Path

class ReportPage:

    def __init__(self,driver):
        self.driver = driver

    def choosefiles(self):
        self.data = Locator_Path()
        file = self.driver.find_element_by_xpath(self.data.choosefiles)
        return file

    def Submit(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.Submit)

    def ExecuteButton(self):
        self.data = Locator_Path()
        Execute_Button = self.driver.find_element_by_xpath(self.data.ExecuteButton)
        return Execute_Button

    def Status(self):
        self.data = Locator_Path()
        Status = self.driver.find_element_by_xpath(self.data.Status)
        return Status