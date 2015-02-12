#!/usr/bin/env python3

print("Content-type: text/html",end='\n\n')

import cgi
form=cgi.FieldStorage()

company_name=form.getvalue('pro_name')
sqlpath=form.getvalue('sqlpath')

from database import insert_db
from database import link_db
insert_db(link_db(sqlpath),'product',[company_name])

print('''
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Language" content="utf-8">
<meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">
<meta http-equiv="refresh" content="0.1;url=http://localhost:8000/cgi-bin/ListProduct.cgi">
</head>
</html>
''')


