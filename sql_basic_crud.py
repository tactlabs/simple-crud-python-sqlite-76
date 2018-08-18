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

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def select_all(conn):
    """
    Query all rows in the CITY table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM CITY")
 
    rows = cur.fetchall()
    
    print('rows count : '+str(len(rows)))
    
    if(len(rows) <= 0):
        print('No Data available');
 
    for row in rows:
        print(row)         



def add_city(conn, city_obj):
    """
    Create a city
    :param task:
    :return: task id
    """
   
    sql = ''' INSERT INTO CITY (NAME, STATE) 
            VALUES (:name, :state) '''
    cur = conn.cursor()
    
    lastrowid = -1
    try:
        cur.execute(sql, city_obj)
        
        lastrowid = cur.lastrowid
    except sqlite3.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()
    
    return lastrowid

def update_city(conn, city_obj):
    """
    Create a city
    :param city object:
    :return: None
    """
   
    sql = ''' UPDATE CITY
    SET NAME = :new_name, 
    STATE = :state 
    WHERE NAME = :name '''
    cur = conn.cursor()
    
    try:
        cur.execute(sql, city_obj)
        
    except sqlite3.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()
    
    print('Updated')
    
def delete_city(conn, name):
    """
    Delete a city
    :param city object:
    :return: None
    """
   
    sql = ''' DELETE FROM CITY    
    WHERE NAME = ?'''
    cur = conn.cursor()
    
    try:
        cur.execute(sql, (name,))
        
    except sqlite3.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()
    
    print('Deleted')
    
def delete_all_cities(conn):
    """
    Delete a city
    :param city object:
    :return: None
    """
   
    sql = ''' DELETE CITY '''
    cur = conn.cursor()
    
    try:
        cur.execute(sql)
        
    except sqlite3.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()
    
    print('Delete')        

def main():    
 
    # create a database connection
    conn = create_connection(database)
    
    with conn:        
        
        # CREATE
        print('Create City')
        city_obj = {
            'name' : 'Montreal',
            'state' : 'QC'
        } 
        result = add_city(conn, city_obj)
        print(result)
        print('---------------\n')
    
        # READ
        print('Read City')
        select_all(conn)
        print('---------------\n')
        
        # UPDATE
        print('Update City')
        city_new_obj = {
            'name' : 'Montreal',
            'new_name' : 'Quebec City',
            'state' : 'ON'
        }
        update_city(conn, city_new_obj)
        print('---------------\n')
        
        # DELETE    
        print('Delete City')  
        delete_city(conn, 'Quebec City')
        print('---------------\n')
        
        
 
 
if __name__ == '__main__':
    main()        