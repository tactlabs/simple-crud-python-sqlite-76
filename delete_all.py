#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 

Course work: 

@author:

Source:
    
'''
import sqlite3
import random
from sqlite3 import Error

database = "test"

def start():
    """
    Query all rows in the CITY table
    :param conn: the Connection object
    :return:
    """    
    conn = None
    
    try:
        conn = sqlite3.connect(database)        
    except Error as e:
        print(e) 
        return
    
    sql = ''' DELETE FROM CITY'''
    cur = conn.cursor()
    
    try:
        cur.execute(sql)       
    except sqlite3.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:        
        conn.commit()
    
    print('Deleted All!')

if __name__ == '__main__':
    start()        