#!/usr/bin/env python3

print("Content-type: text/html",end='\n\n')

import cgi
form=cgi.FieldStorage()

company_name=form.getvalue('com_name')
company_id=form.getvalue('com_id')
sqlpath=form.getvalue('sqlpath')

from database import hidden_db
from database import link_db
hidden_db(link_db(sqlpath),'form',company_id)

print('''
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Language" content="utf-8">
<meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">
<meta http-equiv="refresh" content="0.1;url=http://localhost:8000/cgi-bin/ListForm.cgi">
</head>
</html>
''')


