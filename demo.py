# # word=input()
# # word1=''
# # for i in word:
# #     if(i.isupper())==True:
# #         word1+=(i.lower())
# #     elif(i.islower())==True:
# #         word1 += (i.lower())
# #     elif(i.isspace())==True:
# #         word1+=1
# # print(word1)
# #
# #
# # a = "inchara"
# # print(a.upper())
# #
# #
# # n=input("")
# # for i in n:
# #     n=chr(ord(i)-(-32))
# #     print(n,end='')
# #
# # varLowerCase = "INCHARA"
# # print(varLowerCase.lower())
#
# from get_dir import directory
# import configparser
# import os
#
# p = directory()
# config = configparser.ConfigParser()
# cwd = os.path.dirname(__file__)
# ini = os.path.join(cwd, 'Configurations/config.ini')
# config.read(ini)
# print(config['common_info']['baseUrl'])

def login_to_PDS_Billing_Application(self, driver):
    self.driver = driver
    data = ReadConfig()
    self.driver = data.get_driver()
    self.driver.get(data.get_applicationUrl())
    time.sleep(10)
    self.driver.find_element_by_id(self.textbox_username).send_keys(data.get_username())
    self.driver.find_element_by_id(self.textbox_password).send_keys(data.get_password())
    self.driver.find_element_by_id(self.button_login).click()
    time.sleep(10)