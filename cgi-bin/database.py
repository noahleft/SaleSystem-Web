#!/usr/local/bin/python3

import sqlite3

def create_db(name):
  conn=sqlite3.connect(name)
  cursor=conn.cursor()
  cursor.execute('''CREATE TABLE IF NOT EXISTS company
                    (ID    INTEGER PRIMARY KEY AUTOINCREMENT,
                     NAME  TEXT NOT NULL,
                     HIDE  BOOLEAN NOT NULL DEFAULT FALSE,
                     UNIQUE(NAME));
                 ''')
  cursor.execute('''CREATE TABLE IF NOT EXISTS product
                    (ID    INTEGER PRIMARY KEY AUTOINCREMENT,
                     NAME  TEXT NOT NULL,
                     HIDE  BOOLEAN NOT NULL DEFAULT FALSE,
                     UNIQUE(NAME));
                 ''')
  cursor.execute('''CREATE TABLE IF NOT EXISTS form
                    (ID    INTEGER PRIMARY KEY AUTOINCREMENT,
                     NAME  TEXT NOT NULL,
                     HIDE  BOOLEAN NOT NULL DEFAULT FALSE,
                     UNIQUE(NAME));
                 ''')
  cursor.execute('''CREATE TABLE IF NOT EXISTS unitprice
                    (ID       INTEGER PRIMARY KEY AUTOINCREMENT,
                     COMP_ID  INTEGER NOT NULL,
                     PROD_ID  INTEGER NOT NULL,
                     UNIT_PRICE REAL  NOT NULL);
                 ''')
  cursor.execute('''CREATE TABLE IF NOT EXISTS record
                    (ID           INTEGER  PRIMARY KEY AUTOINCREMENT,
                     COMP_ID      INTEGER  NOT NULL,
                     PROD_ID      INTEGER  NOT NULL,
                     FORM_ID      INTEGER  NOT NULL,
                     CREATED_DATE DATETIME NOT NULL,
                     DELIVER_DATE DATETIME NOT NULL,
                     UNIT_PRICE   REAL     NOT NULL,
                     QUANTITY     INTEGER  NOT NULL,
                     HIDE  BOOLEAN NOT NULL DEFAULT FALSE);
                 ''')
  conn.commit()
  return conn

def link_db(name):
  conn=sqlite3.connect(name)
  return conn

def hidden_db(conn,table_name,row_id):
  cursor=conn.cursor()
  cursor.execute('UPDATE '+table_name+' SET HIDE=1 '+' WHERE ID='+str(row_id)+';')
  conn.commit()

def insert_db(conn,table_name,element,table_cols=["name"]):
  cursor=conn.cursor()
  cursor.execute('INSERT OR IGNORE INTO '+table_name+' '+ \
                 '('+','.join(table_cols)+') VALUES ' + \
                 '('+','.join(element)+');')
  conn.commit()

def update_db(conn,table_name,element,table_cols,checkList,setList):
  cursor=conn.cursor()
  cursor.execute('SELECT * FROM '+table_name+' WHERE '+
                 ' and '.join(list(map(lambda x:str(x[0])+'='+str(x[1]),checkList))))
  if cursor.fetchall():
    cursor.execute('UPDATE '+table_name+' SET '+
    ','.join(list(map(lambda x:str(x[0])+'='+str(x[1]),setList)))+
    ' WHERE '+' and '.join(list(map(lambda x:str(x[0])+'='+str(x[1]),checkList))))
    conn.commit()
  elif element and table_cols:
    insert_db(conn,table_name,element,table_cols)
