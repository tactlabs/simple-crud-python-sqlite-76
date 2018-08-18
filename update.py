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
    
    sql = ''' UPDATE CITY
    SET NAME = :new_name, 
    STATE = :state 
    WHERE NAME = :name '''
    cur = conn.cursor()
    
    city_new_obj = {
        'name' : 'Theni',
        'new_name' : 'Toronto',
        'state' : 'ON'
    }
    
    try:
        cur.execute(sql, city_new_obj)       
    except sqlite3.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:        
        conn.commit()
    
    print('updated!')

if __name__ == '__main__':
    start()        