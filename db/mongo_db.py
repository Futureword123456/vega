# -*- coding: utf-8 -*-
# @Time : 2021/2/5 0005
# @Author : yang
# @Email : 2635681517@qq.com
# @File : mongo_db.py

from pymongo import MongoClient
client = MongoClient(host="localhost", port=27017)
client.admin.authenticate("admin", "root")