import MySQLdb
import sys

sys.path.append('..')
from src.config.config import *


def get_db_conn():
    ##创建数据库连接
    conn = MySQLdb.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        db=db,
        passwd=db_passwd,
    )
    return conn


def get_ucenter_db():
    conn = MySQLdb.connect(
        host=ucenter_db_host,
        port=db_port,
        user=User_db_name,
        db=user_db,
        passwd=user_db_passwd
    )
    return conn


def ucenter_query_db(sql):
    ## 执行sql语句
    logging.debug(sql)
    conn = get_ucenter_db()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    result = cur.fetchall()
    logging.debug(result)
    cur.close()
    conn.close()
    return result


def query_db(sql):
    ##执行sql语句
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
    ##更换数据库
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
