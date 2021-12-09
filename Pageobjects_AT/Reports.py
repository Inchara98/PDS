import time

from selenium.webdriver import ActionChains

from Locators.Locators import Locator_Path

class ReportPage:

    def __init__(self,driver):
        self.driver = driver

    def choosefilesCommunity(self):
        self.data = Locator_Path()
        file = self.driver.find_element_by_xpath(self.data.choosefilescommunity)
        return file

    def choosefilesDeaconess(self):
        self.data = Locator_Path()
        file = self.driver.find_element_by_id(self.data.choosefilesDeaconess)
        return file

    def choosefilesWomenshospital(self):
        self.data = Locator_Path()
        file = self.driver.find_element_by_id(self.data.choosefilesWomenshospital)
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
        a = self.driver.find_element_by_id(self.data.SubmitCommunity)
        return a

    def SubmitDeaconess(self):
        self.data = Locator_Path()
        a = self.driver.find_element_by_id(self.data.SubmitDeaconess)
        return a

    def SubmitWomensHospital(self):
        self.data = Locator_Path()
        a = self.driver.find_element_by_id(self.data.SubmitWomensHospital)
        return a


    def SubmitVincent(self):
        self.data = Locator_Path()
        a = self.driver.find_element_by_id(self.data.SubmitVincent)
        return a

    def SubmitVincentDunn(self):
        self.data = Locator_Path()
        a = self.driver.find_element_by_id(self.data.SubmitVincentDunn)
        return a


    def SubmitGoodSam(self):
        self.data = Locator_Path()
        a = self.driver.find_element_by_id(self.data.SubmitGoodSam)
        return a


    def SubmitParkView(self):
        self.data = Locator_Path()
        a = self.driver.find_element_by_id(self.data.SubmitParkView)
        return a

    def ExecuteButtonCommunity(self):
        self.data = Locator_Path()
        Execute_Button = self.driver.find_element_by_id(self.data.ExecuteButtonCommunity)
        return Execute_Button

    def ExecuteButtonDeaconess(self):
        self.data = Locator_Path()
        Execute_Button = self.driver.find_element_by_id(self.data.ExecuteButtonDeaconess)
        return Execute_Button

    def ExecuteButtonWomenshospital(self):
        self.data = Locator_Path()
        Execute_Button = self.driver.find_element_by_id(self.data.ExecuteButtonWomenshospital)
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

    def StatusWomenshospital(self):
        self.data = Locator_Path()
        Status = self.driver.find_element_by_id(self.data.StatusWomenshospital)
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

    def DownloadCommunity(self):
        self.data = Locator_Path()
        Download = self.driver.find_element_by_id(self.data.DownloadCommunity)
        return Download

    def DownloadDeaconess(self):
        self.data = Locator_Path()
        Download = self.driver.find_element_by_name(self.data.DownloadDeaconess)
        return Download

    def DownloadWomenshospital(self):
        self.data = Locator_Path()
        Download = self.driver.find_element_by_name(self.data.DownloadWomenshospital)
        return Download

    def DownloadVincent(self):
        self.data = Locator_Path()
        Download = self.driver.find_element_by_name(self.data.DownloadVincent)
        return Download

    def DownloadVincentDunn(self):
        self.data = Locator_Path()
        Download = self.driver.find_element_by_name(self.data.DownloadVincentDunn)
        return Download

    def DownloadParkview(self):
        self.data = Locator_Path()
        Download = self.driver.find_element_by_name(self.data.DownloadParkview)
        return Download

    def DownloadGoodSam(self):
        self.data = Locator_Path()
        Download = self.driver.find_element_by_name(self.data.DownloadGoodSam)
        return Download

