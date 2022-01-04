from Locators.Locators import Locator_Path
from selenium.webdriver.support.select import Select

class WeeklyReports:

    def __init__(self,driver):
        self.driver = driver


    def WeeklyReports(self):
        self.data = Locator_Path()
        Button = self.driver.find_element_by_id(self.data.WeeklyReports).click()
        return Button


    def Choosefiles(self):
        self.data = Locator_Path()
        file = self.driver.find_element_by_id(self.data.Choosefile)
        return file

    def Submit(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.Submit_WR)

    def ExecuteButton(self):
        self.data = Locator_Path()
        Execute_Button = self.driver.find_element_by_xpath(self.data.ExecuteButton_WR)
        return Execute_Button

    def Download_WR(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.Download_WR)


    def SelectYear_WK(self):
        self.data = Locator_Path()
        year = Select(self.driver.find_element_by_id(self.data.SelectYear_WR))
        return year

    def SelectMonth_WK(self):
        self.data = Locator_Path()
        month = Select(self.driver.find_element_by_id(self.data.SelectMonth_WR))
        return month

    def SelectWeek(self):
        self.data = Locator_Path()
        Week = Select(self.driver.find_element_by_id(self.data.SelectWeek_WR))
        return Week
