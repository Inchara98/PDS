import time

from Pageobjects_AT.LoginPage import LoginPage
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig
from Pageobjects_AT.BookToFacs import BookToFacs

class Test_001_Report:
    baseUrl = ReadConfig.getApplicationUrl1()
    username = ReadConfig.getUserID1()
    password = ReadConfig.getPassword1()
    BookToFacs = ReadConfig.get_BookToFacs_FilePath()



    logger = log_Details.logen()

    def test_BookToFacs(self,setup):
        self.logger.info("********************verifying ChooseFile Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.close()
        self.BK = BookToFacs(self.driver)
        self.BK.BookToFacs()
        choosefiles = self.BK.Choosefile_BK()
        choosefiles.send_keys(self.BookToFacs)
        submit = self.driver.find_element_by_id("")
        if submit.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_BookToFacs.png")
            self.logger.info("********************ChooseFile Test passed********************************")
            assert False

    def test_Submit(self,setup):
        self.logger.info("********************verifying SubmitButton Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.close()
        self.BK = BookToFacs(self.driver)
        self.BK.BookToFacs()
        choosefiles = self.BK.Choosefiles()
        choosefiles.send_keys(self.BookToFacs)
        self.BK.Submit().click()
        Execute_Button = self.BK.ExecuteButton()
        if Execute_Button.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Submit.png")
            self.logger.info("********************Submit Test passed********************************")
            assert False


    def test_Download(self,setup):
        self.logger.info("********************verifying DownloadButton Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.close()
        self.BK = BookToFacs(self.driver)
        self.BK.BookToFacs()
        choosefiles = self.BK.Choosefiles()
        choosefiles.send_keys(self.BookToFacs)
        self.BK.Submit().click()
        self.BK.Download_BK().click()

            