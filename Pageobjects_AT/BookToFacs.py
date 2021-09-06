from Locators.Locators import Locator_Path

class BookToFacs:

    def __init__(self,driver):
        self.driver = driver


    def BookToFacs(self):
        self.data = Locator_Path()
        Button = self.driver.find_element_by_id(self.data.BookToFacs).click()


    def Choosefiles(self):
        self.data = Locator_Path()
        file = self.driver.find_element_by_id(self.data.choosefiles)
        return file

    def Submit(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.Submit_BK)

    def ExecuteButton(self):
        self.data = Locator_Path()
        Execute_Button = self.driver.find_element_by_xpath(self.data.ExecuteButton_BK)
        return Execute_Button

    def Download_BK(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.Download_BK)