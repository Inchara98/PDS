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
    GoodSam = ReadConfig.get_GoodSam_FilePath()


    logger = log_Details.logen()



    def test_ReportPage_Community(self, setup):
        self.logger.info("********************verifying test_ReportPage_Community Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(20)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesCommunity()
        choose_files.send_keys(self.Community)
        time.sleep(20)
        submit = self.rp.SubmitCommunity().is_enabled()
        if submit == True:
            assert True
            self.logger.info("********************test_ReportPage_Community Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ReportPage_Community.png")
            self.logger.info(
                "********************test_ReportPage_Community Test passed********************************")
            assert False



    def test_Community_Submit(self, setup):
        self.logger.info("********************verifying test_Community_Submit Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(15)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesCommunity()
        choose_files.send_keys(self.Community)
        time.sleep(15)
        self.rp.SubmitCommunity().click()
        time.sleep(120)
        Execute_Button = self.rp.ExecuteButtonCommunity()
        if Execute_Button.get_attribute("class") == "execute-color-change-after":
            assert True
            self.logger.info("********************test_Community_Submit Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Community_Submit.png")
            self.logger.info("********************test_Community_Submit Test passed********************************")
            assert False


    def test_Community_ExecuteButton(self, setup):
        self.logger.info("********************verifying test_Community_ExecuteButton Test********************************")
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
        if Status.get_attribute("data-percentage") == "100":
            assert True
            self.logger.info("********************test_Community_ExecuteButton Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Community_ExecuteButton.png")
            self.logger.info("********************ExecuteButton Test passed********************************")
            assert False



    def test_Community_DownloadButton(self, setup):
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
        if Status.get_attribute("data-percentage") == "100":
            self.rp.DownloadCommunity().click()
            time.sleep(120)
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



    def test_ReportPage_Deaconess(self, setup):
        self.logger.info("********************verifying test_ReportPage_Deaconess Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(15)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesDeaconess()
        choose_files.send_keys(self.Deaconess)
        submit = self.rp.SubmitDeaconess().is_enabled()
        time.sleep(20)
        if submit == True:
            assert True
            self.logger.info("********************test_ReportPage_Deaconess Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ReportPage_Deaconess.png")
            self.logger.info("********************ChooseFile Test passed********************************")
            assert False


    def test_Deaconess_Submit(self, setup):
        self.logger.info("********************verifying test_Deaconess_Submit Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesDeaconess()
        choose_files.sendkeys(self.Deaconess)
        self.rp.SubmitDeaconess().click()
        time.sleep(120)
        Execute_Button = self.rp.ExecuteButtonDeaconess()
        if Execute_Button.get_attribute("class") == "execute-color-change-after":
            assert True
            self.logger.info("********************test_Deaconess_Submit Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Community_Submit.png")
            self.logger.info("********************test_Deaconess_Submit Test passed********************************")
            assert False



    def test_Deaconess_ExecuteButton(self, setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesDeaconess()
        choose_files.sendkeys(self.Deaconess)
        self.rp.SubmitDeaconess().click()
        time.sleep(5)
        self.rp.ExecuteButtonDeaconess().click()
        time.sleep(15)
        Status = self.rp.StatusDeaconess()
        time.sleep(120)
        if Status.get_attribute("data-percentage") == "100":
            assert True
            self.logger.info("********************test_Community_ExecuteButton Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Community_ExecuteButton.png")
            self.logger.info("********************ExecuteButton Test passed********************************")
            assert False


    def test_Deaconess_DownloadButton(self, setup):
        self.logger.info("********************verifying test_Deaconess_DownloadButton ********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesDeaconess()
        choose_files.sendkeys(self.Deaconess)
        self.rp.SubmitDeaconess().click()
        time.sleep(5)
        self.rp.ExecuteButtonDeaconess().click()
        time.sleep(15)
        Status = self.rp.StatusDeaconess()
        if Status.get_attribute("data-percentage") == "100":
            self.rp.DownloadDeaconess().click()
            time.sleep(120)
            filename = "Download.default_directory" + "Community.zip"
            if os.path.dirname(filename) != True:
                print("Download is working")
                assert True
            else:
                print("Download is not working")
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Deaconess_DownloadButton.png")
                self.driver.close()
                self.logger.info(
                    "********************test_Deaconess_DownloadButton Ended Due to difference in the txt********************************")
                assert False


    def test_ReportPage_WomensHospital(self, setup):
        self.logger.info("********************verifying test_ReportPage_WomensHospital Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesWomenshospital()
        choose_files.sendkeys(self.Womens_Hospital)
        submit = self.rp.SubmitWomensHospital().is_enabled()
        time.sleep(20)
        if submit == True:
            assert True
            self.logger.info("********************test_ReportPage_WomensHospital Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ReportPage_WomensHospital.png")
            self.logger.info("********************test_ReportPage_WomensHospital Test passed********************************")
            assert False


    def test_WomensHospital_Submit(self, setup):
        self.logger.info("********************verifying test_WomensHospital_Submit ********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesWomenshospital()
        choose_files.sendkeys(self.Womens_Hospital)
        self.rp.SubmitWomensHospital().click()
        time.sleep(120)
        Execute_Button = self.rp.ExecuteButtonWomenshospital()
        if Execute_Button.get_attribute("class") == "execute-color-change-after":
            assert True
            self.logger.info("********************test_St_Vincent_Submit Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_St_Vincent_Submit.png")
            self.logger.info(
                "********************test_St_Vincent_Submit Test passed********************************")
            assert False



    def test_WomensHospital_ExecuteButton(self, setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesWomenshospital()
        choose_files.sendkeys(self.Womens_Hospital)
        self.rp.SubmitWomensHospital().click()
        time.sleep(5)
        self.rp.ExecuteButtonWomenshospital().click()
        time.sleep(15)
        Status = self.rp.StatusWomenshospital()
        if Status.get_attribute("data-percentage") == "100":
            assert True
            self.logger.info("********************test_Community_ExecuteButton Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Community_ExecuteButton.png")
            self.logger.info("********************ExecuteButton Test passed********************************")
            assert False



    def test_WomensHospital_DownloadButton(self, setup):
        self.logger.info("********************verifying test_WomensHospital_DownloadButton********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesWomenshospital()
        choose_files.sendkeys(self.Womens_Hospital)
        self.rp.SubmitWomensHospital().click()
        time.sleep(5)
        self.rp.ExecuteButtonWomenshospital().click()
        time.sleep(15)
        Status = self.rp.StatusWomenshospital()
        if Status.get_attribute("data-percentage") == "100":
            self.rp.DownloadCommunity().click()
            time.sleep(120)
            filename = "Download.default_directory" + "Community.zip"
            if os.path.dirname(filename) != True:
                print("Download is working")
                assert True
            else:
                print("Download is not working")
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_WomensHospital_DownloadButton.png")
                self.driver.close()
                self.logger.info(
                    "********************test_WomensHospital_DownloadButton Ended Due to difference in the txt********************************")
                assert False




    def test_ReportPage_St_Vincent(self, setup):
        self.logger.info("********************verifying ChooseFile Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesVincent()
        choose_files.sendkeys(self.St_Vincent)
        submit = self.rp.SubmitVincent().is_enabled()
        time.sleep(20)
        if submit == True:
            assert True
            self.logger.info("********************test_ReportPage_WomensHospital Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ReportPage_WomensHospital.png")
            self.logger.info("********************test_ReportPage_WomensHospital Test passed********************************")
            assert False



    def test_St_Vincent_Submit(self, setup):
        self.logger.info("********************verifying test_St_Vincent_Submit********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesVincent()
        choose_files.sendkeys(self.St_Vincent)
        self.rp.SubmitVincent().click()
        time.sleep(120)
        Execute_Button = self.rp.ExecuteButtonVincent()
        if Execute_Button.get_attribute("class") == "execute-color-change-after":
            assert True
            self.logger.info("********************test_St_Vincent_Submit Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_St_Vincent_Submit.png")
            self.logger.info(
                "********************test_St_Vincent_Submit Test passed********************************")
            assert False



    def test_St_Vincent_ExecuteButton(self, setup):
        self.logger.info("********************verifying test_St_Vincent_ExecuteButton********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesVincent()
        choose_files.sendkeys(self.St_Vincent)
        self.rp.SubmitVincent().click()
        time.sleep(5)
        self.rp.ExecuteButtonVincent().click()
        time.sleep(15)
        Status = self.rp.StatusVincent()
        if Status.get_attribute("data-percentage") == "100":
            assert True
            self.logger.info("********************test_St_Vincent_ExecuteButton Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_St_Vincent_ExecuteButton.png")
            self.logger.info("********************test_St_Vincent_ExecuteButton passed********************************")
            assert False



    def test_St_Vincent_DownloadButton(self, setup):
        self.logger.info("********************verifying test_St_Vincent_DownloadButton********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesVincent()
        choose_files.sendkeys(self.St_Vincent)
        self.rp.SubmitVincent().click()
        time.sleep(5)
        self.rp.ExecuteButtonVincent().click()
        time.sleep(15)
        Status = self.rp.StatusVincent()
        if Status.get_attribute("data-percentage") == "100":
            self.rp.DownloadCommunity().click()
            time.sleep(120)
            filename = "Download.default_directory" + "Community.zip"
            if os.path.dirname(filename) != True:
                print("Download is working")
                assert True
            else:
                print("Download is not working")
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_St_Vincent_DownloadButton.png")
                self.driver.close()
                self.logger.info(
                    "********************test_St_Vincent_DownloadButton Ended Due to difference in the txt********************************")
                assert False



    def test_ReportPage_St_Vincent_dunn(self, setup):
        self.logger.info("********************verifying ChooseFile Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesVincent()
        choose_files.sendkeys(self.St_Vincent_Dunn)
        submit = self.rp.SubmitVincentDunn().is_enabled()
        time.sleep(20)
        if submit == True:
            assert True
            self.logger.info("********************test_ReportPage_WomensHospital Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ReportPage_WomensHospital.png")
            self.logger.info("********************test_ReportPage_WomensHospital Test passed********************************")
            assert False


        
    def test_St_Vincent_Dunn_Submit(self, setup):
        self.logger.info("********************verifying test_St_Vincent_Dunn_Submit********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesVincentDunn()
        choose_files.sendkeys(self.St_Vincent_Dunn)
        self.rp.SubmitVincentDunn().click()
        time.sleep(120)
        Execute_Button = self.rp.ExecuteButtonVincentDunn()
        if Execute_Button.get_attribute("class") == "execute-color-change-after":
            assert True
            self.logger.info("********************test_St_Vincent_Dunn_Submit Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_St_Vincent_Dunn_Submit.png")
            self.logger.info("********************test_St_Vincent_Dunn_Submit Test passed********************************")
            assert False


    def test_St_Vincent_Dunn_ExecuteButton(self, setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesVincentDunn()
        choose_files.sendkeys(self.St_Vincent_Dunn)
        self.rp.SubmitVincentDunn().click()
        time.sleep(5)
        self.rp.ExecuteButtonVincentDunn().click()
        time.sleep(15)
        Status = self.rp.StatusVincentDunn()
        if Status.get_attribute("data-percentage") == "100":
            assert True
            self.logger.info("********************test_St_Vincent_ExecuteButton Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_St_Vincent_ExecuteButton.png")
            self.logger.info("********************test_St_Vincent_ExecuteButton passed********************************")
            assert False



    def test_St_Vincent_Dunn_DownloadButton(self, setup):
        self.logger.info("********************verifying test_St_Vincent_Dunn_DownloadButton********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesVincentDunn()
        choose_files.sendkeys(self.St_Vincent_Dunn)
        self.rp.SubmitVincentDunn().click()
        time.sleep(5)
        self.rp.ExecuteButtonVincentDunn().click()
        time.sleep(15)
        Status = self.rp.StatusVincentDunn()
        if Status.get_attribute("data-percentage") == "100":
            self.rp.DownloadCommunity().click()
            time.sleep(120)
            filename = "Download.default_directory" + "Community.zip"
            if os.path.dirname(filename) != True:
                print("Download is working")
                assert True
            else:
                print("Download is not working")
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_St_Vincent_Dunn_DownloadButton.png")
                self.driver.close()
                self.logger.info(
                    "********************test_St_Vincent_Dunn_DownloadButton Ended Due to difference in the txt********************************")
                assert False



    def test_ReportPage_Park_view(self, setup):
        self.logger.info("********************verifying ChooseFile Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesParkview()
        choose_files.sendkeys(self.Park_view)
        submit = self.rp.SubmitParkView().is_enabled()
        time.sleep(20)
        if submit == True:
            assert True
            self.logger.info("********************test_ReportPage_WomensHospital Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ReportPage_WomensHospital.png")
            self.logger.info("********************test_ReportPage_WomensHospital Test passed********************************")
            assert False


        

    def test_Park_view_Submit(self, setup):
        self.logger.info("********************verifying test_Park_view_Submit********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesParkview()
        choose_files.sendkeys(self.Park_view)
        self.rp.SubmitParkView().click()
        time.sleep(120)
        Execute_Button = self.rp.ExecuteButtonParkview()
        if Execute_Button.get_attribute("class") == "execute-color-change-after":
            assert True
            self.logger.info("********************test_Park_view_Submit Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Park_view_Submit.png")
            self.logger.info("********************test_Park_view_Submit Test passed********************************")
            assert False



    def test_Park_view_ExecuteButton(self, setup):
        self.logger.info("********************verifying ExecuteButton Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesParkview()
        choose_files.sendkeys(self.Park_view)
        self.rp.SubmitParkView().click()
        time.sleep(5)
        self.rp.ExecuteButtonParkview().click()
        time.sleep(15)
        Status = self.rp.StatusParkview()
        if Status.get_attribute("data-percentage") == "100":
            assert True
            self.logger.info("********************test_Park_view_ExecuteButton Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Park_view_ExecuteButton.png")
            self.logger.info("********************test_Park_view_ExecuteButton passed********************************")
            assert False



    def test_Park_view_DownloadButton(self, setup):
        self.logger.info("********************verifying test_Park_view_DownloadButton********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesParkview()
        choose_files.sendkeys(self.Park_view)
        self.rp.SubmitParkView().click()
        time.sleep(5)
        self.rp.ExecuteButtonParkview().click()
        time.sleep(15)
        Status = self.rp.StatusParkview()
        if Status.get_attribute("data-percentage") == "100":
            self.rp.DownloadCommunity().click()
            time.sleep(120)
            filename = "Download.default_directory" + "Community.zip"
            if os.path.dirname(filename) != True:
                print("Download is working")
                assert True
            else:
                print("Download is not working")
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Park_view_DownloadButton.png")
                self.driver.close()
                self.logger.info(
                    "********************test_Park_view_DownloadButton Ended Due to difference in the txt********************************")
                assert False



    def test_ReportPage_GoodSam(self, setup):
        self.logger.info("********************verifying ChooseFile Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefileGoodsamFam()
        choose_files.sendkeys(self.GoodSam)
        submit = self.rp.SubmitGoodSam().is_enabled()
        time.sleep(20)
        if submit == True:
            assert True
            self.logger.info("********************test_ReportPage_GoodSam Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ReportPage_GoodSam.png")
            self.logger.info("********************test_ReportPage_GoodSam Test passed********************************")
            assert False

        

    def test_GoodSam_Submit(self, setup):
        self.logger.info("********************verifying test_GoodSam_Submit ********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.ExecuteButtonGoodSam()
        choose_files.sendkeys(self.GoodSam)
        self.rp.SubmitGoodSam().click()
        time.sleep(120)
        Execute_Button = self.rp.ExecuteButtonCommunity()
        if Execute_Button.get_attribute("class") == "execute-color-change-after":
            assert True
            self.logger.info("********************test_GoodSam_Submit Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_GoodSam_Submit.png")
            self.logger.info("********************test_GoodSam_Submit Test passed********************************")
            assert False



    def test_GoodSam_ExecuteButton(self, setup):
        self.logger.info("********************verifying ExecuteButton Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefileGoodsamFam()
        choose_files.sendkeys(self.GoodSam)
        self.rp.SubmitGoodSam().click()
        time.sleep(5)
        self.rp.ExecuteButtonGoodSam().click()
        time.sleep(15)
        Status = self.rp.StatusGoodSam()
        if Status.get_attribute("data-percentage") == "100":
            assert True
            self.logger.info("********************test_GoodSam_ExecuteButton Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Park_view_ExecuteButton.png")
            self.logger.info("********************test_Park_view_ExecuteButton passed********************************")
            assert False



    def test_GoodSam_DownloadButton(self, setup):
        self.logger.info("********************verifying test_GoodSam_DownloadButton********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefileGoodsamFam()
        choose_files.sendkeys(self.GoodSam)
        self.rp.SubmitGoodSam().click()
        time.sleep(5)
        self.rp.ExecuteButtonGoodSam().click()
        time.sleep(15)
        Status = self.rp.StatusGoodSam()
        if Status.get_attribute("data-percentage") == "100":
            self.rp.DownloadCommunity().click()
            time.sleep(120)
            filename = "Download.default_directory" + "Community.zip"
            if os.path.dirname(filename) != True:
                print("Download is working")
                assert True
            else:
                print("Download is not working")
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_GoodSam_DownloadButton.png")
                self.driver.close()
                self.logger.info(
                    "********************test_GoodSam_DownloadButton Ended Due to difference in the txt********************************")
                assert False
