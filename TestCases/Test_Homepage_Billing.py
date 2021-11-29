import time

import pytest
from PageObjects.HomePage_Billing import Homepage_Billing
from PageObjects.HomePage_Billing import Homepage_Billing
from PageObjects.LoginPage import LoginPage
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()

    logger =log_Details.logen()

    @pytest.mark.smoke
    def test_Homepage(self,setup):
        self.logger.info("********************verifying Homepage Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(7)
        a = self.driver.current_url
        if a == "https://uat-pds-billing-info.pdsnew.com/dashboard":
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
        time.sleep(10)
        self.driver.maximize_window()
        self.hp = Homepage_Billing(self.driver)
        time.sleep(10)
        self.hp.logout()
        time.sleep(5)
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


    def test_SelectYear(self, setup):
        self.logger.info("********************verifying SelectYear2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Homepage_Billing(self.driver)
        time.sleep(35)

        year = self.CH.SelectYear()
        i = 0
        for i in range(0, len(year.options)):
            year.select_by_index(i)
            print(year.options[i].text, 'year is selected ')
            time.sleep(8)
            z = "Revenue"
            value = year.options[i].text
            if z in self.driver.page_source:
                print(value, 'Records are Displayed')
            elif z not in self.driver.page_source:
                print(year.options[i].text, "is not having data")
                assert True
            else:
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_SelectYear2020.png")
                self.driver.close()
                self.logger.info(
                    "********************Test  SelectYear2020 Ended Due to difference in the txt********************************")
                assert False

    def test_Revenue(self,setup):
        self.logger.info("********************verifying Revenue2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Homepage_Billing(self.driver)
        time.sleep(30)
        year = self.CH.SelectYear()
        time.sleep(15)
        i = 0
        for i in range(0, len(year.options)):
            year.select_by_index(i)
            time.sleep(20)
            print(year.options[i].text, 'year is selected ')
            time.sleep(15)
            D = "Revenue"
            if D in self.driver.page_source:
                c = self.CH.Revenue()
                a = "0"
                if c >= a:
                    print(year.options[i].text, "REVENUE", c)
                    assert True
                    self.logger.info("********************Test  Revenue Ended********************************")
            elif D not in self.driver.page_source:
                print(year.options[i].text, "is not having data")
                assert True
            else:
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_SelectYear2020.png")
                self.driver.close()
                self.logger.info(
                    "********************Test  SelectYear2020 Ended Due to difference in the txt********************************")
                assert False


    def test_TOTALTRANSACTIONS(self,setup):
        self.logger.info("********************verifying TOTAL_TRANSACTIONS2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Homepage_Billing(self.driver)
        time.sleep(30)
        year = self.CH.SelectYear()
        time.sleep(15)
        i = 0
        for i in range(0, len(year.options)):
            year.select_by_index(i)
            time.sleep(20)
            print(year.options[i].text, 'year is selected ')
            time.sleep(15)
            D = "Revenue"
            if D in self.driver.page_source:
                c = self.CH.Total_Transaction()
                a = "0"
                if c >= a:
                    print(year.options[i].text, "TotalTransaction", c)
                    assert True
                    self.logger.info("********************Test  Revenue Ended********************************")
            elif D not in self.driver.page_source:
                print(year.options[i].text, "is not having data")
                assert True
            else:
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_SelectYear2020.png")
                self.driver.close()
                self.logger.info(
                    "********************Test  SelectYear2020 Ended Due to difference in the txt********************************")
                assert False



    def test_TOTALPAYMENTS(self,setup):
        self.logger.info("********************verifying TOTAL_PAYMENTS2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = Homepage_Billing(self.driver)
        time.sleep(30)
        year = self.CH.SelectYear()
        time.sleep(15)
        i = 0
        for i in range(0, len(year.options)):
            year.select_by_index(i)
            time.sleep(20)
            print(year.options[i].text, 'year is selected ')
            time.sleep(15)
            D = "Revenue"
            if D in self.driver.page_source:
                c = self.CH.Total_Payment()
                a = "0"
                if c >= a:
                    print(year.options[i].text, "TOTALPAYMENTS", c)
                    assert True
                    self.logger.info("********************Test  Revenue Ended********************************")
            elif D not in self.driver.page_source:
                print(year.options[i].text, "is not having data")
                assert True
            else:
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_SelectYear2020.png")
                self.driver.close()
                self.logger.info(
                    "********************Test  SelectYear2020 Ended Due to difference in the txt********************************")
                assert False


    def test_LEGAL_ACTIONS(self,setup):
        self.logger.info("********************verifying LEGAL_ACTIONS2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Homepage_Billing(self.driver)
        time.sleep(30)
        year = self.CH.SelectYear()
        time.sleep(15)
        i = 0
        for i in range(0, len(year.options)):
            year.select_by_index(i)
            time.sleep(20)
            print(year.options[i].text, 'year is selected ')
            time.sleep(15)
            D = "Revenue"
            if D in self.driver.page_source:
                c = self.CH.Legal_Action()
                a = "0"
                if c >= a:
                    print(year.options[i].text, "LEGAL_ACTIONS", c)
                    assert True
                    self.logger.info("********************Test  Revenue Ended********************************")
            elif D not in self.driver.page_source:
                print(year.options[i].text, "is not having data")
                assert True
            else:
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_SelectYear2020.png")
                self.driver.close()
                self.logger.info(
                    "********************Test  SelectYear2020 Ended Due to difference in the txt********************************")
                assert False

    def test_Chatbot(self, setup):
        self.logger.info("********************verifying Chatbot Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Homepage_Billing(self.driver)
        time.sleep(30)
        self.CH.Chatbot()
        c = self.CH.chatbot_tittle()
        time.sleep(10)
        if c == "PDS Bot":
            assert True
            self.driver.close()
            self.logger.info("********************Test  Chatbot Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Chatbot.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Chatbot Ended Due to difference in the title********************************")
            assert False

    def test_Chatbot_exit(self, setup):
        self.logger.info("********************verifying ChatbotExit Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Homepage_Billing(self.driver)
        time.sleep(30)
        self.CH.Chatbot()
        time.sleep(10)
        self.CH.chatbot_exit()
        D = "PDS Bot"
        if D in self.driver.page_source:
            assert True
            self.logger.info("********************Test  Chatbot_Exit Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Chatbot_exit.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Chatbot_Exit Ended Due to difference in the title********************************")
            assert False



