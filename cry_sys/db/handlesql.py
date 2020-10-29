import pymysql

class Dboperation:

    def __init__(self,host='', user='', password="",database='', port=3306, charset='utf8'):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.port=port
        self.charset=charset

    def get_conn(self):
        try:
            conn = pymysql.Connection(host=self.host, user=self.user, password=self.password, database=self.database,
                                      port=self.port,
                                      charset=self.charset)
        except Exception as e:
            print(e)
        finally:
            return conn

    def search_opertion(self,sql):
        try:
            conn=self.get_conn()
            cur = conn.cursor()
            # sql = "select * from tb_user"
            # 执行sql
            cur.execute(sql)
            # 获取数据
            res = cur.fetchall()
            # print(res)
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            # 关闭游标
            cur.close()
            conn.close()
            # 关闭连接
        return res

    def update_opertion(self,sql):

        try:
            # sql = "update tb_user set grade='2' where username='daa'"
            # sql = "delete from tb_user where username='daa'"
            # 执行sql
            conn=self.get_conn()
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            # 关闭游标
            cur.close()
            conn.close()
            # 关闭连接

# if __name__=='__main__':
#     a = Dboperation('localhost', 'root', '123456', 'crm', 3306, 'utf8')
#     print(a.search_opertion("select * from customer_info where customer_name='hai'"))

#     a=Dboperation('localhost','root','123456','crm',3306,'utf8')
#
#     #查询
#     # print(a.search_opertion("select * from customer_info"))
#
#     ##更新
#     a.update_opertion("update customer_info set customer_address='重庆' where customer_id=1")
#     print(a.search_opertion("select * from customer_info where customer_id=1"))

    #删除
    # a.update_opertion("delete from customer_info where customer_name='温庆心'")
    # a.search_opertion("select * from customer_info")

    #添加
    # a.update_opertion("insert into customer_info(customer_name,customer_sex,customer_email,birth_day,customer_addman) values('王五','男','84478@qq.com','2000-03-12 20:40:52','admin')")
    # a.search_opertion("select * from customer_info where customer_name='王五'")

