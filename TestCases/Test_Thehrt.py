
import time

from PageObjects.LoginPage import LoginPage
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig


class Test_ThehrtHospital:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()

    logger =log_Details.logen()

    def test_ThehrtHomepage(self,setup):
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
        if a == "https://pds-billing-info.tibilprojects.com/dashboard/THEHRT":
            assert True
            self.logger.info("********************Test ThehrtHomepage Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ThehrtHomepage.png")
            self.logger.info("********************ThehrtHomepage Test ended********************************")
            assert False

    def test_SelectYear2018(self,setup):
        self.logger.info("********************verifying SelectYear2018 Test********************************")
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
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        a = self.driver.find_element_by_id("").text
        time.sleep(3)
        if a == "Overall Revenue v/s Transactions-2018":
            assert True
            self.driver.close()
            self.logger.info("********************Test  SelectYear2018 Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_SelectYear2018.png")
            self.driver.close()
            self.logger.info(
                "********************Test  SelectYear2018 Ended Due to difference in the txt********************************")
            assert False

    def test_SelectYear2019(self,setup):
        self.logger.info("********************verifying SelectYear2019 Test********************************")
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
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(2)
        a = self.driver.find_element_by_id("").text
        time.sleep(3)
        if a == "Overall Revenue v/s Transactions-2018":
            assert True
            self.driver.close()
            self.logger.info("********************Test  SelectYear Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_SelectYear.png")
            self.driver.close()
            self.logger.info(
                "********************Test  SelectYear Ended Due to difference in the txt********************************")
            assert False


    def test_SelectYear2020(self,setup):
        self.logger.info("********************verifying SelectYear2020 Test********************************")
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
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(3)
        a = self.driver.find_element_by_id("").text
        time.sleep(3)
        if a == "Overall Revenue v/s Transactions-2018":
            assert True
            self.driver.close()
            self.logger.info("********************Test  SelectYear Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_SelectYear.png")
            self.driver.close()
            self.logger.info(
                "********************Test  SelectYear Ended Due to difference in the txt********************************")
            assert False


    def test_SelectYear2021(self,setup):
        self.logger.info("********************verifying SelectYear2021 Test********************************")
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
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(4)
        a = self.driver.find_element_by_id("").text
        time.sleep(3)
        if a == "Overall Revenue v/s Transactions-2018":
            assert True
            self.driver.close()
            self.logger.info("********************Test  SelectYear2021 Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_SelectYear2021.png")
            self.driver.close()
            self.logger.info(
                "********************Test  SelectYear2021 Ended Due to difference in the txt********************************")
            assert False