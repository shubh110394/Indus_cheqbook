import mysql.connector as dbc
import pandas as pd

con = dbc.connect(host = "localhost",user = "root",password = "Shubh1",database = "testdb",charset = "utf8")

# Read the sql file
query = open('sql_file.sql', 'r')
offset_val = 0

while True:
    


# connection == the connection to your database, in your case prob_db
    print(offset_val)
    DF = pd.read_sql_query(query.read(),con,params=[offset_val])
    if DF.empty:
        break
    else:
        offset_val += 8
        print(DF)
        print("-------------------------------------")


query.close() 

# while True:
#     con = dbc.connect(host = "localhost",user = "root",password = "Shubh1",database = "testdb",charset = "utf8")
#     cur = con.cursor()
#     cur.execute("SELECT * FROM testdb.`student-por` LIMIT 10 offset 649")
#     val = cur.fetchall()
#     print(val)
# rec = cur.fetchmany(3)

# for i in rec:
#     print(i)
#     l1 = []
#     lim = 100
# # while True:
    
#     rec = cur.fetchall()
#     print("100 data has been fetched")
#     # if rec == None:
#     #     break
#     for i in rec:
#         l1.append(i)

#     if cur.execute("SELECT count(*) FROM testdb.`student-por`")==0:

#     cur.close()
#     con.close()
#     # sleep(0.5)
    

# print(len(l1))





