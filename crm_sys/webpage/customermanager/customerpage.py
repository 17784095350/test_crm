import time
import sys

sys.path.append('E:\.jenkins\workspace\crm')
from selenium.webdriver.common.alert import Alert

from cry_sys.base.usebrowser import UseBrowser
from cry_sys.config.log_crm import Autolog
from cry_sys.db.customerdb.customeroperdb import CustomerOperdb
from cry_sys.util.excel_operation import OperationExcel
from cry_sys.webpage.usermanager.loginpage import LoginPage


class CustomerPage:

    def __init__(self):
        self.db=CustomerOperdb()
        self.op=OperationExcel('../../config/test_case.xlsx','用例参数')
        self.autolog=Autolog()
        self.lp=LoginPage()
        self.lp.login(self.lp.op.get_cell(5, 2),  str(int(self.lp.op.get_cell(5, 3))))


    def customer_add(self,**kwargs):
        self.kwargs=kwargs
        # print(self.check_db_id_name())
        if self.check_db_id_name()==True:
            self.db.dele_customer("delete from customer_info where customer_name='"+self.kwargs['name']+"'")
        self.autolog.set_message('切换Frame', 'info')
        self.lp.bo.change_frame(self.lp.ya.get_data('CustomerPage','frametopFrame'))
        self.autolog.set_message('点击客户信息', 'info')
        self.lp.bo.click_element(self.lp.ya.get_data('CustomerPage','clickmation'))

        self.autolog.set_message('切换Frame', 'info')
        self.lp.bo.change_frame(self.lp.ya.get_data('CustomerPage', 'mainframe'))


        self.autolog.set_message('点击添加客户信息', 'info')
        self.lp.bo.click_element(self.lp.ya.get_data('CustomerPage','clickadd'))


        self.autolog.set_message('输入客户姓名', 'info')
        self.lp.bo.send_keys(self.lp.ya.get_data('CustomerPage','customername'),kwargs.get('name',''))


        self.autolog.set_message('输入客户出生年月日', 'info')
        self.lp.bo.driver.execute_script("window.document.getElementById('customerBirthday').value='" + str(kwargs.get('birthday','')) + "'")

        self.autolog.set_message('输入客户创建人', 'info')
        self.lp.bo.send_keys(self.lp.ya.get_data('CustomerPage','customeraddman'),kwargs.get('addman', ''))

        self.autolog.set_message('输入客户email', 'info')
        self.lp.bo.send_keys(self.lp.ya.get_data('CustomerPage','customeremail'),kwargs.get('email', ''))
        time.sleep(4)

        self.autolog.set_message('点击添加', 'info')
        self.lp.bo.click_element(self.lp.ya.get_data('CustomerPage','clicksubmit'))


    def customer_modify(self,tel):
        self.autolog.set_message('切换Frame', 'info')
        self.lp.bo.change_frame(self.lp.ya.get_data('CustomerPage', 'frametopFrame'))
        time.sleep(1)
        self.autolog.set_message('点击客户信息', 'info')
        self.lp.bo.click_element(self.lp.ya.get_data('CustomerPage', 'clickmation'))

        self.autolog.set_message('切换Frame', 'info')
        self.lp.bo.change_frame(self.lp.ya.get_data('CustomerPage', 'mainframe'))

        self.autolog.set_message('点击编辑客户信息', 'info')
        self.lp.bo.click_element(self.lp.ya.get_data('CustomerPage', 'upcustmoer'))

        self.autolog.set_message('清空和输入客户手机号', 'info')
        self.lp.bo.clear_element(self.lp.ya.get_data('CustomerPage','customermobile'),tel)

        self.autolog.set_message('点击修改', 'info')
        self.lp.bo.click_element(self.lp.ya.get_data('CustomerPage', 'clicksubmit'))

    def check_db_id_name(self):
        page_content =[]
        page_content.append(self.kwargs['name'])
        data=self.db.search_customer("select * from customer_info where customer_name='"+self.kwargs['name']+"'")
        if page_content==self.db.add_customer_dbata(data):
            return True
        return False


    def login_False(self):
        alert=Alert(UseBrowser.driver)
        t=alert.text
        alert.accept()
        return t


# if __name__=='__main__':
#     cu=CustomerPage()
#     cu.customer_add(name='王五',birthday=str(cu.op.get_cell(6, 6)),addman=cu.op.get_cell(6, 7),email=cu.op.get_cell(6, 8))
#     print(cu.login_False())

