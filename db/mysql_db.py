# -*- coding: utf-8 -*-
# @Time : 2021/2/2 0002
# @Author : yang
# @Email : 2635681517@qq.com
# @File : mysql_db.py

import mysql.connector.pooling

__config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "root",
    "database": "vega"
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(**__config, pool_size=20)

except Exception as e:

    print(e)
