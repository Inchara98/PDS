import time
import pytest
from Pageobjects_AT.LoginPage import LoginPage
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl1()
    username = ReadConfig.getUserID1()
    password = ReadConfig.getPassword1()
    FakeUsername = ReadConfig.getUser()
    FakePassword = ReadConfig.getpassword()
    Empty = ReadConfig.getEmpty()


    logger =log_Details.logen()


    def test_loginPageTittle(self, setup):
        self.logger.info("***********************Test_001_Login*****************************")
        self.logger.info("********************Test Login Ended********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        time.sleep(5)
        if act_title == "PDS":
            assert True
            self.driver.close()
            self.logger.info("********************Test  Login Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_loginPageTittle.png")
            self.driver.close()
            self.logger.info("********************Test  Login Ended Due to difference in the title********************************")
            assert False

    @pytest.mark.smoke
    def test_login(self, setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(35)
        a = self.driver.current_url
        if a == "https://uat-pds-bi-automationtool.pdsnew.com/reports":
            assert True
            self.logger.info("********************Test  Login Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Login.png")
            self.logger.info("********************Login Test passed********************************")
            assert False
        self.driver.close()
        self.logger.info("********************Login Test passed********************************")

    def test_login1(self, setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPasswordFake(self.FakePassword)
        self.lp.clickLogin()
        time.sleep(35)
        D = "Incorrect Username/ Password. Please try again"
        if D in self.driver.page_source:
            assert True
            self.logger.info("********************Test  Login Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Login.png")
            self.logger.info("********************Login Test passed********************************")
            assert False
        self.driver.close()
        self.logger.info("********************Login Test passed********************************")

    def test_login2(self, setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserNameFake(self.FakeUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(35)
        D = "Incorrect Username/ Password. Please try again"
        if D in self.driver.page_source:
            assert True
            self.logger.info("********************Test  Login Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Login.png")
            self.logger.info("********************Login Test passed********************************")
            assert False
        self.driver.close()
        self.logger.info("********************Login Test passed********************************")

    def test_login3(self, setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.EmptyPassword(self.Empty)
        self.lp.clickLogin()
        time.sleep(35)
        D = "Please Enter Username/ Password. Please try again"
        if D in self.driver.page_source:
            assert True
            self.logger.info("********************Test  Login Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Login.png")
            self.logger.info("********************Login Test passed********************************")
            assert False
        self.driver.close()
        self.logger.info("********************Login Test ended********************************")

    def test_login4(self, setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.EmptyUsername(self.Empty)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(35)
        D = "Please Enter Username/ Password. Please try again"
        if D in self.driver.page_source:
            assert True
            self.logger.info("********************Test  Login Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Login.png")
            self.logger.info("********************Login Test passed********************************")
            assert False
        self.driver.close()
        self.logger.info("********************Login Test ended********************************")

    def test_login5(self, setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.EmptyUsername(self.Empty)
        self.lp.EmptyPassword(self.Empty)
        self.lp.clickLogin()
        time.sleep(35)
        D = "Please Enter Username/ Password. Please try again"
        if D in self.driver.page_source:
            assert True
            self.logger.info("********************Test  Login Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Login.png")
            self.logger.info("********************Login Test passed********************************")
            assert False
        self.driver.close()
        self.logger.info("********************Login Test ended********************************")
