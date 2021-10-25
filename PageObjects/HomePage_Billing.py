import time

from selenium.webdriver.support.select import Select

from Locators.Locators import Locator_Path

class Homepage_Billing:

    def __init__(self,driver):
        self.driver = driver

    def logout(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.Logout_Billing).click()

    def SelectYear(self):
        self.data = Locator_Path()
        Year = Select(self.driver.find_element_by_id(self.data.SelectYear1))
        return Year

    def Dashboard(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.Dashboard).click()


    def Revenue(self):
        self.data = Locator_Path()
        e = self.driver.find_element_by_id(self.data.Revenue).text
        return e


    def Total_Transaction(self):
        self.data = Locator_Path()
        f = self.driver.find_element_by_id(self.data.Total_Transaction).text
        return f

    def Total_Payment(self):
        self.data = Locator_Path()
        g = self.driver.find_element_by_id(self.data.Total_Payment).text
        return g

    def Legal_Action(self):
        self.data = Locator_Path()
        h = self.driver.find_element_by_id(self.data.Legal_Action).text
        return h

    def RevenueTittle(self):
        self.date = Locator_Path()
        revenue = self.driver.find_element_by_css_selector(self.data.RevenueTittle1).text
        return revenue
