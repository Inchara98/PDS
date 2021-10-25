import time

from selenium.webdriver.support.select import Select

from Locators.Locators import Locator_Path

class OrthoHospital:

    def __init__(self,driver):
        self.driver = driver

    def OrthoHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("ORTHO")
        return a

    def SelectYear(self):
        self.data = Locator_Path()
        Year = Select(self.driver.find_element_by_id(self.data.SelectYear))
        return Year

    def HospitalRevenue(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.HospitalRevenue).text


    def Total_Transaction(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.HospitalTotal_Transaction).text

    def Total_Payment(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.HospitalTotal_Payment).text

    def Legal_Action(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.HospitalLegal_Action).text

    def CommunityPageTittle(self):
        self.date = Locator_Path()
        self.driver.find_element_by_css_selector(self.data.HospitalPageTittle).text

    def Hospitaldropdown(self):
        self.date = Locator_Path()
        Hospital = Select(self.driver.find_element_by_id(self.data.Hospitaldropdown))
        return Hospital
