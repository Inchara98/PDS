from Locators.Locators import Locator_Path

class WeeklyReports:

    def __init__(self,driver):
        self.driver = driver


    def WeeklyReports(self):
        self.data = Locator_Path()
        Button = self.driver.find_element_by_id(self.data.WeeklyReports).click()


    def Choosefiles(self):
        self.data = Locator_Path()
        file = self.driver.find_element_by_id(self.data.choosefiles)
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