#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from config import SQL_path

print("Content-type: text/html",end='\n\n')
print("""
<!DOCTYPE html>
<html>
<head>
<title>單價列表</title>
<meta charset="UTF-8">
<link href="../Site.css" rel="stylesheet">
</head>
<body>

<nav id="nav01"></nav>

<div id="main">
  <h1>單價列表</h1>""")

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
showList=['id','name']
cursor.execute('SELECT '+','.join(showList)+' FROM product WHERE hide=="FALSE"')
productList=cursor.fetchall()
productDict=convertToDict(productList)
cursor.execute('SELECT '+','.join(showList)+' FROM company WHERE hide=="FALSE"')
companyList=cursor.fetchall()
companyDict=convertToDict(companyList)
UPList=['comp_id','prod_id','unit_price']
cursor.execute('SELECT '+','.join(UPList)+' FROM unitprice')
unitPriceList=cursor.fetchall()

showList=['comp','prod','unit_price']
print('<table>')
print('<tr>')
print(''.join(list(map(lambda x:'<th>'+x+'</th>',showList))))
print('</tr>')
unitPriceList=list(filter(lambda x: x[0] in companyDict and x[1] in productDict ,unitPriceList))
for row in unitPriceList:
  print('<tr>')
  print('<td>'+str(companyDict[row[0]])+'</td>')
  print('<td>'+str(productDict[row[1]])+'</td>')
  print('<td>'+str(row[2])+'</td>')
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


############################
print('<br>'*3)
print('<h1>更新單價</h1>')
print("<form action='UpdateUnitPrice.cgi'>"+
      "<input type='hidden' name='sqlpath' value='"+SQL_path+"' readonly>"+
      "公司<select name='comp_id'>\n"+genOptions(companyList)+"</select><br>\n"+ \
      "產品<select name='prod_id'>\n"+genOptions(productList)+"</select><br>\n"+ \
      "單價<input type='number' name='unit_price' step='any' required>\n<br>"+ \
      "<input type='submit' value='更新'></form>")
print('<br>'*3)

print("""<footer id="foot01"></footer>
</div>

<script src="../Script.js"></script>

</body>
</html>""")



