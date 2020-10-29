
# from selenium import webdriver
from crm_sys.base.usebrowser import UseBrowser


class BrowserOperation:

    def __init__(self,driver):
        self.driver=driver
        # self.driver=webdriver.Chrome()


    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'url address error')

    def send_keys(self,xpath,content):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception as e:
            print(e, 'element not found ')

    def click_element(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e, 'element not found ')

    def get_text(self,xpath):
        try:
            t=self.driver.find_element_by_xpath(xpath).text
            return t
        except Exception as e:
            print(e, 'element not found ')
    def change_frame(self,frame_name):
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(frame_name)

    def change_window(self,window_name):
        for window_hd in self.driver.window_handles:
            self.driver.switch_to.window(window_hd)
            if self.driver.title==window_name:
                break

    def clear_element(self,xpath,context):
        try:
            self.driver.find_element_by_xpath(xpath).clear()
            self.send_keys(xpath,context)
        except Exception as e:
            print(e, 'element not found ')
                
                


# if __name__=='__main__':
#     ub=UseBrowser()
#     bo=BrowserOperation(UseBrowser.driver)
#     bo.open_url('http://localhost:8080/JavaPrj_6/')
#     bo.send_keys('//*[@id="UserName"]','admin')
#     bo.send_keys('//*[@id="Password"]','admin')
#     bo.click_element('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[6]/td/input[1]')
#     UseBrowser.quit()

