#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from config import SQL_path

print("Content-type: text/html",end='\n\n')
print("""
<!DOCTYPE html>
<html>
<head>
<title>表單列表</title>
<meta charset="UTF-8">
<link href="../Site.css" rel="stylesheet">
</head>
<body>

<nav id="nav01"></nav>

<div id="main">
  <h1>表單列表</h1>""")

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
showList=['id','name']
cursor.execute('SELECT '+','.join(showList)+' FROM form WHERE hide!=1 ORDER BY id DESC')
data=cursor.fetchall()

print('<table>')
print('<tr>')
print(''.join(list(map(lambda x:'<th>'+x+'</th>',showList[1:]+['bill']))))
print('</tr>')
for row in data:
  print('<tr>')
  href='ListRecord.cgi?form_id='+str(row[0])
  for ele in row[1:]:
    print('<td>')
    print('<a href="'+href+'">')
    print(ele)
    print('</a></td>')
  href='DumpRecord.cgi?form_id='+str(row[0])
  print('<td><a href="'+href+'">產生</a></td>')
  print('</tr>')
print('</table>')

############################
print('<br>'*3)
print('<h1>新增表單</h1>')
print("""<form action='AddForm.cgi'>
         表單名字:<input type='text' name='com_name' required>
         <input type='hidden' name='sqlpath' value='"""
         +SQL_path+"""' readonly>
         <input type='submit' value='更新'>
         </form>""")
print('<br>'*3)

###########################

from common import genOptions

print('<br>'*3)
print('<h1>刪除表單</h1>')
print('<p><a href="javascript:disable_enable()">啟用</a>刪除功能</p>')
print("<form name='rmForm' action='RmForm.cgi' onsubmit='return validateRmForm()'>"+
      "將表單:<select name='com_id' disabled='disabled' required>\n"+
      "<option disabled selected value='-1'> -- select an option -- </option>"
      +genOptions(data)+"</select>"+
      "<input type='hidden' name='sqlpath' value='"+SQL_path+"""' readonly>
      <input name='submit' type='submit' value='刪除' disabled="disabled">
      </form>""")
print('<br>'*3)

print("""
<script type="text/javascript">
function disable_enable(){
      document.rmForm.com_id.disabled=!document.rmForm.com_id.disabled
      document.rmForm.submit.disabled=!document.rmForm.submit.disabled
}
</script>
<script>
function validateRmForm() {
  var x = document.forms["rmForm"]["com_id"].value;
  if (x == -1) {
    alert("you must select a form");
    return false;
  }
}
</script>
""")

print("""<footer id="foot01"></footer>
</div>

<script src="../Script.js"></script>

</body>
</html>""")



