import time

from selenium.webdriver.support.select import Select

from Locators.Locators import Locator_Path

class Group_not_knownHospital:

    def __init__(self,driver):
        self.driver = driver

    def Group_not_knownHomepage(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.Group_not_KnownBargraph).click()
        time.sleep(4)

    def SelectYear(self):
        self.data = Locator_Path()
        Year = Select(self.driver.find_element_by_id(self.data.SelectYear))
        return Year

    def HospitalRevenue(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.HospitalRevenue).text


    def HospitalTotal_Transaction(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.HospitalTotal_Transaction).text

    def HospitalTotal_Payment(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.HospitalTotal_Payment).text

    def HospitalLegal_Action(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.HospitalLegal_Action).text

    def HospitalPageTittle(self):
        self.date = Locator_Path()
        self.driver.find_element_by_css_selector(self.data.HospitalPageTittle).text