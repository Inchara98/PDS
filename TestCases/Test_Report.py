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

    def test_ReportPage_Community(self, setup):
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
        choose_files = self.rp.choosefilesCommunity()
        choose_files.sendkeys(self.Community)
        submit = self.rp.SubmitCommunity()
        if submit.is_enabled():
            assert True
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ReportPage_Community.png")
            self.logger.info("********************ChooseFile Test passed********************************")
            assert False


    def test_Community_Submit(self, setup):
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
        choose_files = self.rp.choosefilesCommunity()
        choose_files.sendkeys(self.Community)
        self.rp.SubmitCommunity().click()
        Execute_Button = self.rp.ExecuteButtonCommunity()
        if Execute_Button.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Community_Submit.png")
            self.logger.info("********************Submit Test passed********************************")
            assert False

    def test_Community_ExecuteButton(self, setup):
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
        choose_files = self.rp.choosefilesCommunity()
        choose_files.sendkeys(self.Community)
        self.rp.SubmitCommunity().click()
        time.sleep(5)
        self.rp.ExecuteButtonCommunity().click()
        time.sleep(15)
        Status = self.rp.Status()
        if Status is 100:
            assert True
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
        time.sleep(5)
        self.driver.maximize_window()
        self.rp = ReportPage(self.driver)
        time.sleep(3)
        choose_files = self.rp.choosefilesCommunity()
        choose_files.sendkeys(self.Community)
        self.rp.SubmitCommunity().click()
        time.sleep(5)
        self.rp.ExecuteButtonCommunity().click()
        time.sleep(15)
        Status = self.rp.Status()
        if Status is 100:
            self.rp.DownloadCommunity().click()
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Community_DownloadButton.png")
            self.logger.info("********************ExecuteButton Test passed********************************")
            assert False

    def test_ReportPage_Deaconess(self, setup):
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
        choose_files = self.rp.choosefilesDeaconess()
        choose_files.sendkeys(self.Deaconess)
        submit = self.rp.SubmitDeaconess()
        if submit.is_enabled():
            assert True
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ReportPage_Deaconess.png")
            self.logger.info("********************ChooseFile Test passed********************************")
            assert False

    def test_Deaconess_Submit(self, setup):
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
        Execute_Button = self.rp.ExecuteButtonDeaconess()
        if Execute_Button.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Community_Submit.png")
            self.logger.info("********************Submit Test passed********************************")
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
        Status = self.rp.Status()
        if Status is 100:
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Community_ExecuteButton.png")
            self.logger.info("********************ExecuteButton Test passed********************************")
            assert False


    def test_Deaconess_DownloadButton(self, setup):
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
        Status = self.rp.Status()
        if Status is 100:
            self.rp.DownloadDeaconess().click()
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Community_DownloadButton.png")
            self.logger.info("********************ExecuteButton Test passed********************************")
            assert False

    def test_ReportPage_WomensHospital(self, setup):
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
        choose_files = self.rp.choosefilesWomenshsptl()
        choose_files.sendkeys(self.womens_Hospital)
        submit = self.rp.SubmitWomenshsptl()
        if submit.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ReportPage_WomensHospital.png")
            self.logger.info("********************ChooseFile Test passed********************************")
            assert False

    def test_WomensHospital_Submit(self, setup):
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.womens_Hospital)
        self.rp.Submit().click()
        Execute_Button = self.rp.ExecuteButtonWomenshsptl()
        if Execute_Button.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_WomensHospital_Submit.png")
            self.logger.info("********************Submit Test passed********************************")
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
        choose_files = self.rp.choosefilesWomenshsptl()
        choose_files.sendkeys(self.womens_Hospital)
        self.rp.SubmitWomenshsptl().click()
        time.sleep(5)
        self.rp.ExecuteButtonWomenshsptl().click()
        time.sleep(15)
        Status = self.rp.Status()
        if Status is 100:
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_WomensHospital_ExecuteButton.png")
            self.logger.info("********************ExecuteButton Test passed********************************")
            assert False


    def test_WomensHospital_DownloadButton(self, setup):
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
        choose_files = self.rp.choosefilesWomenshsptl()
        choose_files.sendkeys(self.womens_Hospital)
        self.rp.SubmitWomenshsptl().click()
        time.sleep(5)
        self.rp.ExecuteButtonWomenshsptl().click()
        time.sleep(15)
        Status = self.rp.Status()
        if Status is 100:
            self.rp.DownloadWomenshsptl().click()
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_WomensHospital_DownloadButton.png")
            self.logger.info("********************ExecuteButton Test passed********************************")
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
        choose_files = self.rp.choosefilesVinecnt()
        choose_files.sendkeys(self.St_Vincent)
        submit = self.rp.SubmitVincent()
        if submit.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ReportPage_St_Vincent.png")
            self.logger.info("********************ChooseFile Test passed********************************")
            assert False


    def test_St_Vincent_Submit(self, setup):
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
        choose_files = self.rp.choosefilesVinecnt()
        choose_files.sendkeys(self.St_Vincent)
        self.rp.SubmitVincent().click()
        Execute_Button = self.rp.ExecuteButtonVincent()
        if Execute_Button.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_St_Vincent_Submit.png")
            self.logger.info("********************Submit Test passed********************************")
            assert False

    def test_St_Vincent_ExecuteButton(self, setup):
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
        choose_files = self.rp.choosefilesVinecnt()
        choose_files.sendkeys(self.St_Vincent)
        self.rp.SubmitVincent().click()
        time.sleep(5)
        self.rp.ExecuteButtonVincent().click()
        time.sleep(15)
        Status = self.rp.Status()
        if Status is 100:
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_St_Vincent_ExecuteButton.png")
            self.logger.info("********************ExecuteButton Test passed********************************")
            assert False

    def test_St_Vincent_DownloadButton(self, setup):
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
        choose_files = self.rp.choosefilesVinecnt()
        choose_files.sendkeys(self.St_Vincent)
        self.rp.SubmitVincent().click()
        time.sleep(5)
        self.rp.ExecuteButtonVincent().click()
        time.sleep(15)
        Status = self.rp.Status()
        if Status is 100:
            self.rp.DownloadVincent().click()
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_St_Vincent_DownloadButton.png")
            self.logger.info("********************DownloadButton Test Ended********************************")
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
        choose_files = self.rp.choosefilesVincentDunniles()
        choose_files.sendkeys(self.St_Vincent_Dunn)
        submit = self.rp.SubmitVincentDunn()
        if submit.is_enabled():
            assert True
            self.logger.info("********************ChooseFile Test passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ReportPage_St_Vincent_dunn.png")
            self.logger.info("********************ChooseFile Test Ended********************************")
            assert False

    def test_St_Vincent_Dunn_Submit(self, setup):
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
        Execute_Button = self.rp.ExecuteButtonVincentDunn()
        if Execute_Button.is_enabled():
            assert True
            self.logger.info("********************Submit Test passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_St_Vincent_Dunn_Submit.png")
            self.logger.info("********************Submit Test Ended********************************")
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
        Status = self.rp.Status()
        if Status is 100:
            assert True
            self.logger.info("********************ExecuteButton Test passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_St_Vincent_Dunn_ExecuteButton.png")
            self.logger.info("********************ExecuteButton Test Ended********************************")
            assert False

    def test_St_Vincent_Dunn_DownloadButton(self, setup):
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
        Status = self.rp.Status()
        if Status is 100:
            self.rp.DownloadVincentDunn().click()
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_St_Vincent_DownloadButton.png")
            self.logger.info("********************ExecuteButton Test passed********************************")
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
        submit = self.rp.SubmitParkView()
        if submit.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ReportPage_Park_view.png")
            self.logger.info("********************ChooseFile Test passed********************************")
            assert False

    def test_Park_view_Submit(self, setup):
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
        choose_files = self.rp.choosefilesParkview()
        choose_files.sendkeys(self.Park_view)
        self.rp.SubmitParkView().click()
        Execute_Button = self.rp.ExecuteButtonParkview()
        if Execute_Button.is_enabled():
            assert True
            self.logger.info("********************Submit Test passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Park_view_Submit.png")
            self.logger.info("********************Submit Test Ended********************************")
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
        Status = self.rp.Status()
        if Status is 100:
            assert True
            self.logger.info("********************ExecuteButton Test passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Park_view_ExecuteButton.png")
            self.logger.info("********************ExecuteButton Test Ended********************************")
            assert False

    def test_Park_view_DownloadButton(self, setup):
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
        choose_files = self.rp.choosefilesParkview()
        choose_files.sendkeys(self.Park_view)
        self.rp.SubmitParkView().click()
        time.sleep(5)
        self.rp.ExecuteButtonParkview().click()
        time.sleep(15)
        Status = self.rp.Status()
        if Status is 100:
            self.rp.DownloadParkview().click()
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Park_view_DownloadButton.png")
            self.logger.info("********************DownloadButton Test Ended********************************")
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
        submit = self.rp.SubmitGoodSam()
        if submit.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ReportPage_Park_view.png")
            self.logger.info("********************ChooseFile Test passed********************************")
            assert False

    def test_GoodSam_Submit(self, setup):
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
        choose_files = self.rp.choosefileGoodsamFam()
        choose_files.sendkeys(self.GoodSam)
        self.rp.SubmitGoodSam().click()
        Execute_Button = self.rp.ExecuteButtonGoodSam()
        if Execute_Button.is_enabled():
            assert True
            self.logger.info("********************Submit Test passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Park_view_Submit.png")
            self.logger.info("********************Submit Test Ended********************************")
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
        Status = self.rp.Status()
        if Status is 100:
            assert True
            self.logger.info("********************ExecuteButton Test passed********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Park_view_ExecuteButton.png")
            self.logger.info("********************ExecuteButton Test Ended********************************")
            assert False

    def test_GoodSam_DownloadButton(self, setup):
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
        choose_files = self.rp.choosefileGoodsamFam()
        choose_files.sendkeys(self.GoodSam)
        self.rp.SubmitGoodSam().click()
        time.sleep(5)
        self.rp.ExecuteButtonGoodSam().click()
        time.sleep(15)
        Status = self.rp.Status()
        if Status is 100:
            self.rp.GoodSam().click()
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_GoodSam_DownloadButton.png")
            self.logger.info("********************DownloadButton Test Ended********************************")
            assert False
