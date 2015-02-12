#!/usr/local/bin/python3

import sqlite3

def create_db(name):
  conn=sqlite3.connect(name)
  cursor=conn.cursor()
  cursor.execute('''CREATE TABLE IF NOT EXISTS company
                    (ID    INTEGER PRIMARY KEY AUTOINCREMENT,
                     NAME  TEXT NOT NULL,
                     UNIQUE(NAME));
                 ''')
  cursor.execute('''CREATE TABLE IF NOT EXISTS product
                    (ID    INTEGER PRIMARY KEY AUTOINCREMENT,
                     NAME  TEXT NOT NULL,
                     UNIQUE(NAME));
                 ''')
  cursor.execute('''CREATE TABLE IF NOT EXISTS form
                    (ID    INTEGER PRIMARY KEY AUTOINCREMENT,
                     NAME  TEXT NOT NULL,
                     UNIQUE(NAME));
                 ''')
  cursor.execute('''CREATE TABLE IF NOT EXISTS record
                    (ID    INTEGER PRIMARY KEY AUTOINCREMENT,
                     COMP_ID   INTEGER NOT NULL,
                     PROD_ID   INTEGER NOT NULL,
                     FORM_ID   INTEGER NOT NULL,
                     CREATED_DATE DATETIME NOT NULL,
                     DELIVER_DATE DATETIME NOT NULL,
                     UNIT_PRICE INTEGER NOT NULL,
                     QUANTITY   INTEGER NOT NULL);
                 ''')
  conn.commit()
  return conn

def link_db(name):
  conn=sqlite3.connect(name)
  return conn


def insert_db(conn,table_name,element):
  cursor=conn.cursor()
  cursor.execute('INSERT OR IGNORE INTO '+table_name+' '+ \
                 '(NAME) VALUES ' + \
                 '("'+element[0]+'");')
  conn.commit()

