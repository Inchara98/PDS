from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
@pytest.fixture()


def setup(browser):
    chromeOptions = Options()
    chromeOptions.add_experimental_option("prefs",
                                          {"download.default_directory": "/home/inchara/PycharmProjects/PDS/Downloads"})
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="/home/inchara/PycharmProjects/PDS/driver/chromedriver",chrome_options=chromeOptions)
        print("Launching chrome browser.......")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="/home/inchara/PycharmProjects/PDS/driver/geckodriver")
        print("Launching firefox browser.......")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report #############
#It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'PDS Billing INFO'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Inchara'

#It is hook for delete/modify Environment info to Html Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)

