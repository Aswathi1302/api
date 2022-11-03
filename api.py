import mysql.connector
try:
    mydb= mysql.connector.connect(host= 'localhost',user='root',password='',database=' userdb')
except mysql.connector.Error as e:
    #print("connection error")   
    sys.exit("dbconnection failure")
mycursor= mydb.cursor()
import requests
import json
data=requests.get("https://jsonplaceholder.typicode.com/users").text

data_info=json.loads(data)
#print(data_info)

#user_list=[]
for i in data_info:
    #user_list.append([i["name"],i["email"],i["phone"]])
    sql="INSERT INTO `usertbl`(`name`, `email`, `phone`) VALUES ('"+i['name']+"','"+i['email']+"','"+i['phone']+"')"
    mycursor.execute(sql)
    mydb.commit()
    print("data inserted successfully....",i["name"])
#print(user_list)    