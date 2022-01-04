import time

from Pageobjects_AT.LoginPage import LoginPage
from Logs.Log import log_Details
from Utilities.readProperties import ReadConfig
from Pageobjects_AT.BookToFacs import BookToFacs



class Test_001_Report:
    baseUrl = ReadConfig.getApplicationUrl1()
    username = ReadConfig.getUserID1()
    password = ReadConfig.getPassword1()
    BookToFacs = ReadConfig.get_BookToFacs_FilePath()



    logger = log_Details.logen()


    def test_Book_to_facs(self, setup):
        self.logger.info("********************verifying test_Book_to_facst********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(35)
        self.BK = BookToFacs(self.driver)
        self.BK.BookToFacs()
        a = self.driver.current_url
        if a == "https://uat-pds-bi-automationtool.pdsnew.com/reports/book_to_facs":
            assert True
            self.logger.info("********************Ttest_Book_to_facs********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Book_to_facs.png")
            self.logger.info("********************test_Book_to_facs passed********************************")
            assert False
        self.driver.close()
        self.logger.info("********************test_Book_to_facs passed********************************")



    def test_BookToFacs(self,setup):
        self.logger.info("********************verifying ChooseFile Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.BK = BookToFacs(self.driver)
        self.BK.BookToFacs()
        choosefiles = self.BK.Choosefiles()
        choosefiles.send_keys(self.BookToFacs)
        submit = self.BK.Submit().is_enabled()
        time.sleep(20)
        if submit == True:
            assert True
            self.logger.info("********************test_BookToFacs Ended********************************")
        else:
            self.driver.save_screenshot("/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_BookToFacs.png")
            self.logger.info("********************test_BookToFacs Test passed********************************")
            assert False

    def test_Submit(self, setup):
        self.logger.info("********************verifying SubmitButton Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()
        time.sleep(25)
        self.BK = BookToFacs(self.driver)
        self.BK.BookToFacs()
        choosefiles = self.BK.Choosefiles()
        choosefiles.send_keys(self.BookToFacs)
        time.sleep(25)
        self.BK.Submit().click()
        time.sleep(150)
        Execute_Button = self.BK.ExecuteButton()
        if Execute_Button.get_attribute("class") == "alert alert-success text-left":
            assert True
            self.logger.info("********************test_GoodSam_Submit Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_GoodSam_Submit.png")
            self.logger.info("********************test_GoodSam_Submit Test passed********************************")
            assert False

    def test_Executebutton(self, setup):
        self.logger.info("********************verifying SubmitButton Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()
        time.sleep(25)
        self.BK = BookToFacs(self.driver)
        self.BK.BookToFacs()
        choosefiles = self.BK.Choosefiles()
        choosefiles.send_keys(self.BookToFacs)
        time.sleep(25)
        self.BK.Submit().click()
        time.sleep(150)
        self.BK.ExecuteButton().click()
        time.sleep(200)
        D = "100%"
        if D in self.driver.page_source:
            assert True
            self.logger.info("********************test_Executebutton Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Executebutton.png")
            self.logger.info("********************test_Executebutton Test passed********************************")
            assert False



    def test_Confirmation(self, setup):
        self.logger.info("********************verifying SubmitButton Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()
        time.sleep(25)
        self.BK = BookToFacs(self.driver)
        self.BK.BookToFacs()
        choosefiles = self.BK.Choosefiles()
        choosefiles.send_keys(self.BookToFacs)
        time.sleep(25)
        self.BK.Submit().click()
        time.sleep(150)
        self.BK.ExecuteButton().click()
        time.sleep(200)
        D = "Your file execution is completed, you can download the files now."
        if D in self.driver.page_source:
            assert True
            self.logger.info("********************test_Confirmation Ended********************************")
        else:
            self.driver.save_screenshot(
                "/home/inchara/PycharmProjects/PDS/Screenshots/" + "test_Confirmation.png")
            self.logger.info("********************test_Confirmation Test passed********************************")
            assert False




    def test_Download(self,setup):
        self.logger.info("********************verifying DownloadButton Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.driver.close()
        self.BK = BookToFacs(self.driver)
        self.BK.BookToFacs()
        choosefiles = self.BK.Choosefiles()
        choosefiles.send_keys(self.BookToFacs)
        self.BK.Submit().click()
        self.BK.Download_BK().click()

            