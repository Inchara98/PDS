import time
from selenium.webdriver.support.select import Select

from Locators.Locators import Locator_Path


class Hospital:

    def __init__(self,driver):
        self.driver = driver

    def ColumbHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("COLUMB")
        return a

    def CommunityHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("COMMUNITY")
        return a

    def DeaconessHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("DEACONESS")
        return a

    def FloydHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("FLOYD")
        return a

    def GoshenHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("GOSHEN")
        return a

    def Group_not_knownHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("GROUP_NOT_KNOWN")
        return a

    def HarrisHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("HARRIS")
        return a

    def HchphyHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("HCHPHY")
        return a

    def JasperHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("JASPER")
        return a

    def JennieHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("JENNIE")
        return a

    def KingsHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("KINGS")
        return a

    def Logan1Homepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("LOGAN1")
        return a

    def LvngstHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("LVNGST")
        return a

    def MajorHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("MAJOR")
        return a

    def MemsbHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("MEMSB")
        return a

    def OrthoHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("ORTHO")
        return a

    def ParkvwHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("PARKVW")
        return a

    def PutnamHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("PUTNAM")
        return a

    def RiverHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("RIVER")
        return a

    def SchnekHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("SCHNEK")
        return a

    def ThehrtHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("THEHRT")
        return a

    def UtmcHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("UTMC")
        return a

    def VincentHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("VINCENT")
        return a

    def WomensHomepage(self):
        self.data = Locator_Path()
        a = Select(self.driver.find_element_by_id(self.data.SelectHospital)).select_by_visible_text("WOMENS HOSPITAL")
        return a


    def SelectYear(self):
        self.data = Locator_Path()
        Year = Select(self.driver.find_element_by_id(self.data.SelectYear1))
        return Year

    def HospitalRevenue(self):
        self.data = Locator_Path()
        a = self.driver.find_element_by_id(self.data.HospitalRevenue1).text
        return a

    def HospitalTotal_Transaction(self):
        self.data = Locator_Path()
        b = self.driver.find_element_by_id(self.data.HospitalTotal_Transaction).text
        return b
    
    
    def HospitalTotal_Payment(self):
        self.data = Locator_Path()
        c = self.driver.find_element_by_id(self.data.HospitalTotal_Payment).text
        return c

    def HospitalLegal_Action(self):
        self.data = Locator_Path()
        d = self.driver.find_element_by_id(self.data.HospitalLegal_Action).text
        return d
    
    
    def HospitalPageTittle(self):
        self.date = Locator_Path()
        page = self.driver.find_element_by_css_selector(self.data.HospitalPageTittle).text
        return page
    
    
    def Hospitaldropdown(self):
        self.date = Locator_Path()
        Hospital = self.driver.find_element_by_id(self.data.Hospitaldropdown).click()
        return Hospital

    def Dashboard(self):
        Dashboard = self.driver.find_element_by_link_text('DASHBOARD').click()
        return Dashboard


    def Dashboardmenu(self):
        Dashboardmenu = self.driver.find_element_by_id(self.data.Dashboard).click()
        return Dashboardmenu