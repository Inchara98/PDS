import time
import pytest
from Pageobjects_AT.Homepage import Homepage
from Pageobjects_AT.LoginPage import LoginPage
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig


class Test_001_Homepage:
    baseUrl = ReadConfig.getApplicationUrl1()
    username = ReadConfig.getUserID1()
    password = ReadConfig.getPassword1()

    logger =log_Details.logen()

    @pytest.mark.smoke
    def test_Homepage(self,setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(35)
        self.driver.maximize_window()
        self.hp = Homepage(self.driver)
        time.sleep(3)
        a = self.driver.current_url
        if a == "https://uat-pds-bi-automationtool.pdsnew.com/reports":
            assert True
            self.logger.info("********************Test  Homepage Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_HomepagePage.png")
            self.logger.info("********************Login Test passed********************************")
            assert False

    @pytest.mark.smoke
    def test_Book_to_Facs(self,setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(35)
        self.driver.maximize_window()
        self.hp = Homepage(self.driver)
        time.sleep(3)
        self.hp.clickBooktoFacs()
        time.sleep(3)
        c = self.driver.current_url
        if c == "https://uat-pds-bi-automationtool.pdsnew.com/reports/Book_To_Facs":
            assert True
            self.logger.info("********************Test Book_To_Facs Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Book_To_Facs.png")
            self.logger.info("********************Book_To_Facs Test passed********************************")
            assert False

    @pytest.mark.smoke
    def test_Weekly_Reports(self,setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(35)
        self.driver.maximize_window()
        self.hp = Homepage(self.driver)
        time.sleep(6)
        self.hp.clickBooktoFacs()
        time.sleep(8)
        c = self.driver.current_url
        if c == "https://uat-pds-bi-automationtool.pdsnew.com/reports/Weekly_Reports":
            assert True
            self.logger.info("********************Test Weekly_Reports Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Weekly_Reports.png")
            self.logger.info("********************Weekly_Reports Test passed********************************")
            assert False


    def test_Filemanager(self,setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(35)
        self.driver.maximize_window()
        self.hp = Homepage(self.driver)
        time.sleep(6)
        self.hp.clickFilemanager()
        time.sleep(8)
        b = self.driver.current_url
        if b == "https://uat-pds-bi-automationtool.pdsnew.com/fileslist":
            assert True
            self.logger.info("********************Test File_Manager_page Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Filemanager.png")
            self.logger.info("********************Filemanager Test passed********************************")
            assert False

    @pytest.mark.smoke
    def test_Exception_Report(self,setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(35)
        self.driver.maximize_window()
        self.hp = Homepage(self.driver)
        time.sleep(6)
        self.hp.clickExceptionReport()
        time.sleep(8)
        b = self.driver.current_url
        if b == "https://uat-pds-bi-automationtool.pdsnew.com/exceptionReport":
            assert True
            self.logger.info("********************Test File_Manager_page Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Exception_Report.png")
            self.logger.info("********************ExceptionReport Test passed********************************")
            assert False

    @pytest.mark.smoke
    def test_logout(self,setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(35)
        self.driver.maximize_window()
        self.hp = Homepage(self.driver)
        time.sleep(6)
        self.hp.clicklogout()
        time.sleep(8)
        act_title = self.driver.title
        time.sleep(5)
        if act_title == "PDS":
            assert True
            self.driver.close()
            self.logger.info("********************Test  Logout Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_logout.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Logout Ended Due to difference in the title********************************")
            assert False

