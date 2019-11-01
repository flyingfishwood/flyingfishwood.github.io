'''
Created on 2019年8月5日

@author: SNQU
'''
import psycopg2
import sys
sys.path.append('..')
from config.config import *

def get_db_conn():
    conn = psycopg2._connect(
        host = db_host,
        post = db_port,
        user = db_user,
        db = db,
        charset = 'utf-8')
    return conn

def  query_db(sql):
    logging.debug(sql)
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    result = cur.fetchall()
    logging.debug(result)
    cur.close()
    conn.close()
    return result
def change_db(sql):
    logging.debug(sql)
    conn = get_db_conn()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        logging.error(str(e))
    finally:
        cur.close()
        conn.close()
def check_user(name):
    sql = "select * from user where name='{}'".format(name)
    result =query_db(sql)
    return True if result else False
def add_user(name,password):
    sql = "insert into user (name, passwd) values ('{}','{}')".format(name, password)
    change_db(sql)
def del_user(name):
    sql = "delete from user where name='{}'".format(name)
    change_db(sql)    
                  




