import mysql.connector
from DBUtils.PooledDB import PooledDB
import socket
import time

pool = PooledDB(mysql.connector, 10, host='47.101.136.129', user='root', passwd='Liu961227@', db='ip_proxy',
                    port=3306)


def get_proxy_list():
    sql = 'select * from t_proxy'
    conn = pool.connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res


def check_proxy(proxy):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((proxy[1], int(proxy[2])))
        if proxy[5] == '0':
            mark_invalid_proxy(proxy, '1')
        s.close()
        return True
    except Exception as e:
        if proxy[5] == '1':
            mark_invalid_proxy(proxy, '0')
        return False


def mark_invalid_proxy(proxy, flag):
    curr_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    sql = 'update t_proxy set enable = ' + flag + ',last_check_time = ' + '\'' + curr_time + '\'' + ' where id = ' + str(proxy[0])
    conn = pool.connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    proxy_list = get_proxy_list()
    curr_index = 1
    total_no = len(proxy_list)
    for proxy in proxy_list:
        flag = check_proxy(proxy)
        if flag:
            print('[',str(curr_index),'/',str(total_no),']',' ',proxy[1],':',proxy[2],'  可用')
        else:
            print('[',str(curr_index),'/',str(total_no),']',' ',proxy[1],':',proxy[2],'  不可用')
        curr_index += 1