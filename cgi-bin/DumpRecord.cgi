#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from config import SQL_path

import cgi
form=cgi.FieldStorage()
form_id=form.getvalue('form_id')
import sqlite3

from os.path import isfile

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
cursor.execute('SELECT NAME FROM form where id='+str(form_id))
formName=cursor.fetchall()[0][0]

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

<nav id="nav01"></nav>""")
print("""
<div id="main">
  <h1>出貨記錄 """+str(formName)+'</h1>')



showList=['COMP_ID']
cursor.execute('SELECT '+','.join(showList)+' FROM record WHERE form_id='+str(form_id)+' AND hide!=1')
data=set(cursor.fetchall())
cursor.execute('SELECT ID,NAME FROM company')
companyList=cursor.fetchall()
companyDict=convertToDict(companyList)
cursor.execute('SELECT ID,NAME FROM product')


print('<table>')
print('<tr>')
showChList=['公司']
print(''.join(list(map(lambda x:'<th>'+x+'</th>',showChList))))
print('</tr>')
for row in data:
  print('<tr>')
  href='Bill.cgi?form_id='+str(form_id)+'&company_id='+str(row[0])
  print('<td><a href="'+href+'" target="_blank">')
  print(companyDict[row[0]])
  print('</a></td>')
  print('</tr>')
print('</table>')

############################

print("""<footer id="foot01"></footer>
</div>

<script src="../Script.js"></script>

</body>
</html>""")



