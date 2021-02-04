# -*- coding: utf-8 -*-
# @Time : 2021/2/4 0004
# @Author : yang
# @Email : 2635681517@qq.com
# @File : type_dao.py

from db.mysql_db import pool


class TypeDao(object):

    def search_list(self):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = "SELECT id,type from t_type order by id"
            cur.execute(sql)
            result = cur.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

