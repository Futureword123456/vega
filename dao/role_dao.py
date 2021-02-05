# -*- coding: utf-8 -*-
# @Time : 2021/2/2 0002
# @Author : yang
# @Email : 2635681517@qq.com
# @File : role_dao.py

from db.mysql_db import pool


class RoleDao(object):

    def search_list(self):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = "SELECT id,role from t_role"
            cur.execute(sql)
            result = cur.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
