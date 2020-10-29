import time
import unittest
import sys

sys.path.append('E:\.jenkins\workspace\crm')
from HTMLTestRunner import HTMLTestRunner

from cry_sys.config.log_crm import Autolog
from cry_sys.util.excel_operation import OperationExcel
from cry_sys.base.browseroperation import BrowserOperation
from cry_sys.base.usebrowser import UseBrowser
from cry_sys.webpage.usermanager.loginpage import LoginPage


class LoginTest(unittest.TestCase):

    def setUp(self) -> None:

        self.l = LoginPage()
        self.autolog = Autolog()
        self.op = OperationExcel('../../config/test_case.xlsx', '用例参数')


    def test_login_name_psaawd_error(self):

        self.l.login(self.op.get_cell(1,2),self.op.get_cell(1,3))
        self.autolog.set_message('判断是否登录成功', 'info')
        self.assertEqual(self.l.login_False(),self.op.get_cell(1,4))

    # def test_login_succes(self):
    #     self.l.login('admin','admin' )
    #     time.sleep(4)
    #     t=self.l.login_correct_text('main','/html/body/table/tbody/tr[1]/td/span')
    #     self.assertEqual(t, '欢迎使用报价管理系统')
    def test_login_passwd_error(self):
        self.l.login(self.op.get_cell(2, 2), self.op.get_cell(2, 3))
        self.autolog.set_message('判断是否登录成功', 'info')
        self.assertEqual(self.l.login_False(), self.op.get_cell(2, 4))
        # self.autolog.set_message('判断是否登录成功', 'info')

    def test_login_name_error(self):
        self.l.login(self.op.get_cell(3, 2), str(int(self.op.get_cell(3, 3))))
        self.autolog.set_message('判断是否登录成功', 'info')
        self.assertEqual(self.l.login_False(), self.op.get_cell(3, 4))
        # self.autolog.set_message('判断是否登录成功', 'info')

    def test_login_name_or_passwd_error(self):
        self.l.login(self.op.get_cell(4, 2), str(int(self.op.get_cell(4, 3))))
        self.autolog.set_message('判断是否登录成功', 'info')
        self.assertEqual(self.l.login_False(), self.op.get_cell(4, 4))
        # self.autolog.set_message('判断是否登录成功', 'info')

    def test_login_sucess(self):
        self.l.login(self.op.get_cell(5, 2), str(int(self.op.get_cell(5, 3))))
        t = self.l.login_correct_text(self.l.ya.get_data('CustomerPage','frametopFrame'),self.l.ya.get_data('LoginPage','succes'))
        # print(t)
        # print(self.op.get_cell(5, 4))
        self.autolog.set_message('判断是否登录成功', 'info')
        self.assertEqual(t, self.op.get_cell(5, 4))
        # self.autolog.set_message('判断是否登录成功', 'info')


    def tearDown(self) -> None:
        UseBrowser.quit()




if __name__ == '__main__':
    data_1 = time.strftime('%Y-%m-%d', time.localtime())
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    suite.addTests(test_case)
    with open('../../report/LoginTest_report_.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='auto_test', description='ui_auto_test')
        runner.run(suite)
