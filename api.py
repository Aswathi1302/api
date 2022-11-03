import mysql.connector
mydb= mysql.connector.connect(host= 'localhost',user='root',password='',database=' hoteldb')
import requests
import json
data=requests.get("https://jsonplaceholder.typicode.com/users").text

data_info=json.loads(data)
#print(data_info)

user_list=[]
for i in data_info:
    user_list.append([i["name"],i["email"],i["phone"]])
print(user_list)    