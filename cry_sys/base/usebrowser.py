import time

import sys

sys.path.append('E:\\gxa')
from selenium import webdriver
class UseBrowser:

    driver=None

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver=webdriver.Chrome('E:\\gxa\\cry_sys\\chromedriver.exe',chrome_options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        UseBrowser.driver=self.driver
        self.driver.switch_to.parent_frame()

    @classmethod
    def quit(cls):

        UseBrowser.driver.quit()


# if __name__=='__main__':
#
#     u=UseBrowser()
#     time.sleep(4)
#     UseBrowser.quit()