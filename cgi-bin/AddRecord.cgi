#!/usr/bin/env python3

print("Content-type: text/html",end='\n\n')

import cgi
form=cgi.FieldStorage()

if form.getvalue('load'):
  company_id=form.getvalue('comp_id')
  product_id=form.getvalue('prod_id')
  form_id=form.getvalue('form_id')
  sqlpath=form.getvalue('sqlpath')
  from database import link_db
  connect=link_db(sqlpath)
  cursor=connect.cursor()
  cursor.execute('SELECT UNIT_PRICE FROM unitprice WHERE comp_id='+ \
                  str(company_id)+' and prod_id='+str(product_id))
  data=cursor.fetchall()
  if data:
    unitStr='&unit_price='+str(data[0][0])
  else:
    unitStr=''
  print('''
  <!DOCTYPE html>
  <html>
  <head>
  <meta http-equiv="Content-Language" content="utf-8">
  <meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">''')
  print('<meta http-equiv="refresh"'+ \
        'content="0.1;url=http://localhost:8000/cgi-bin/ListRecord.cgi?'+ \
        'form_id='+str(form_id)+'&comp_id='+str(company_id)+'&prod_id='+str(product_id)+unitStr+'">')
  print('''
  </head>
  </html>
  ''')


if form.getvalue('update'):
  company_id=form.getvalue('comp_id')
  product_id=form.getvalue('prod_id')
  form_id=form.getvalue('form_id')
  sqlpath=form.getvalue('sqlpath')
  deliver=form.getvalue('deliver_date')
  unit_price=form.getvalue('unit_price')
  quantity=form.getvalue('quantity')
  from datetime import date
  today=date.today().isoformat()
  from database import insert_db
  from database import link_db
  insert_db(link_db(sqlpath),'record', \
            list(map(lambda x:'"'+str(x)+'"', \
            [company_id,product_id,form_id,today,deliver,unit_price,quantity])), \
            table_cols=['COMP_ID','PROD_ID','FORM_ID','CREATED_DATE','DELIVER_DATE','UNIT_PRICE','QUANTITY'])
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

