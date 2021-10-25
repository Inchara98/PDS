# import os
# import zipfile
# 
# import wget
# from selenium import webdriver
# 
# fdriver = webdriver.Firefox(executable_path="/home/inchara/PycharmProjects/PDS/driver/geckodriver")
# 
# url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
# response = fdriver.get(url)
# version_number = response.text
# # build the donwload url
# download_url = "https://chromedriver.storage.googleapis.com/" + version_number + "/chromedriver_linux64.zip"
# fdriver.get(download_url)
# # download the zip file using the url built above
# latest_driver_zip = wget.download(download_url, 'chromedriver.zip')
# # extract the zip file
# with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
#    zip_ref.extractall()  # you can specify the destination folder path here
# 
#     #delete the zip file downloaded above
# os.remove("/home/inchara/PycharmProjects/PDS/driver/chromedriver")





