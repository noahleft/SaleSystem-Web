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



showList=['COMP_ID','PROD_ID','DELIVER_DATE','UNIT_PRICE','QUANTITY']
cursor.execute('SELECT '+','.join(showList)+' FROM record WHERE form_id='+str(form_id)+' ORDER BY DELIVER_DATE')
data=cursor.fetchall()
cursor.execute('SELECT ID,NAME FROM company')
companyList=cursor.fetchall()
companyDict=convertToDict(companyList)
cursor.execute('SELECT ID,NAME FROM product')
productList=cursor.fetchall()
productDict=convertToDict(productList)


print('<table>')
print('<tr>')
showChList=['公司','日期','品項','單價','數量']
print(''.join(list(map(lambda x:'<th>'+x+'</th>',showChList))))
print('</tr>')
for row in data:
  rowStrings=['<tr><td>'+str(companyDict[row[0]])+'</td>']
  rowStrings+=['<td>'+str(row[2])+'</td>']
  rowStrings+=['<td>'+str(productDict[row[1]])+'</td>']
  rowStrings+=['<td>'+str(row[3])+'</td>']
  rowStrings+=['<td>'+str(row[4])+'</td>']
  rowStrings+=['</tr>']
  print(''.join(rowStrings))
print('</table>')

############################

cursor.execute('SELECT id,name from company;')
companyList=cursor.fetchall()
cursor.execute('SELECT id,name from product;')
productList=cursor.fetchall()

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

if form.getvalue('comp_id'):
  comp_initial=int(form.getvalue('comp_id'))
else:
  comp_initial=1
if form.getvalue('prod_id'):
  prod_initial=int(form.getvalue('prod_id'))
else:
  prod_initial=1
if form.getvalue('unit_price'):
  unitStr=' value='+str(form.getvalue('unit_price'))+' '
else:
  unitStr=''


print('<br>'*3)
print('<h1>新增記錄</h1>')
print("<form action='AddRecord.cgi' name='AddRecord'>\n"+ \
      "<input type='hidden' name='sqlpath' value='"+SQL_path+"' readonly>\n"+ \
      "<input type='hidden' name='form_id' value='"+str(form_id)+"' readonly>\n"+ \
      "公司<select name='comp_id'>\n"+genOptions(companyList,comp_initial)+"</select><br>\n"+ \
      "產品<select name='prod_id'>\n"+genOptions(productList,prod_initial)+"</select><br>\n"+ \
      "單價<input type='number' name='unit_price' step='any' readonly"+unitStr+">\n"+ \
      "<input type='submit' name='load' value='讀取'><br>"+ \
      "數量<input type='number' name='quantity'><br>\n"+ \
      "日期<input type='date'   name='deliver_date'><br>\n"+ \
      "<input type='submit' name='update' value='更新'></form>")
print('<br>'*3)

############################
print('<h1>更新單價</h1>')
print("<form action='UpdateUnitPrice.cgi' name='UpdateUnitPrice'>"+
      "<input type='hidden' name='sqlpath' value='"+SQL_path+"' readonly>"+
      "<input type='hidden' name='form_id' value='"+str(form_id)+"' readonly>\n"+ \
      "<input type='hidden' name='back' value='"+'ListRecord.cgi'+"' readonly>"+
      "公司<select name='comp_id'>\n"+genOptions(companyList,comp_initial)+"</select><br>\n"+ \
      "產品<select name='prod_id'>\n"+genOptions(productList,prod_initial)+"</select><br>\n"+ \
      "單價<input type='number' name='unit_price' step='any' required>\n<br>"+ \
      "<input type='submit' value='更新'></form>")
print('<br>'*3)

print("""<footer id="foot01"></footer>
</div>

<script src="../Script.js"></script>

</body>
</html>""")




