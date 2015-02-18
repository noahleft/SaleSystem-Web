#!/usr/bin/env python3

print("Content-type: text/html",end='\n\n')

import cgi
form=cgi.FieldStorage()

company_id=form.getvalue('comp_id')
product_id=form.getvalue('prod_id')
unit_price=form.getvalue('unit_price')
sqlpath=form.getvalue('sqlpath')
if form.getvalue('back') and form.getvalue('form_id'):
  form_id=form.getvalue('form_id')
  scriptName=str(form.getvalue('back'))+ \
             '?form_id='+str(form_id)+ \
             '&comp_id='+str(company_id)+ \
             '&prod_id='+str(product_id)
else:
  scriptName='ListUnitPrice.cgi'

from database import update_db
from database import link_db
update_db(link_db(sqlpath),
          'unitprice',
          [str(company_id),str(product_id),str(unit_price)],
          ['comp_id','prod_id','unit_price'],
          [('comp_id',company_id),('prod_id',product_id)],
          [('unit_price',unit_price)])

print('<!DOCTYPE html>')
print('<html>')
print('<head>')
print('<meta http-equiv="Content-Language" content="utf-8">')
print('<meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">')
print('<meta http-equiv="refresh" content="0.1;url=http://localhost:8000/cgi-bin/'+scriptName+'">')
print('</head>')
print('</html>')



