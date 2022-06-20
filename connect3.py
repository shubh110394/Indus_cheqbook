import mysql.connector as dbc
import pandas as pd


class Db_connection_for_csv:
    def __init__(self,location):
        self.location = location

    def myfnc(self):
        con = dbc.connect(host = "localhost",user = "root",password = "Shubh1",database = "testdb",charset = "utf8")
        cur = con.cursor()
        cur.execute("select * from testdb.data")

        #fetching all the data from the database
        val2 = cur.fetchall()
        field_names = [i[0] for i in cur.description]

        #putting data to dataframe
        data = pd.DataFrame(val2,columns=field_names)
        offset = 0
        lim = 8
        a = 1

        while offset <= data.shape[0]:
            ans = data[offset:lim]
            # ans.to_csv('E:\\Cheqbook\\python_mysql\\users_{}.csv'.format(a),index=False)
            ans.to_csv(self.location.format(a),index=False)
            a += 1
            offset += 8
            lim += 8
            print("success")


