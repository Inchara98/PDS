import time

from PageObjects.LoginPage import LoginPage
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()

    logger =log_Details.logen()

    def test_ColumbHomepage(self,setup):
        self.logger.info("********************verifying Homepage Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = ColumbHosptal(self.driver)
        time.sleep(3)
        self.CH.ColumbHomepage()
        a = self.driver.current_url
        if a == "https://pds-billing-info.tibilprojects.com/dashboard/COLUMB":
            assert True
            self.logger.info("********************Test  ColumbHomepage Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ColumbHomepage.png")
            self.logger.info("********************ColumbHomepage Test ended********************************")
            assert False
            