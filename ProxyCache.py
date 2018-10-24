import mysql.connector
import redis
from DBUtils.PooledDB import PooledDB

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


if __name__ == '__main__':
    proxy_list = get_proxy_list()
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    r = redis.Redis(connection_pool=pool)
    for proxy in proxy_list:
        r.sadd('ip', proxy[1]+':'+proxy[2])