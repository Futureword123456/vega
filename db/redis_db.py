# -*- coding: utf-8 -*-
# @Time : 2021/2/4 0004
# @Author : yang
# @Email : 2635681517@qq.com
# @File : redis_db.py


import redis

"""redis的链接池"""
try:
    pool = redis.ConnectionPool(
        host="localhost",
        port=6379,
        password="root",
        db=1,
        max_connections=20
    )
except Exception as e:
    print(e)

