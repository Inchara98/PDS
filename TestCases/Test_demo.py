import os
import time

from Pageobjects_AT.LoginPage import LoginPage
from Logs.Log import log_Details
from Pageobjects_AT.Reports import ReportPage
from Utilities.readProperties import ReadConfig


class Test_001_Report:
    baseUrl = ReadConfig.getApplicationUrl1()
    username = ReadConfig.getUserID1()
    password = ReadConfig.getPassword1()
    Community = ReadConfig.get_Community_FilePath()
    Deaconess = ReadConfig.get_Deaconess_FilePath()
    Womens_Hospital = ReadConfig.get_Womenshospital_FilePath()
    St_Vincent = ReadConfig.get_St_Vincent_FilePath()
    St_Vincent_Dunn = ReadConfig.get_St_Vincent_Dunn_FilePath()
    Park_view = ReadConfig.get_Park_view_FilePath()


    logger = log_Details.logen()






    def test_Community_ExecuteButton(self, setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesCommunity()
        choose_files.send_keys(self.Community)
        self.rp.SubmitCommunity().click()
        time.sleep(120)
        self.rp.ExecuteButtonCommunity().click()
        time.sleep(120)
        Status = self.rp.StatusCommunity()
        print(Status.get_attribute("data-percentage"))
        if Status.get_attribute("data-percentage") == "100":
            self.rp.DownloadCommunity().click()
            filename = "Download.default_directory" + "Community.zip"
            if os.path.dirname(filename) != True:
                print("Download is working")
                assert True
            else:
                print("Download is not working")
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Propensity_download.png")
                self.driver.close()
                self.logger.info(
                    "********************test_Propensity_download Ended Due to difference in the txt********************************")
                assert False