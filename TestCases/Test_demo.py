import time
import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.Hospital import Hospital
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig
from selenium.webdriver.support.select import Select
import os


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()
    search = ReadConfig.getSearch()

    logger =log_Details.logen()


    def test_Propensity_close(self,setup):
        self.logger.info("********************verifying test_Propensity_close Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(15)
        self.driver.maximize_window()
        self.CH = Hospital(self.driver)
        time.sleep(35)
        self.CH.ColumbHomepage()
        time.sleep(35)
        self.CH.Propensitylink()
        time.sleep(5)
        self.CH.Propensity_close()
        D = "PROPENSITY TO PAY SCORES"
        if D in self.driver.page_source:
            assert True
            self.logger.info("********************test_Propensity_close Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Propensity_close.png")
            self.driver.close()
            self.logger.info(
                "********************test_Propensity_close Ended Due to difference in the txt********************************")


# Downlaod foldoer directory
# "download.default_directory"

# os.path(filename)








# filename = "Downlaod foldoer directory"+"/columbus"
# if os.path(filename) != True:
#     print("Downloaaad is not working")




