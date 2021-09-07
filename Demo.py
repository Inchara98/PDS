import time
import requests
import wget
import zipfile
import os
import shutil
from selenium.webdriver.chrome.options import Options

from selenium import webdriver

from Utilities.readProperties import ReadConfig

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory":"/home/inchara/PycharmProjects/PDS/Downloads"})
driver = webdriver.Chrome(executable_path="/home/inchara/PycharmProjects/PDS/driver/chromedriver",chrome_options=chromeOptions)
fdriver = webdriver.Firefox(executable_path="/home/inchara/PycharmProjects/PDS/driver/geckodriver")
str1 = driver.capabilities['browserVersion']
str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
print("chrome-browser_version: ",str1)
print("chrome-driver_version: ",str2)
print(str1[0:2])
print(str2[0:2])
if str1[0:2] != str2[0:2]:

  # get the latest chrome driver version number
  url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
  response = fdriver.get(url)
  version_number = response.text
  # build the donwload url
  download_url = "https://chromedriver.storage.googleapis.com/" + version_number + "/chromedriver_linux64.zip"
  fdriver.get(download_url)
  # download the zip file using the url built above
  latest_driver_zip = wget.download(download_url, 'chromedriver.zip')
  # extract the zip file
  with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
    zip_ref.extractall()  # you can specify the destination folder path here

  #delete the zip file downloaded above
  os.remove("/home/inchara/PycharmProjects/PDS/driver/chromedriver")
  #os.remove(latest_driver_zip)
# file = ReadConfig()



# src =  r'/home/inchara/PycharmProjects/PDS/driver/chromedriver'
# dest = r'/home/inchara/PycharmProjects/PDS/Downloads'
# shutil.copyfile(src, dest)







