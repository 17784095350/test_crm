from cry_sys.db.handlesql import Dboperation


class CustomerOperdb:

    def __init__(self):
        self.dbop=Dboperation('www.summermori.icu','root','123456','crm',3306,'utf8')


    def dele_customer(self,sql):

        self.dbop.update_opertion(sql)
    def search_customer(self,sql):
        data=self.dbop.search_opertion(sql)
        return data

    def add_customer_dbata(self,data):
        lst_id_name = []
        if data==():
            return []
        else:
            lst_id_name.append(data[0][5])
            return lst_id_name


# c=CustomerOperdb()
# c.dbop.update_opertion("insert into customer_info(customer_name,customer_sex,customer_email,birth_day,customer_addman) values('王五','男','84478@qq.com','2000-03-12 20:40:52','admin')")
# data=c.search_customer("select * from customer_info where customer_name='王五'")
# print(data)
# print(c.add_customer_dbata(data))
# c.dele_customer("delete from customer_info where customer_name='王五'")
# print(c.search_customer("select * from customer_info"))

