#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from config import SQL_path

print("Content-type: text/html",end='\n\n')
print("""
<!DOCTYPE html>
<html>
<head>
<title>品項列表</title>
<meta charset="UTF-8">
<link href="../Site.css" rel="stylesheet">
</head>
<body>

<nav id="nav01"></nav>

<div id="main">
  <h1>品項列表</h1>""")

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
cursor.execute('SELECT '+','.join(showList)+' FROM product WHERE hide!=1 ORDER BY NAME')
data=cursor.fetchall()

viewList=['品項名字']
print('<table>')
print('<tr>')
print(''.join(list(map(lambda x:'<th>'+x+'</th>',viewList))))
print('</tr>')
for row in data:
  print('<tr>')
  for ele in row:
    print('<td>')
    print(ele)
    print('</td>')
  print('</tr>')
print('</table>')

def genOptions(dataList,initial=1):
  strList=[]
  optionStr=lambda x:'<option value="'+str(x[0])+'">'+str(x[1])+'</option>'
  optionStrSelected=lambda x:'<option value="'+str(x[0])+'" selected>'+str(x[1])+'</option>'
  for data in dataList:
    if data[0]==initial:
      strList.append(optionStrSelected(data))
    else:
      strList.append(optionStr(data))
  return '\n'.join(list(strList))


cursor.execute('SELECT ID,NAME FROM product WHERE hide!=1')
productList=cursor.fetchall()

############################
print('<br>'*3)
print('<h1>品項更名</h1>')
print("<form action='UpdateProductName.cgi'>"+
      "將品項:<select name='prod_id'>\n"+genOptions(productList)+"</select>"+
      "更改成<input type='text' name='pro_name' required>"+
      "<input type='hidden' name='sqlpath' value='"+SQL_path+"' readonly>"+
      "<input type='submit' value='更新'></form>")
print('<br>'*3)

print("""<footer id="foot01"></footer>
</div>

<script src="../Script.js"></script>

</body>
</html>""")



