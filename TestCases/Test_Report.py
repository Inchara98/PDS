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
    womens_Hospital = ReadConfig.get_Womenshospital_FilePath()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.Community)
        submit = self.driver.find_element_by_id("")
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.Community)
        self.rp.Submit().click()
        Execute_Button = self.rp.ExecuteButton()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.Community)
        self.rp.Submit().click()
        time.sleep(5)
        self.rp.ExecuteButton().click()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.Community)
        self.rp.Submit().click()
        time.sleep(5)
        self.rp.ExecuteButton().click()
        time.sleep(15)
        Status = self.rp.Status()
        if Status is 100:
            self.driver.find_element_by_id("").click()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.Deaconess)
        submit = self.driver.find_element_by_id("")
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.Deaconess)
        self.rp.Submit().click()
        Execute_Button = self.rp.ExecuteButton()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.Deaconess)
        self.rp.Submit().click()
        time.sleep(5)
        self.rp.ExecuteButton().click()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.Deaconess)
        self.rp.Submit().click()
        time.sleep(5)
        self.rp.ExecuteButton().click()
        time.sleep(15)
        Status = self.rp.Status()
        if Status is 100:
            self.driver.find_element_by_id("").click()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.womens_Hospital)
        submit = self.driver.find_element_by_id("")
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
        Execute_Button = self.rp.ExecuteButton()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.womens_Hospital)
        self.rp.Submit().click()
        time.sleep(5)
        self.rp.ExecuteButton().click()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.womens_Hospital)
        self.rp.Submit().click()
        time.sleep(5)
        self.rp.ExecuteButton().click()
        time.sleep(15)
        Status = self.rp.Status()
        if Status is 100:
            self.driver.find_element_by_id("").click()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.St_Vincent)
        submit = self.driver.find_element_by_id("")
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.St_Vincent)
        self.rp.Submit().click()
        Execute_Button = self.rp.ExecuteButton()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.St_Vincent)
        self.rp.Submit().click()
        time.sleep(5)
        self.rp.ExecuteButton().click()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.St_Vincent)
        self.rp.Submit().click()
        time.sleep(5)
        self.rp.ExecuteButton().click()
        time.sleep(15)
        Status = self.rp.Status()
        if Status is 100:
            self.driver.find_element_by_id("").click()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.St_Vincent_Dunn)
        submit = self.driver.find_element_by_id("")
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.St_Vincent_Dunn)
        self.rp.Submit().click()
        Execute_Button = self.rp.ExecuteButton()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.St_Vincent_Dunn)
        self.rp.Submit().click()
        time.sleep(5)
        self.rp.ExecuteButton().click()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.St_Vincent_Dunn)
        self.rp.Submit().click()
        time.sleep(5)
        self.rp.ExecuteButton().click()
        time.sleep(15)
        Status = self.rp.Status()
        if Status is 100:
            self.driver.find_element_by_id("").click()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.Park_view)
        submit = self.driver.find_element_by_id("")
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.Park_view)
        self.rp.Submit().click()
        Execute_Button = self.rp.ExecuteButton()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.Park_view)
        self.rp.Submit().click()
        time.sleep(5)
        self.rp.ExecuteButton().click()
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
        choose_files = self.rp.choosefiles()
        choose_files.sendkeys(self.Park_view)
        self.rp.Submit().click()
        time.sleep(5)
        self.rp.ExecuteButton().click()
        time.sleep(15)
        Status = self.rp.Status()
        if Status is 100:
            self.driver.find_element_by_id("").click()
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Park_view_DownloadButton.png")
            self.logger.info("********************DownloadButton Test Ended********************************")
            assert False

