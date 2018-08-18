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
    
    sql = ''' INSERT INTO CITY (NAME, STATE) 
            VALUES (:name, :state) '''
    cur = conn.cursor()
    
    city_obj = {
        'name' : 'Toronto',
        'state' : 'ON'
    }
    
    created_id = -1
    try:
        cur.execute(sql, city_obj)
        
        created_id = cur.lastrowid
    except sqlite3.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:
        #print('clean up')
        conn.commit()
    
    print('created id : '+str(created_id))

if __name__ == '__main__':
    start()        