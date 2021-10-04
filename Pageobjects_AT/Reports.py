import time

from selenium.webdriver import ActionChains

from Locators.Locators import Locator_Path

class ReportPage:

    def __init__(self,driver):
        self.driver = driver

    def choosefilesCommunity(self):
        self.data = Locator_Path()
        file = self.driver.find_element_by_id(self.data.choosefilesCommunity)
        return file

    def choosefilesDeaconess(self):
        self.data = Locator_Path()
        file = self.driver.find_element_by_id(self.data.choosefilesDeaconess)
        return file

    def choosefilesWomenshsptl(self):
        self.data = Locator_Path()
        file = self.driver.find_element_by_id(self.data.choosefilesWomenshsptl)
        return file

    def choosefilesVincent(self):
        self.data = Locator_Path()
        file = self.driver.find_element_by_id(self.data.choosefilesVincent)
        return file

    def choosefilesVincentDunn(self):
        self.data = Locator_Path()
        file = self.driver.find_element_by_id(self.data.choosefilesVincentDunn)
        return file

    def choosefilesParkview(self):
        self.data = Locator_Path()
        file = self.driver.find_element_by_id(self.data.choosefilesParkview)
        return file

    def choosefileGoodsamFam(self):
        self.data = Locator_Path()
        file = self.driver.find_element_by_id(self.data.choosefileGoodsamFam)
        return file

    def SubmitCommunity(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.SubmitCommunity)

    def SubmitDeaconess(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.SubmitDeaconess)

    def SubmitWomenshsptl(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.SubmitWomenshsptl)


    def SubmitVincent(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.SubmitVincent)

    def SubmitVincentDunn(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.SubmitVincentDunn)


    def SubmitGoodSam(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.SubmitGoodSam)


    def SubmitParkView(self):
        self.data = Locator_Path()
        self.driver.find_element_by_id(self.data.SubmitParkView)

    def ExecuteButtonCommunity(self):
        self.data = Locator_Path()
        Execute_Button = self.driver.find_element_by_id(self.data.ExecuteButtonCommunity)
        return Execute_Button

    def ExecuteButtonDeaconess(self):
        self.data = Locator_Path()
        Execute_Button = self.driver.find_element_by_id(self.data.ExecuteButtonDeaconess)
        return Execute_Button

    def ExecuteButtonWomenshsptl(self):
        self.data = Locator_Path()
        Execute_Button = self.driver.find_element_by_id(self.data.ExecuteButtonWomenshsptl)
        return Execute_Button

    def ExecuteButtonVincent(self):
        self.data = Locator_Path()
        Execute_Button = self.driver.find_element_by_id(self.data.ExecuteButtonVincent)
        return Execute_Button

    def ExecuteButtonVincentDunn(self):
        self.data = Locator_Path()
        Execute_Button = self.driver.find_element_by_id(self.data.ExecuteButtonVincentDunn)
        return Execute_Button

    def ExecuteButtonParkview(self):
        self.data = Locator_Path()
        Execute_Button = self.driver.find_element_by_id(self.data.ExecuteButtonParkview)
        return Execute_Button

    def ExecuteButtonGoodSam(self):
        self.data = Locator_Path()
        Execute_Button = self.driver.find_element_by_id(self.data.ExecuteButtonGoodSam)
        return Execute_Button

    def StatusCommunity(self):
        self.data = Locator_Path()
        Status = self.driver.find_element_by_id(self.data.StatusCommunity)
        return Status

    def StatusDeaconess(self):
        self.data = Locator_Path()
        Status = self.driver.find_element_by_id(self.data.StatusDeaconess)
        return Status

    def StatusWomenshsptl(self):
        self.data = Locator_Path()
        Status = self.driver.find_element_by_id(self.data.StatusWomenshsptl)
        return Status

    def StatusVincent(self):
        self.data = Locator_Path()
        Status = self.driver.find_element_by_id(self.data.StatusVincent)
        return Status

    def StatusVincentDunn(self):
        self.data = Locator_Path()
        Status = self.driver.find_element_by_id(self.data.StatusVincentDunn)
        return Status

    def StatusParkview(self):
        self.data = Locator_Path()
        Status = self.driver.find_element_by_id(self.data.StatusParkview)
        return Status

    def StatusGoodSam(self):
        self.data = Locator_Path()
        Status = self.driver.find_element_by_id(self.data.StatusGoodSam)
        return Status

