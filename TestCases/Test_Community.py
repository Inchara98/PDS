import time

from PageObjects.LoginPage import LoginPage
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()

    logger =log_Details.logen()

    def test_CommunityHomepage(self,setup):
        self.logger.info("********************verifying Homepage Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHosptal(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        a = self.driver.current_url
        if a == "https://pds-billing-info.tibilprojects.com/dashboard/COMMUNITY":
            assert True
            self.logger.info("********************Test  CommunityHomepage Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_CommunityHomepage.png")
            self.logger.info("********************CommunityHomepage Test ended********************************")
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
        self.CH = CommunityHospital(self.driver)
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
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(2)
        a = self.driver.find_element_by_id("").text
        time.sleep(3)
        if a == "Overall Revenue v/s Transactions-2019":
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
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(3)
        a = self.driver.find_element_by_id("").text
        time.sleep(3)
        if a == "Overall Revenue v/s Transactions-2020":
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
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(4)
        a = self.driver.find_element_by_id("").text
        time.sleep(3)
        if a == "Overall Revenue v/s Transactions-2021":
            assert True
            self.driver.close()
            self.logger.info("********************Test  SelectYear2021 Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_SelectYear2021.png")
            self.driver.close()
            self.logger.info(
                "********************Test  SelectYear2021 Ended Due to difference in the txt********************************")
            assert False

    def test_Revenue2018(self, setup):
        self.logger.info("********************verifying Revenue2018 Test********************************")
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
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c >= 0:
            assert True
            self.driver.close()
            self.logger.info("********************Test  LEGAL_ACTIONS2018 Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_LEGAL_ACTIONS2018.png")
            self.driver.close()
            self.logger.info(
                "********************Test  LEGAL_ACTIONS2018 Ended Due to difference in the txt********************************")
            assert False

    def test_TOTALTRANSACTIONS2018(self, setup):
        self.logger.info("********************verifying TOTAL_TRANSACTIONS2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c >= 0:
            else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_TRANSACTIONS2018 Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_TRANSACTIONS2018.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_TRANSACTIONS2018 Ended Due to difference in the txt********************************")
            assert False

    def test_TOTALPAYMENTS2018(self, setup):
        self.logger.info("********************verifying TOTAL_PAYMENTS2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c >= 0:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_PAYMENTS2018 Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_PAYMENTS2018.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_PAYMENTS2018 Ended Due to difference in the txt********************************")
            assert False

    def test_LEGAL_ACTIONS2018(self, setup):
        self.logger.info("********************verifying LEGAL_ACTIONS2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c >= 0:
            assert True
            self.driver.close()
            self.logger.info("********************Test  LEGAL_ACTIONS2018 Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_LEGAL_ACTIONS2018.png")
            self.driver.close()
            self.logger.info(
                "********************Test  LEGAL_ACTIONS2018 Ended Due to difference in the txt********************************")
            assert False

    def test_Revenue2019(self, setup):
        self.logger.info("********************verifying Revenue2019 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c >= 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Revenue2019.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Revenue2019 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  Revenue2019 Ended********************************")

    def test_TOTALTRANSACTIONS2019(self, setup):
        self.logger.info("********************verifying TOTAL_TRANSACTIONS2019 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c >= 0:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_TRANSACTIONS2019 Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_TRANSACTIONS2019.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_TRANSACTIONS2019 Ended Due to difference in the txt********************************")
            assert False

    def test_TOTALPAYMENTS2019(self, setup):
        self.logger.info("********************verifying TOTAL_PAYMENTS2019 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c >= 0:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_PAYMENTS2019 Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_PAYMENTS2019.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_PAYMENTS2019 Ended Due to difference in the txt********************************")
            assert False

    def test_LEGAL_ACTIONS2019(self, setup):
        self.logger.info("********************verifying LEGALACTIONS2019 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c == 0:
            assert True
            self.driver.close()
            self.logger.info("********************Test  LEGAL_ACTIONS2019 Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_LEGAL_ACTIONS2019.png")
            self.driver.close()
            self.logger.info(
                "********************Test  LEGAL_ACTIONS2019 Ended Due to difference in the txt********************************")
            assert False

    def test_Revenue2020(self, setup):
        self.logger.info("********************verifying REVENUE2020 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c >= 0:
            assert True
            self.driver.close()
            self.logger.info("********************Test  Revenue2020 Ended********************************")
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Revenue2020.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Revenue2020 Ended Due to difference in the txt********************************")
            assert False
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Revenue2020.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Revenue2020 Ended Due to difference in the txt********************************")
            assert False

    def test_TOTALTRANSACTIONS2020(self, setup):
        self.logger.info("********************verifying TOTALTRANSACTIONS2020 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c >= 0:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_TRANSACTIONS Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_TRANSACTIONS2020.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_TRANSACTIONS2020 Ended Due to difference in the txt********************************")
            assert False

    def test_TOTALPAYMENTS2020(self, setup):
        self.logger.info("********************verifying TOTALPAYMENTS2020 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c < 0:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_PAYMENTS2020.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_PAYMENTS2020 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_PAYMENTS2020 Ended********************************")

    def test_LEGAL_ACTIONS2020(self, setup):
        self.logger.info("********************verifying LEGALACTIONS2020 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c < 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_LEGAL_ACTIONS2020.png")
            self.driver.close()
            self.logger.info(
                "********************Test  LEGAL_ACTIONS2020 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  LEGAL_ACTIONS2020 Ended********************************")

    def test_Revenue2021(self, setup):
        self.logger.info("********************verifying Revenue2021 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c < 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Revenue2021.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Revenue2021 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  Revenue2021 Ended********************************")

    def test_TOTALTRANSACTIONS2021(self, setup):
        self.logger.info("********************verifying TOTALTRANSACTION2021 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c < 0:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_TRANSACTIONS2021.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_TRANSACTIONS2021 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_TRANSACTIONS2021 Ended********************************")

    def test_TOTALPAYMENTS2021(self, setup):
        self.logger.info("********************verifying TOTALPAYMENTS2021 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c < 0:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTAL_PAYMENTS2021.png")
            self.driver.close()
            self.logger.info(
                "********************Test  TOTAL_PAYMENTS2021 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  TOTAL_PAYMENTS Ended********************************")

    def test_LEGAL_ACTIONS2021(self, setup):
        self.logger.info("********************verifying LEGALACTIONs2021 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        c = self.driver.find_element_by_id("").text
        time.sleep(3)
        if c < 0:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_LEGAL_ACTIONS2021.png")
            self.driver.close()
            self.logger.info(
                "********************Test  LEGAL_ACTIONS2021 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  LEGAL_ACTIONS2021 Ended********************************")

    def test_Data2018(self, setup):
        self.logger.info("********************verifying Data2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        hospital = Select(self.driver.find_element_by_id(""))
        for i in range(1, len(hospital.options)):
            hospital.select_by_index(i)
            if "No Data Found for this hospital" in self.page_source:
                print(hospital.options[i].text, "No Data")
            else:
                if hospital == name:
                    print("Selected hospital records are related")

    def test_Data2019(self, setup):
        self.logger.info("********************verifying Data2019 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(2)
        hospital = Select(self.driver.find_element_by_id(""))
        for i in range(1, len(hospital.options)):
            hospital.select_by_index(i)
            if "No Data Found for this hospital" in self.page_source:
                print(hospital.options[i].text, "No Data")
            else:
                if hospital == name:
                    print("Selected hospital records are related")

    def test_Data2020(self, setup):
        self.logger.info("********************verifying Data2020 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(3)
        hospital = Select(self.driver.find_element_by_id(""))
        for i in range(1, len(hospital.options)):
            hospital.select_by_index(2)
            if "No Data Found for this hospital" in self.page_source:
                print(hospital.options[i].text, "No Data")
            else:
                if hospital == name:
                    print("Selected hospital records are related")

    def test_Data2021(self, setup):
        self.logger.info("********************verifying Data2021 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = CommunityHospital(self.driver)
        time.sleep(3)
        self.CH.CommunityHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(4)
        hospital = Select(self.driver.find_element_by_id(""))
        for i in range(1, len(hospital.options)):
            hospital.select_by_index(i)
            if "No Data Found for this hospital" in self.page_source:
                print(hospital.options[i].text, "No Data")
            else:
                if hospital == name:
                    print("Selected hospital records are related")