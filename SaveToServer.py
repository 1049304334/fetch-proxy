import mysql.connector
from DBUtils.PooledDB import PooledDB

pool = PooledDB(mysql.connector, 10, host='47.101.136.129', user='root', passwd='Liu961227@', db='ip_proxy',
                    port=3306)


def save_to_db(proxy):
    sql = 'insert into t_proxy(ip, port, location, last_check_time, enable) values ('\
        + '\''+proxy['ip'] + '\'' + ',' + '\'' + proxy['port'] + '\'' + ','\
        + '\'' + proxy['location'] + '\'' + ',' + '\'' + proxy['last_check_time'] + '\'' + ','\
        + '\'' + proxy['enable'] + '\'' + ')'
    conn = pool.connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
