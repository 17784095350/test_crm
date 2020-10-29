import time
import unittest

import sys

sys.path.append('E:\.jenkins\workspace\crm')
from HTMLTestRunner import HTMLTestRunner
from crm_sys.base.usebrowser import UseBrowser
from crm_sys.config.log_crm import Autolog
from crm_sys.util.excel_operation import OperationExcel
from crm_sys.webpage.customermanager.customerpage import CustomerPage


class CustomerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.autolog=Autolog()
        self.c = CustomerPage()
        self.op = OperationExcel('../../config/test_case.xlsx', '用例参数')

    def test_customer_add(self):
        self.c.customer_add(name=self.op.get_cell(6, 5),birthday=str(self.op.get_cell(6, 6)),addman=self.op.get_cell(6, 7),email=self.op.get_cell(6, 8))

        self.autolog.set_message('判断客户是否添加成功', 'info')
        self.assertEqual(self.c.login_False(),self.op.get_cell(6, 4))

    def test_customer_modify(self):
        self.c.customer_modify(str(int(self.op.get_cell(7,9))))
        self.autolog.set_message('判断客户是否修改成功', 'info')
        self.assertEqual(self.c.login_False(), self.op.get_cell(7, 4))

    def tearDown(self) -> None:
        UseBrowser.quit()




if __name__ == '__main__':
    # unittest.main()
    data_1 = time.strftime('%Y-%m-%d', time.localtime())
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(CustomerTest)
    suite.addTests(test_case)
    with open('../../report/CustomerTest_report_.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='auto_test', description='ui_auto_test')
        runner.run(suite)
