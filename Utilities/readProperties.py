import configparser
import os
import time

config=configparser.RawConfigParser()
config.read("/home/inchara/PycharmProjects/PDS/Configurations/config.ini")

class ReadConfig():

    def get_driver(self):
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('prefs', prefs)
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options, executable_path="/home/inchara/PycharmProjects/PDS/driver/chromedriver")
        print("Current session is {}".format(self.driver.session_id))
        return self.driver

    @staticmethod
    def getApplicationUrl():
        url = config.get('common_info', 'baseUrl')
        return url

    @staticmethod
    def getUserID():
        username = config.get('common_info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common_info', 'password')
        return password

    @staticmethod
    def getUser():
        Fakeusername = config.get('common_info', 'FakeUsername')
        return Fakeusername

    @staticmethod
    def getpassword():
        FakePassword = config.get('common_info', 'FakePassword')
        return FakePassword

    @staticmethod
    def getEmpty():
        Empty = config.get('common_info', 'Empty')
        return Empty

    @staticmethod
    def getApplicationUrl1():
        url = config.get('common_info', 'baseUrl(AT)')
        return url

    @staticmethod
    def getUserID1():
        username = config.get('common_info', 'username(AT)')
        return username

    @staticmethod
    def getPassword1():
        password = config.get('common_info', 'password(AT)')
        return password

    @staticmethod
    def get_Community_FilePath():
        Community = config.get('common_info', 'Community')
        return Community

    @staticmethod
    def get_Deaconess_FilePath():
        Deaconess = config.get('common_info', 'Deaconess')
        return Deaconess

    @staticmethod
    def get_Womenshospital_FilePath():
        Womenshospital = config.get('common_info', 'WomensHospital')
        return Womenshospital

    @staticmethod
    def get_St_Vincent_FilePath():
        St_Vincent = config.get('common_info', 'St_Vincent')
        return St_Vincent

    @staticmethod
    def get_St_Vincent_Dunn_FilePath():
        St_Vincent_dunn = config.get('common_info', 'St_Vincent_dunn')
        return St_Vincent_dunn

    @staticmethod
    def get_Park_view_FilePath():
        Park_view = config.get('common_info', 'Park_view')
        return Park_view

    @staticmethod
    def get_GoodSam_FilePath():
        GoodSam = config.get('common_info', 'GoodSam')
        return GoodSam

    @staticmethod
    def get_BookToFacs_FilePath():
        BookToFacs = config.get('common_info', 'BookToFacs')
        return BookToFacs

    @staticmethod
    def get_WeeklyReports_FilePath():
        WeeklyReports = config.get('common_info', 'WeeklyReports')
        return WeeklyReports

    @staticmethod
    def get_download_dir():
        cwd = os.path.dirname(__file__)
        download_path = os.path.join(cwd, 'Downloads')
        return download_path

    def get_applicationUrl(self):
        self.p = directory()
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['common_info']['baseUrl']

    def get_username(self):
        self.p = directory()
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['common_info']['username']

    def get_password(self):
        self.p = directory()
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['common_info']['password']


    @staticmethod
    def getSearch():
        Search = config.get('common_info', 'search')
        return Search
