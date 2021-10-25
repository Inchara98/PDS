import time
import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.Hospital import AllHospital
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig


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

    def test_SelectYear2018(self,setup):
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
        self.CH.ColumbHomepage()
        SelectYear18 = self.CH.SelectYear()
        SelectYear18.select_by_index(0)
        time.sleep(35)
        a = self.CH.HospitalPageTittle()
        print(a)
        time.sleep(10)
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
        self.CH = Hospital(self.driver)
        time.sleep(35)
        self.CH.ColumbHomepage()
        SelectYear19 = self.CH.SelectYear()
        SelectYear19.select_by_index(1)
        time.sleep(30)
        a = self.CH.HospitalPageTittle()
        time.sleep(10)
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
        self.CH = Hospital(self.driver)
        time.sleep(30)
        self.CH.ColumbHomepage()
        SelectYear20 = self.CH.SelectYear()
        SelectYear20.select_by_index(2)
        time.sleep(30)
        a = self.CH.HospitalPageTittle()
        time.sleep(10)
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
        self.CH = Hospital(self.driver)
        time.sleep(30)
        self.CH.ColumbHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(3)
        time.sleep(20)
        z = "No Data Found For This Hospital"
        if z in self.driver.page_source:
            print(SelectYear.options[3].text,"is not having data")
            assert False
        else:
            
            a = self.CH.HospitalPageTittle()
            time.sleep(10)
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

    def test_Revenue2018(self,setup):
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
        self.CH.ColumbHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(0)
        time.sleep(30)
        c = self.CH.HospitalRevenue()
        a = "0"
        time.sleep(7)
        if c >= a:
            assert True
            self.driver.close()
            self.logger.info("********************Test  LEGAL_ACTIONS2018 Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_LEGAL_ACTIONS2018.png")
            self.driver.close()
            self.logger.info(
                "********************Test  LEGAL_ACTIONS2018 Ended Due to difference in the txt********************************")
            assert False


    def test_TOTALTRANSACTIONS2018(self,setup):
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
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(0)
        time.sleep(10)
        c = self.CH.HospitalTotal_Transaction()
        time.sleep(3)
        a = "0"
        if c >= a:
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
        self.CH = Hospital(self.driver)
        time.sleep(30)
        self.CH.ColumbHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(0)
        time.sleep(30)
        c = self.CH.HospitalTotal_Payment()
        time.sleep(10)
        a = "0"
        if c >= a:
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


    def test_LEGAL_ACTIONS2018(self,setup):
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
        self.CH.ColumbHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(0)
        time.sleep(30)
        c = self.CH.HospitalLegal_Action()
        time.sleep(10)
        a = "0"
        if c >= a:
            assert True
            self.driver.close()
            self.logger.info("********************Test  LEGAL_ACTIONS2018 Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_LEGAL_ACTIONS2018.png")
            self.driver.close()
            self.logger.info(
                "********************Test  LEGAL_ACTIONS2018 Ended Due to difference in the txt********************************")
            assert False


    def test_Revenue2019(self,setup):
        self.logger.info("********************verifying Revenue2019 Test********************************")
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
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        time.sleep(30)
        c = self.CH.HospitalRevenue()
        time.sleep(10)
        a = "0"
        if c >= a:
            assert True
            self.driver.close()
            self.logger.info("********************Test  Revenue2019 Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Revenue2019.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Revenue2019 Ended Due to difference in the txt********************************")
            assert False



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
        self.CH = Hospital(self.driver)
        time.sleep(30)
        self.CH.ColumbHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        time.sleep(30)
        c = self.CH.HospitalTotal_Transaction()
        time.sleep(10)
        a = "0"
        if c >= a:
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


    def test_TOTALPAYMENTS2019(self,setup):
        self.logger.info("********************verifying TOTAL_PAYMENTS2019 Test********************************")
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
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        time.sleep(30)
        c = self.CH.HospitalTotal_Payment()
        time.sleep(10)
        a = "0"
        if c >= a:
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


    def test_LEGAL_ACTIONS2019(self,setup):
        self.logger.info("********************verifying LEGALACTIONS2019 Test********************************")
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
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        time.sleep(30)
        c = self.CH.HospitalLegal_Action()
        time.sleep(10)
        a = "0"
        if c >= a:
            assert True
            self.driver.close()
            self.logger.info("********************Test  LEGAL_ACTIONS2019 Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_LEGAL_ACTIONS2019.png")
            self.driver.close()
            self.logger.info(
                "********************Test  LEGAL_ACTIONS2019 Ended Due to difference in the txt********************************")
            assert False



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
        self.CH = Hospital(self.driver)
        time.sleep(30)
        self.CH.ColumbHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(2)
        time.sleep(30)
        c = self.CH.HospitalRevenue()
        time.sleep(10)
        a = "0"
        if c >= a:
            assert True
            self.driver.close()
            self.logger.info("********************Test  Revenue2020 Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Revenue2020.png")
            self.driver.close()
            self.logger.info(
                "********************Test  Revenue2020 Ended Due to difference in the txt********************************")
            assert False


    def test_TOTALTRANSACTIONS2020(self,setup):
        self.logger.info("********************verifying TOTALTRANSACTIONS2020 Test********************************")
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
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(2)
        time.sleep(30)
        c = self.CH.HospitalTotal_Transaction()
        time.sleep(10)
        a = "0"
        if c >= a:
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


    def test_TOTALPAYMENTS2020(self,setup):
        self.logger.info("********************verifying TOTALPAYMENTS2020 Test********************************")
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
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(2)
        time.sleep(30)
        c = self.CH.HospitalTotal_Payment()
        time.sleep(10)
        a = "0"
        if c < a:
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
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Hospital(self.driver)
        time.sleep(30)
        self.CH.ColumbHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(2)
        time.sleep(30)
        c = self.CH.HospitalLegal_Action()
        time.sleep(10)
        a = "0"
        if c < a:
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
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Hospital(self.driver)
        time.sleep(30)
        self.CH.ColumbHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(3)
        time.sleep(30)
        c = self.CH.HospitalRevenue()
        time.sleep(10)
        a = "0"
        if c < a:
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
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Hospital(self.driver)
        time.sleep(30)
        self.CH.ColumbHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(3)
        time.sleep(30)
        c = self.CH.HospitalTotal_Transaction()
        time.sleep(10)
        a = "0"
        if c < a:
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
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Hospital(self.driver)
        time.sleep(30)
        self.CH.ColumbHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(3)
        time.sleep(30)
        c = self.CH.HospitalTotal_Payment()
        time.sleep(10)
        a = "0"
        if c < a:
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
        time.sleep(10)
        self.driver.maximize_window()
        self.CH = Hospital(self.driver)
        time.sleep(3)
        self.CH.ColumbHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(3)
        time.sleep(10)
        c = self.CH.HospitalLegal_Action()
        time.sleep(3)
        a = "0"
        if c < a:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_LEGAL_ACTIONS2021.png")
            self.driver.close()
            self.logger.info(
                "********************Test  LEGAL_ACTIONS2021 Ended Due to difference in the txt********************************")
            assert False
        else:
            assert True
            self.driver.close()
            self.logger.info("********************Test  LEGAL_ACTIONS2021 Ended********************************")

    def test_Data2018(self,setup):
        self.logger.info("********************verifying Data2018 Test********************************")
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
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(0)
        time.sleep(20)
        hospital = self.CH.Hospitaldropdown()
        for i in range(1,len(hospital.options)):
            hospital.select_by_index(i)
            if "No Data Found For This Hospital" in self.page_source:
                print(hospital.options[i].text,"No Data")
            else:
                if hospital == name:
                    print("Selected hospital records are present")


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
        self.CH = Hospital(self.driver)
        time.sleep(30)
        self.CH.ColumbHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        time.sleep(30)
        hospital = self.CH.Hospitaldropdown()
        for i in range(1, len(hospital.options)):
            hospital.select_by_index(i)
            if "No Data Found For This Hospital" in self.page_source:
                print(hospital.options[i].text, "No Data")
            else:
                if hospital == name:
                    print("Selected hospital records are present")



    def test_Data2020(self,setup):
        self.logger.info("********************verifying Data2020 Test********************************")
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
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(2)
        time.sleep(30)
        hospital = self.CH.Hospitaldropdown()
        for i in range(1,len(hospital.options)):
            hospital.select_by_index(i)
            if "No Data Found For This Hospital" in self.page_source:
                print(hospital.options[i].text,"No Data")
            else:
                if hospital == name:
                    print("Selected hospital records are present")

    def test_Data2021(self,setup):
        self.logger.info("********************verifying Data2021 Test********************************")
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
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(3)
        time.sleep(30)
        hospital = self.CH.Hospitaldropdown()
        for i in range(1,len(hospital.options)):
            hospital.select_by_index(i)
            time.sleep(3)
            if "No Data Found For This Hospital" in self.page_source:
                print(hospital.options[i].text,"No Data")
            else:
                if hospital == name:
                    print("Selected hospital records are present")


