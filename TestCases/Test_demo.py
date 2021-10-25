import time
import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.ColumbHospital import ColumbHospital
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig



class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserID()
    password = ReadConfig.getPassword()

    logger =log_Details.logen()
    
    
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
        self.CH = ColumbHospital(self.driver)
        time.sleep(30)
        self.CH.ColumbHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(1)
        time.sleep(30)
        hospital = self.CH.Hospitaldropdown()
        for i in range(1, len(hospital.options)):
            hospital.select_by_index(i)
            time.sleep(5)
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
        self.CH = ColumbHospital(self.driver)
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
        self.CH = ColumbHospital(self.driver)
        time.sleep(30)
        self.CH.ColumbHomepage()
        SelectYear = self.CH.SelectYear()
        SelectYear.select_by_index(3)
        time.sleep(30)
        hospital = self.CH.Hospitaldropdown()
        for i in range(1,len(hospital.options)):
            hospital.select_by_index(i)
            if "No Data Found For This Hospital" in self.page_source:
                print(hospital.options[i].text,"No Data")
            else:
                if hospital == name:
                    print("Selected hospital records are present")

