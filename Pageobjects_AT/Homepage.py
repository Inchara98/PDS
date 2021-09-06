import time

from selenium.webdriver import ActionChains

from Locators.Locators import Locator_Path

class Homepage:

    def __init__(self,driver):
        self.driver = driver

    def clicktoggle(self):
        self.data = Locator_Path()
        button = self.driver.find_element_by_xpath(self.data.toggle_menu_xpath)
        time.sleep(3)
        ActionChains(self.driver).move_to_element(button).click(button).perform()

    def clickFilemanager(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.File_manager_id).click()

    def clickExceptionReport(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.Exception_Report_id).click()

    def clicklogout(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.button_logout_class_name).click()

    def clickBooktoFacs(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.button_Book_to_Facs).click()

    def clickweeklyReport(self):
        self.data = Locator_Path()
        self.driver.fiend_element_by_id(self.data.button_weekly_Reports).click()