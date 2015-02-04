#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from config import SQL_path

print("Content-type: text/html",end='\n\n')
print("""
<!DOCTYPE html>
<html>
<head>
<title>廠商列表</title>
<meta charset="UTF-8">
<link href="../Site.css" rel="stylesheet">
</head>
<body>

<nav id="nav01"></nav>

<div id="main">
  <h1>廠商列表</h1>""")

from os.path import isfile
import sqlite3

if not isfile(SQL_path):
  print("Can't detect SQL database at path:",SQL_path)
  from database import create_db
  conn=create_db(SQL_path)
else:
  from database import link_db
  conn=link_db(SQL_path)

cursor=conn.cursor()
showList=['name']
cursor.execute('SELECT '+','.join(showList)+' FROM company')
data=cursor.fetchall()

print('<table>')
print('<tr>')
print(''.join(list(map(lambda x:'<th>'+x+'</th>',showList))))
print('</tr>')
for row in data:
  print('<tr>')
  for ele in row:
    print('<td>')
    print(ele)
    print('</td>')
  print('</tr>')
print('</table>')

############################
print('<br>'*3)
print('<h1>新增廠商</h1>')
print("""<form action='AddVendor.cgi'>
         廠商名字:<input type='text' name='com_name'>
         <input type='hidden' name='sqlpath' value='"""
         +SQL_path+"""' readonly>
         <input type='submit' value='更新'>
         </form>""")
print('<br>'*3)

print("""<footer id="foot01"></footer>
</div>

<script src="../Script.js"></script>

</body>
</html>""")



