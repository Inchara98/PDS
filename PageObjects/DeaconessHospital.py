import time

from selenium.webdriver.support.select import Select

from Locators.Locators import Locator_Path

class DeaconessHospital:

    def __init__(self,driver):
        self.driver = driver

    def DeaconessHomepage(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.ColumbBargraph).click()
        time.sleep(4)

    def SelectYear(self):
        self.data = Locator_Path()
        Year = Select(self.driver.find_element_by_id(self.data.SelectYear))
        return Year
