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











