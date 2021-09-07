import time

from selenium.webdriver.support.select import Select

from Locators.Locators import Locator_Path

class Homepage_Billing:

    def __init__(self,driver):
        self.driver = driver

    def logut(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.Logout_Billing).click()

    def SelectYear(self):
        self.data = Locator_Path()
        Year = Select(self.driver.find_element_by_id(self.data.SelectYear))
        return Year

    def Dashboard(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.Dashboard).click()

