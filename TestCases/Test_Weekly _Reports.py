import time

from Pageobjects_AT.LoginPage import LoginPage
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig

from Pageobjects_AT.WeeklyReports import WeeklyReports


class Test_001_Report:
    baseUrl = ReadConfig.getApplicationUrl1()
    username = ReadConfig.getUserID1()
    password = ReadConfig.getPassword1()
    WeeklyReports = ReadConfig.get_WeeklyReports_FilePath()

    logger = log_Details.logen()

    def test_Weekly_Reports(self, setup):
        self.logger.info("********************verifying test_Book_to_facst********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(35)
        self.WR = WeeklyReports(self.driver)
        self.WR.WeeklyReports()
        a = self.driver.current_url
        if a == "https://uat-pds-bi-automationtool.pdsnew.com/reports/weekly_reports":
            assert True
            self.logger.info("********************Ttest_Book_to_facs********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Book_to_facs.png")
            self.logger.info("********************test_Book_to_facs passed********************************")
            assert False
        self.driver.close()
        self.logger.info("********************test_Book_to_facs passed********************************")



    def test_dropdown(self, setup):
        self.logger.info("********************verifying Submit Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(25)
        self.WR = WeeklyReports(self.driver)
        self.WR.WeeklyReports()
        time.sleep(5)
        a = self.WR.SelectYear_WK()
        a.select_by_index(1)
        month = self.WR.SelectMonth_WK()
        week = self.WR.SelectWeek()
        time.sleep(5)
        i = 1
        j = 1
        for i in range(1, len(month.options)):
            month.select_by_index(i)
            print(month.options[i].text, 'month is selected ')
            for j in range(1, len(week.options)):
                week.select_by_index(j)
                print(week.options[j].text, ' is selected ')
                time.sleep(3)
                choosefile = self.WR.Choosefiles().is_enabled()
                time.sleep(5)
                if choosefile == True:
                    assert True
                else:
                    self.driver.save_screenshot(
                        "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_dropdown.png")
                    self.logger.info("********************test_dropdown passed********************************")
                    assert False

    def test_monthdropdown(self, setup):
        self.logger.info("********************verifying Submit Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(25)
        self.WR = WeeklyReports(self.driver)
        self.WR.WeeklyReports()
        time.sleep(5)
        a = self.WR.SelectYear_WK()
        a.select_by_index(1)
        month = self.WR.SelectMonth_WK()
        month.select_by_visible_text("February")
        time.sleep(5)
        week = self.WR.SelectWeek()
        week.select_by_visible_text("Week1")



