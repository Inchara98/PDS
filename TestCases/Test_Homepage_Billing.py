import time



from PageObjects.HomePage_Billing import Homepage_Billing
from PageObjects.LoginPage import LoginPage
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()

    logger =log_Details.logen()

    def test_Homepage(self,setup):
        self.logger.info("********************verifying Homepage Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        a = self.driver.current_url
        if a == "https://pds-billing-info.tibilprojects.com/dashboard":
            assert True
            self.logger.info("********************Test  Homepage Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_HomepagePage.png")
            self.logger.info("********************Login Test passed********************************")
            assert False


    def test_logout(self,setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        self.hp.logut()
        time.sleep(3)
        act_title = self.driver.title
        time.sleep(5)
        if act_title == "TIBIL SOLUTIONS":
            assert True
            self.driver.close()
            self.logger.info("********************Test  Logout Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_logout.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Logout Ended Due to difference in the title********************************")
            assert False


    def test_SelectYear(self,setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        a = self.driver.find_element_by_id("").text
        time.sleep(3)
        if a == "Revenue 2018":
            assert True
            self.driver.close()
            self.logger.info("********************Test  SelectYear Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_SelectYear.png")
            self.driver.close()
            self.logger.info(
                "********************Test  SelectYear Ended Due to difference in the txt********************************")
            assert False


    def test_SelectYear2019(self,setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(2)
        a = self.driver.find_element_by_id("").text
        time.sleep(3)
        if a == "Revenue 2019":
            assert True
            self.driver.close()
            self.logger.info("********************Test  SelectYear Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_SelectYear2019.png")
            self.driver.close()
            self.logger.info(
                "********************Test  SelectYear Ended Due to difference in the txt********************************")
            assert False


    def test_SelectYear2020(self,setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = Select(self.hp.SelectYear())
        SelectYear.select_by_index(3)
        a = self.driver.find_element_by_id("").text
        time.sleep(3)
        if a == "Revenue 2020":
            assert True
            self.driver.close()
            self.logger.info("********************Test  SelectYear Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_SelectYear2020.png")
            self.driver.close()
            self.logger.info(
                "********************Test  SelectYear Ended Due to difference in the txt********************************")
            assert False


    def test_SelectYear2021(self,setup):
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(4)
        a = self.driver.find_element_by_id("").text
        time.sleep(3)
        if a == "Revenue 2021":
            assert True
            self.driver.close()
            self.logger.info("********************Test  SelectYear Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_SelectYear2021.png")
            self.driver.close()
            self.logger.info(
                "********************Test  SelectYear Ended Due to difference in the txt********************************")
            assert False

    def test_Revenue2018(self,setup):
        self.logger.info("********************verifying Revenue2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Revenue2018.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Revenue2018 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  Revenue2018 Ended********************************")


    def test_TOTALTRANSACTIONS2018(self,setup):
        self.logger.info("********************verifying TOTAL_TRANSACTIONS2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_TRANSACTIONS2018.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_TRANSACTIONS2018 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_TRANSACTIONS2018 Ended********************************")


    def test_TOTALPAYMENTS2018(self,setup):
        self.logger.info("********************verifying TOTAL_PAYMENTS2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_PAYMENTS2018.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_PAYMENTS2018 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_PAYMENTS2018 Ended********************************")

    def test_LEGAL_ACTIONS2018(self,setup):
        self.logger.info("********************verifying LEGAL_ACTIONS2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_LEGAL_ACTIONS2018.png")
            self.driver.close()
            self.logger.info(
                "********************Test  LEGAL_ACTIONS2018 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  LEGAL_ACTIONS2018 Ended********************************")


    def test_Revenue2019(self,setup):
        self.logger.info("********************verifying Revenue2019 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Revenue2019.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Revenue2019 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  Revenue2019 Ended********************************")


    def test_TOTALTRANSACTIONS2019(self,setup):
        self.logger.info("********************verifying TOTAL_TRANSACTIONS2019 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_TRANSACTIONS2019.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_TRANSACTIONS2019 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_TRANSACTIONS2019 Ended********************************")


    def test_TOTALPAYMENTS2019(self,setup):
        self.logger.info("********************verifying TOTAL_PAYMENTS2019 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_PAYMENTS2019.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_PAYMENTS2019 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_PAYMENTS2019 Ended********************************")

    def test_LEGAL_ACTIONS2019(self,setup):
        self.logger.info("********************verifying LEGALACTIONS2019 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_LEGAL_ACTIONS2019.png")
            self.driver.close()
            self.logger.info(
                "********************Test  LEGAL_ACTIONS2019 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  LEGAL_ACTIONS2019 Ended********************************")


    def test_Revenue2020(self,setup):
        self.logger.info("********************verifying REVENUE2020 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Revenue2020.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Revenue2020 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  Revenue2020 Ended********************************")


    def test_TOTALTRANSACTIONS2020(self,setup):
        self.logger.info("********************verifying TOTALTRANSACTIONS2020 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_TRANSACTIONS2020.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_TRANSACTIONS2020 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_TRANSACTIONS Ended********************************")


    def test_TOTALPAYMENTS2020(self,setup):
        self.logger.info("********************verifying TOTALPAYMENTS2020 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_PAYMENTS2020.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_PAYMENTS2020 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_PAYMENTS2020 Ended********************************")

    def test_LEGAL_ACTIONS2020(self,setup):
        self.logger.info("********************verifying LEGALACTIONS2020 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_LEGAL_ACTIONS2020.png")
            self.driver.close()
            self.logger.info(
                "********************Test  LEGAL_ACTIONS2020 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  LEGAL_ACTIONS2020 Ended********************************")


    def test_Revenue2021(self,setup):
        self.logger.info("********************verifying Revenue2021 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Revenue2021.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Revenue2021 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  Revenue2021 Ended********************************")


    def test_TOTALTRANSACTIONS2021(self,setup):
        self.logger.info("********************verifying TOTALTRANSACTION2021 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_TRANSACTIONS2021.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_TRANSACTIONS2021 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_TRANSACTIONS2021 Ended********************************")


    def test_TOTALPAYMENTS2021(self,setup):
        self.logger.info("********************verifying TOTALPAYMENTS2021 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_PAYMENTS2021.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_PAYMENTS2021 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_PAYMENTS Ended********************************")

    def test_LEGAL_ACTIONS2021(self,setup):
        self.logger.info("********************verifying LEGALACTIONs2021 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        SelectYear = self.hp.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_LEGAL_ACTIONS2021.png")
            self.driver.close()
            self.logger.info(
                "********************Test  LEGAL_ACTIONS2021 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  LEGAL_ACTIONS2021 Ended********************************")

    def Dashboard(self,setup):
        self.logger.info("********************verifying Dashboard Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(3)
        self.hp.Dashboard()
        selectyear = self.driver.find_element_by_id("")
        if selectyear.is_selected():
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Dashboard.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Dashboard Ended Due to selected Year********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  Dashboard Ended********************************")




