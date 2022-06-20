# import mysql.connector as dbc
# import pandas as pd

# con = dbc.connect(host = "localhost",user = "root",password = "Shubh1",database = "testdb",charset = "utf8")
# cur = con.cursor()
# # query = open('sql_file.sql', 'r')
# offset_val = 0
# cur.execute("select count(*) from testdb.data")
# val2 = cur.fetchall()
# # print(val2)
# # print("##################################################")
# a=0
# while True:
#     if offset_val > int(val2[0][0]):
#         break;
#     cur.execute("SELECT * FROM testdb.data limit 5 offset %s;" %offset_val)
#     val = cur.fetchall()
#     df = pd.DataFrame(val)
    
#     df.to_csv('E:\\Cheqbook\\python_mysql\\check\\users_{}.csv'.format(a))
#     a += 1
#     print("success")
#     print("-------------------------------------")
#     offset_val += 5
    
# print(val)

from connect3 import Db_connection_for_csv

connect = Db_connection_for_csv('E:\\Cheqbook\\python_mysql\\users_{}.csv')
connect.myfnc()
