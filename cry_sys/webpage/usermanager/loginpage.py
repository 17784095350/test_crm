import sys
import time
sys.path.append('E:\\gxa')
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from cry_sys.config.log_crm import Autolog
from cry_sys.util.excel_operation import OperationExcel
from cry_sys.base.browseroperation import BrowserOperation
from cry_sys.base.usebrowser import UseBrowser
from cry_sys.util.yaml_opertion import YamlOperation



class LoginPage:

    def __init__(self):
        options=webdriver.ChromeOptions.headless
        self.ub = UseBrowser()
        self.op = OperationExcel('E:\\gxa\\cry_sys\\config\\test_case.xlsx', '用例参数')
        self.bo = BrowserOperation(UseBrowser.driver)
        self.bo.open_url(self.op.get_cell(1,1))
        self.ya=YamlOperation('E:\\gxa\\cry_sys\\config\\locator.yaml')
        self.autolog=Autolog()

    def login(self,username='',password=''):
        self.autolog.set_message('输入用户名','info')
        self.bo.send_keys(self.ya.get_data('LoginPage','username'),username)
        self.autolog.set_message('输入密码', 'info')
        self.bo.send_keys(self.ya.get_data('LoginPage','password'),password)
        self.autolog.set_message('点击登录', 'info')
        self.bo.click_element(self.ya.get_data('LoginPage','clicklogin'))

    def login_correct_text(self,frame_name,xpath):
        self.bo.change_frame(frame_name)#main
        return self.bo.get_text(xpath)#/html/body/table/tbody/tr[1]/td/span
    def login_False(self):
        alert=Alert(UseBrowser.driver)
        t=alert.text
        alert.accept()
        return t

# if __name__=='__main__':
#     l=LoginPage()
#     l.login('admin','123456')
#     time.sleep(4)
#     print(l.login_correct_text(l.ya.get_data('CustomerPage','frametopFrame'),l.ya.get_data('LoginPage','succes')))
#     print(l.op.get_cell(5, 4))
#     UseBrowser.quit()