import time
import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.Hospital import Hospital
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()

    logger =log_Details.logen()

    @pytest.mark.smoke
    def test_DeaconessHomepage(self,setup):
        self.logger.info("********************verifying Homepage Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(35)
        self.driver.maximize_window()
        self.CH = Hospital(self.driver)
        time.sleep(15)
        self.CH.DeaconessHomepage()
        a = self.driver.current_url
        if a == "https://uat-pds-billing-info.pdsnew.com/dashboard/DEACONESS":
            assert True
            self.logger.info("********************Test DeaconessHomepage Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_DeaconessHomepage.png")
            self.logger.info("********************DeaconessHomepage Test ended********************************")
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
        self.CH = Hospital(self.driver)
        time.sleep(35)
        self.CH.DeaconessHomepage()
        time.sleep(5)

        year = self.CH.SelectYear()
        i = 0
        for i in range(0, len(year.options)):
            year.select_by_index(i)
            print(year.options[i].text, 'year is selected ')
            time.sleep(8)
            z = "PROPENSITY TO PAY SCORES"
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

    def test_Revenue(self, setup):
        self.logger.info("********************verifying Revenue2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Hospital(self.driver)
        time.sleep(30)
        self.CH.DeaconessHomepage()
        time.sleep(15)
        year = self.CH.SelectYear()
        time.sleep(15)
        i = 0
        for i in range(0, len(year.options)):
            year.select_by_index(i)
            time.sleep(20)
            print(year.options[i].text, 'year is selected ')
            time.sleep(15)
            D = "PROPENSITY TO PAY SCORES"
            if D in self.driver.page_source:
                c = self.CH.HospitalRevenue()
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

    def test_TOTALTRANSACTIONS(self, setup):
        self.logger.info("********************verifying TOTAL_TRANSACTIONS2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Hospital(self.driver)
        time.sleep(30)
        self.CH.DeaconessHomepage()
        time.sleep(15)
        year = self.CH.SelectYear()
        time.sleep(15)
        i = 0
        for i in range(0, len(year.options)):
            year.select_by_index(i)
            time.sleep(20)
            print(year.options[i].text, 'year is selected ')
            time.sleep(15)
            D = "PROPENSITY TO PAY SCORES"
            if D in self.driver.page_source:
                c = self.CH.HospitalTotal_Transaction()
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

    def test_TOTALPAYMENTS(self, setup):
        self.logger.info("********************verifying TOTAL_PAYMENTS2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.maximize_window()
        self.CH = Hospital(self.driver)
        time.sleep(30)
        self.CH.DeaconessHomepage()
        time.sleep(15)
        year = self.CH.SelectYear()
        time.sleep(15)
        i = 0
        for i in range(0, len(year.options)):
            year.select_by_index(i)
            time.sleep(20)
            print(year.options[i].text, 'year is selected ')
            time.sleep(15)
            D = "PROPENSITY TO PAY SCORES"
            if D in self.driver.page_source:
                c = self.CH.HospitalTotal_Payment()
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

    def test_LEGAL_ACTIONS(self, setup):
        self.logger.info("********************verifying LEGAL_ACTIONS2018 Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Hospital(self.driver)
        time.sleep(30)
        self.CH.DeaconessHomepage()
        time.sleep(15)
        year = self.CH.SelectYear()
        time.sleep(15)
        i = 0
        for i in range(0, len(year.options)):
            year.select_by_index(i)
            time.sleep(20)
            print(year.options[i].text, 'year is selected ')
            time.sleep(15)
            D = "PROPENSITY TO PAY SCORES"
            if D in self.driver.page_source:
                c = self.CH.HospitalLegal_Action()
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

    # def test_Data2018(self, setup):
    #     self.logger.info("********************verifying Data2018 Test********************************")
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUserName(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #     time.sleep(5)
    #     self.driver.maximize_window()
    #     self.CH = DeaconessHospital(self.driver)
    #     time.sleep(3)
    #     self.CH.DeaconessHomepage()
    #     SelectYear = self.CH.SelectYear()
    #     SelectYear.select_by_index(1)
    #     hospital = self.CH.Hospitaldropdown()
    #     for i in range(1, len(hospital.options)):
    #         hospital.select_by_index(i)
    #         if "No Data Found For This Hospital" in self.page_source:
    #             print(hospital.options[i].text, "No Data")
    #         else:
    #             if hospital == name:
    #                 print("Selected hospital records are present")
    #
    def test_Dashboard(self, setup):
        self.logger.info("********************verifying test_Dashboard ********************************")
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
        self.CH.DeaconessHomepage()
        time.sleep(35)
        self.CH.Dashboard()
        a = self.driver.current_url
        if a == "https://uat-pds-billing-info.pdsnew.com/dashboard":
            assert True
            self.logger.info("********************test_Dashboard Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Dashboard.png")
            self.logger.info("********************test_Dashboard ended********************************")
            assert False


    def test_Dashboard1(self, setup):
        self.logger.info("********************verifying test_Dashboard1 Test********************************")
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
        self.CH.DeaconessHomepage()
        time.sleep(35)
        self.CH.Dashboard()
        self.CH.DeaconessHomepage()
        time.sleep(35)
        a = self.driver.current_url
        if a == "https://uat-pds-billing-info.pdsnew.com/dashboard/DEACONESS":
            assert True
            self.logger.info("********************test_Dashboard1 Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Dashboard1.png")
            self.logger.info("********************test_Dashboard1 ended********************************")
            assert False


    def test_logout(self, setup):
        self.logger.info("********************verifying test_logout Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Hospital(self.driver)
        time.sleep(35)
        self.CH.DeaconessHomepage()
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


    def test_DashboardMenu(self, setup):
        self.logger.info("********************verifying test_DashboardMenu ********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Hospital(self.driver)
        time.sleep(35)
        self.CH.DeaconessHomepage()
        time.sleep(10)
        self.CH.Dashboardmenu()
        a = self.driver.current_url
        if a == "https://uat-pds-billing-info.pdsnew.com/dashboard":
            assert True
            self.logger.info("********************test_DashboardMenu Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_DashboardMenu.png")
            self.logger.info("********************test_DashboardMenu ended********************************")
            assert False


    def test_DashboardMenu1(self,setup):
        self.logger.info("********************verifying test_DashboardMenu1 Test********************************")
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
        self.CH.DeaconessHomepage()
        time.sleep(35)
        self.CH.Dashboardmenu()
        self.CH.DeaconessHomepage()
        time.sleep(35)
        a = self.driver.current_url
        if a == "https://uat-pds-billing-info.pdsnew.com/dashboard/DEACONESS":
            assert True
            self.logger.info("********************test_Dashboard1 Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_DashboardMenu1.png")
            self.logger.info("********************test_DashboardMenu1 ended********************************")
            assert False


    def test_Propensity_score_link(self, setup):
        self.logger.info("********************verifying test_DashboardMenu1 Test********************************")
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
        self.CH.DeaconessHomepage()()
        time.sleep(35)
        self.CH.Propensitylink()
        D = "PROPENSITY SCORE"
        if D in self.driver.page_source:
            assert True
            self.logger.info("********************test_Propensity_score_link Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Propensity_score_link.png")
            self.driver.close()
            self.logger.info(
                "********************test_Propensity_score_link Ended Due to difference in the txt********************************")
            assert False

    def test_Propensity_download(self, setup):
        self.logger.info("********************verifying test_DashboardMenu1 Test********************************")
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
        self.CH.DeaconessHomepage()()
        time.sleep(35)
        self.CH.Propensitylink()
        time.sleep(5)
        self.CH.PropensityDownload()
        time.sleep(35)
        filename = "Download.default_directory" + "COLUMBUS REGIONAL HEALTH_Propensity_Score"
        if os.path.dirname(filename) != True:
            print("Download is working")
        else:
            print("Download is not working")

    def test_Propensity_Search(self, setup):
        self.logger.info("********************verifying test_Propensity_Search Test********************************")
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
        self.CH.DeaconessHomepage()()
        time.sleep(35)
        self.CH.Propensitylink()
        time.sleep(40)
        self.CH.PropensitySearch(self.search)
        b = self.CH.search_validator()
        D = "Moss"
        if D == b:
            assert True
            self.logger.info("********************test_Propensity_Search Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Propensity_Search.png")
            self.driver.close()
            self.logger.info(
                "********************test_Propensity_Search Ended Due to difference in the txt********************************")
            assert False


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
        self.CH.DeaconessHomepage()()()
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
