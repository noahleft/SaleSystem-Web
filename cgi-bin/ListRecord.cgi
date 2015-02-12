#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from config import SQL_path

import cgi
form=cgi.FieldStorage()
form_id=form.getvalue('form_id')

print("Content-type: text/html",end='\n\n')
print("""
<!DOCTYPE html>
<html>
<head>
<title>紀錄</title>
<meta charset="UTF-8">
<link href="../Site.css" rel="stylesheet">
</head>
<body>

<nav id="nav01"></nav>

<div id="main">
  <h1>出貨記錄</h1>""")

from os.path import isfile
import sqlite3

if not isfile(SQL_path):
  print("Can't detect SQL database at path:",SQL_path)
  from database import create_db
  conn=create_db(SQL_path)
else:
  from database import link_db
  conn=link_db(SQL_path)

def convertToDict(DataList):
  DataDict={}
  for item in DataList:
    DataDict[item[0]]=item[1]
  return DataDict

cursor=conn.cursor()
showList=['COMP_ID','PROD_ID','DELIVER_DATE','UNIT_PRICE','QUANTITY']
cursor.execute('SELECT '+','.join(showList)+' FROM record WHERE form_id='+str(form_id))
data=cursor.fetchall()
cursor.execute('SELECT ID,NAME FROM company')
companyList=cursor.fetchall()
companyDict=convertToDict(companyList)
cursor.execute('SELECT ID,NAME FROM product')
productList=cursor.fetchall()
productDict=convertToDict(productList)


print('<table>')
print('<tr>')
showChList=['公司','產品','日期','單價','數量']
print(''.join(list(map(lambda x:'<th>'+x+'</th>',showChList))))
print('</tr>')
for row in data:
  print('<tr>')
  print('<td>')
  print(companyDict[row[0]])
  print('</td>')
  print('<td>')
  print(productDict[row[1]])
  print('</td>')
  for ele in row[2:]:
    print('<td>')
    print(ele)
    print('</td>')
  print('</tr>')
print('</table>')

############################

cursor.execute('SELECT id,name from company;')
companyList=cursor.fetchall()
cursor.execute('SELECT id,name from product;')
productList=cursor.fetchall()

print('<br>'*3)
print('<h1>新增記錄</h1>')
print("""<form action='AddRecord.cgi'>
         <input type='hidden' name='sqlpath' value='"""
         +SQL_path+"""' readonly>
         <input type='hidden' name='form_id' value='"""
         +str(form_id)+"""' readonly>公司
         <select name='comp_id'>"""
         +'\n'.join(list(map(lambda x:'<option value="'+str(x[0])+'">'+str(x[1])+'</option>',companyList)))
         +"""</select><br>產品
         <select name='prod_id'>"""
         +'\n'.join(list(map(lambda x:'<option value="'+str(x[0])+'">'+str(x[1])+'</option>',productList)))
         +"""</select><br>單價
         <input type='number' name='unit_price' step='any'><br>數量
         <input type='number' name='quantity'><br>日期
         <input type='date'   name='deliver_date'><br>
         <input type='submit' value='更新'>
         </form>""")
print('<br>'*3)

print("""<footer id="foot01"></footer>
</div>

<script src="../Script.js"></script>

</body>
</html>""")



