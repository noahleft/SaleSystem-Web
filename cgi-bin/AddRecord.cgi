#!/usr/local/bin/python3

print("Content-type: text/html",end='\n\n')

import cgi
form=cgi.FieldStorage()

company_id=form.getvalue('comp_id')
product_id=form.getvalue('prod_id')
form_id=form.getvalue('form_id')
sqlpath=form.getvalue('sqlpath')

from database import insert_db
from database import link_db
#insert_db(link_db(sqlpath),'record',[company_name])

print('''
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Language" content="utf-8">
<meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">''')
print('<meta http-equiv="refresh" content="0.1;url=http://localhost:8000/cgi-bin/ListRecord.cgi?form_id='+str(form_id)+'">')
print('''
</head>
</html>
''')


