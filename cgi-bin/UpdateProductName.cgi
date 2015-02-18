#!/usr/bin/env python3

print("Content-type: text/html",end='\n\n')

import cgi
form=cgi.FieldStorage()

product_id=form.getvalue('prod_id')
newProductName=form.getvalue('pro_name')
sqlpath=form.getvalue('sqlpath')

from database import update_db
from database import link_db
update_db(link_db(sqlpath),
          'product',[],[],
          [('id',product_id)],
          [('name',"'"+str(newProductName)+"'")])

print('''
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Language" content="utf-8">
<meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">
<meta http-equiv="refresh" content="0.1;url=http://localhost:8000/cgi-bin/UpdateProduct.cgi">
</head>
</html>
''')



