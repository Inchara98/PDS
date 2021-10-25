import time
import pytest
from PageObjects.LoginPage import LoginPage
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()

    logger =log_Details.logen()


    # def test_loginPageTittle(self, setup):
    #     self.logger.info("***********************Test_001_Login*****************************")
    #     self.logger.info("********************Test Login Ended********************************")
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     act_title = self.driver.title
    #     time.sleep(5)
    #     if act_title == "PDS":
    #         assert True
    #         self.driver.close()
    #         self.logger.info("********************Test  Login Ended********************************")
    #     else:
    #         self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_loginPageTittle.png")
    #         self.driver.close()
    #         self.logger.info("********************Test  Login Ended Due to difference in the title********************************")
    #         assert False



    # @pytest.mark.smoke
    # def test_login(self,setup):
    #     self.logger.info("********************verifying Login Test********************************")
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     time.sleep(5)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUserName(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #     self.driver.close()
    #     self.logger.info("********************Login Test passed********************************")

    # @pytest.mark.smoke
    # def test_login(self,setup):
    #     self.driver = setup
    #     self.logger.info("********************verifying Login Test******************************")
    #     a = ReadConfig()
    #     a.login_to_PDS_Billing_Application(self)
    #     time.sleep(10)
    #     self.driver.close()
    #     self.logger.info("********************Login Test passed********************************")



    def test_login_to_pds_application(self,driver):
        self.driver = driver
        data = ReadConfig(self.driver)
        # self.driver= data.get_driver()
        data.login_to_PDS_Billing_Application()







