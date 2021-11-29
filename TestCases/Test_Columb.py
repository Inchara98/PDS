import time
import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.Hospital import Hospital
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig
from selenium.webdriver.support.select import Select


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()

    logger =log_Details.logen()

    @pytest.mark.smoke
    def test_ColumbHomepage(self,setup):
        self.logger.info("********************verifying ColumbHomepage Test********************************")
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
        a = self.driver.current_url
        if a == "https://uat-pds-billing-info.pdsnew.com/dashboard/COLUMB":
            assert True
            self.logger.info("********************Test  ColumbHomepage Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_ColumbHomepage.png")
            self.logger.info("********************ColumbHomepage Test ended********************************")
            assert False


    def test_SelectYear(self, setup):
        self.logger.info("********************verifying SelectYear Test********************************")
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
        self.CH.ColumbHomepage()
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
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_SelectYear.png")
                self.driver.close()
                self.logger.info(
                    "********************Test  SelectYear Ended Due to difference in the txt********************************")
                assert False

    def test_Revenue(self,setup):
        self.logger.info("********************verifying Revenue Test********************************")
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
        self.CH.ColumbHomepage()
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
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Revenue.png")
                self.driver.close()
                self.logger.info(
                    "********************test_Revenue Ended Due to difference in the txt********************************")
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
        self.CH = Hospital(self.driver)
        time.sleep(30)
        self.CH.ColumbHomepage()
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
                    self.logger.info("********************test_TOTALTRANSACTIONS Ended********************************")
            elif D not in self.driver.page_source:
                print(year.options[i].text, "is not having data")
                assert True
            else:
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTALTRANSACTIONS.png")
                self.driver.close()
                self.logger.info(
                    "********************test_TOTALTRANSACTIONS Ended Due to difference in the txt********************************")
                assert False



    def test_TOTALPAYMENTS(self,setup):
        self.logger.info("********************verifying TOTAL_PAYMENTS Test********************************")
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
        self.CH.ColumbHomepage()
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
                    self.logger.info("********************test_TOTALPAYMENTS Ended********************************")
            elif D not in self.driver.page_source:
                print(year.options[i].text, "is not having data")
                assert True
            else:
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_TOTALPAYMENTS.png")
                self.driver.close()
                self.logger.info(
                    "********************test_TOTALPAYMENTS Ended Due to difference in the txt********************************")
                assert False


    def test_LEGAL_ACTIONS(self,setup):
        self.logger.info("********************verifying LEGAL_ACTIONS Test********************************")
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
        self.CH.ColumbHomepage()
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
                    self.logger.info("********************test_LEGAL_ACTIONS Ended********************************")
            elif D not in self.driver.page_source:
                print(year.options[i].text, "is not having data")
                assert True
            else:
                self.driver.save_screenshot(
                    "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_LEGAL_ACTIONS.png")
                self.driver.close()
                self.logger.info(
                    "********************test_LEGAL_ACTIONS Ended Due to difference in the txt********************************")
                assert False




    # def test_Data2018(self,setup):
    #     self.logger.info("********************verifying Data2018 Test********************************")
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUserName(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #     time.sleep(10)
    #     self.driver.maximize_window()
    #     self.CH = Hospital(self.driver)
    #     time.sleep(30)
    #     self.CH.ColumbHomepage()
    #     SelectYear = self.CH.SelectYear()
    #     SelectYear.select_by_index(0)
    #     time.sleep(20)
    #     hospital = self.CH.Hospitaldropdown()
    #     for i in range(1,len(hospital.options)):
    #         hospital.select_by_index(i)
    #         if "No Data Found For This Hospital" in self.page_source:
    #             print(hospital.options[i].text,"No Data")
    #         else:
    #             if hospital == name:
    #                 print("Selected hospital records are present")



    def test_Dashboard(self,setup):
        self.logger.info("********************verifying test_Dashboard Test********************************")
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
        self.CH.Dashboard()
        a = self.driver.current_url
        if a == "https://uat-pds-billing-info.pdsnew.com/dashboard":
            assert True
            self.logger.info("********************test_Dashboard Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Dashboard.png")
            self.logger.info("********************test_Dashboard ended********************************")
            assert False

    def test_Dashboard1(self,setup):
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
        self.CH.ColumbHomepage()
        time.sleep(35)
        self.CH.Dashboard()
        self.CH.ColumbHomepage()
        time.sleep(35)
        a = self.driver.current_url
        if a == "https://uat-pds-billing-info.pdsnew.com/dashboard/COLUMB":
            assert True
            self.logger.info("********************test_Dashboard1 Passed********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Dashboard1.png")
            self.logger.info("********************test_Dashboard1 ended********************************")
            assert False

    def test_logout(self,setup):
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
        self.CH.ColumbHomepage()
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


    def test_DashboardMenu(self,setup):
        self.logger.info("********************verifying test_DashboardMenu Test********************************")
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
        self.CH.ColumbHomepage()
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
        self.CH.ColumbHomepage()
        time.sleep(35)
        self.CH.Dashboardmenu()
        self.CH.ColumbHomepage()
        time.sleep(35)
        a = self.driver.current_url
        if a == "https://uat-pds-billing-info.pdsnew.com/dashboard/COLUMB":
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
        self.CH.ColumbHomepage()
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
        self.CH.ColumbHomepage()
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


    def test_Propensity_Search(self,setup):
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
        self.CH.ColumbHomepage()
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

    def test_Propensity_ClientAccount(self, setup):
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
        self.CH.ColumbHomepage()
        time.sleep(25)
        self.CH.Propensitylink()
        time.sleep(15)
        self.CH.client_account()
        time.sleep(3)
        values = self.driver.find_elements_by_xpath("//th[1]")
        for i in values:
            time.sleep(2)
            print(i.get_attribute("aria-sort"))
            if i.get_attribute("aria-sort") == "descending" or i.get_attribute("aria-sort") == "ascending":
                assert True
                print("Table sorting is working")
            else:
                assert False

    def test_Propensity_ClientCode(self, setup):
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
        self.CH.ColumbHomepage()
        time.sleep(25)
        self.CH.Propensitylink()
        time.sleep(15)
        self.CH.client_code()
        time.sleep(3)
        values = self.driver.find_elements_by_xpath("//th[2]")
        for i in values:
            time.sleep(2)
            print(i.get_attribute("aria-sort"))
            if i.get_attribute("aria-sort") == "descending" or i.get_attribute("aria-sort") == "ascending":
                assert True
                print("Table sorting is working")
            else:
                assert False

    def test_Propensity_ClientName(self, setup):
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
        self.CH.ColumbHomepage()
        time.sleep(25)
        self.CH.Propensitylink()
        time.sleep(15)
        self.CH.client_Name()
        time.sleep(3)
        values = self.driver.find_elements_by_xpath("//th[3]")
        for i in values:
            time.sleep(2)
            print(i.get_attribute("aria-sort"))
            if i.get_attribute("aria-sort") == "descending" or i.get_attribute("aria-sort") == "ascending":
                assert True
                print("Table sorting is working")
            else:
                assert False

    def test_Propensity_FirstName(self, setup):
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
        self.CH.ColumbHomepage()
        time.sleep(25)
        self.CH.Propensitylink()
        time.sleep(15)
        self.CH.First_Name()
        time.sleep(3)
        values = self.driver.find_elements_by_xpath("//th[4]")
        for i in values:
            time.sleep(2)
            print(i.get_attribute("aria-sort"))
            if i.get_attribute("aria-sort") == "descending" or i.get_attribute("aria-sort") == "ascending":
                assert True
                print("Table sorting is working")
            else:
                assert False

    def test_Propensity_LastName(self, setup):
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
        self.CH.ColumbHomepage()
        time.sleep(25)
        self.CH.Propensitylink()
        time.sleep(15)
        self.CH.Last_Name()
        time.sleep(3)
        values = self.driver.find_elements_by_xpath("//th[5]")
        for i in values:
            time.sleep(2)
            print(i.get_attribute("aria-sort"))
            if i.get_attribute("aria-sort") == "descending" or i.get_attribute("aria-sort") == "ascending":
                assert True
                print("Table sorting is working")
            else:
                assert False

    def test_Phone(self, setup):
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
        self.CH.ColumbHomepage()
        time.sleep(25)
        self.CH.Propensitylink()
        time.sleep(15)
        self.CH.Phone()
        time.sleep(3)
        values = self.driver.find_elements_by_xpath("//th[6]")
        for i in values:
            time.sleep(2)
            print(i.get_attribute("aria-sort"))
            if i.get_attribute("aria-sort") == "descending" or i.get_attribute("aria-sort") == "ascending":
                assert True
                print("Table sorting is working")
            else:
                assert False

    def test_Propensity_score(self, setup):
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
        self.CH.ColumbHomepage()
        time.sleep(25)
        self.CH.Propensitylink()
        time.sleep(15)
        self.CH.Propensity_score()
        time.sleep(3)
        values = self.driver.find_elements_by_xpath("//th[7]")
        for i in values:
            time.sleep(2)
            print(i.get_attribute("aria-sort"))
            if i.get_attribute("aria-sort") == "descending" or i.get_attribute("aria-sort") == "ascending":
                assert True
                print("Table sorting is working")
            else:
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



