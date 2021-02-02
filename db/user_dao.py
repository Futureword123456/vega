# -*- coding: utf-8 -*-
# @Time : 2021/2/2 0002
# @Author : yang
# @Email : 2635681517@qq.com
# @File : user_dao.py

from db.mysql_db import pool


class UserDao:
    # 用户的登录
    def login(self, username, password):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = "select count(*) from t_user where username=%s" \
                  " and AES_DECRYPT(UNHEX(password),'HelloWorld')=%s"
            cur.execute(sql, (username, password))
            count = cur.fetchone()[0]
            return True if count == 1 else False
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询登录用户的身份
    def search_user_role(self, username):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = "SELECT r.role FROM t_user u JOIN t_role r ON u.role_id=r.id " \
                  "WHERE u.username=%s"
            cur.execute(sql, [username])
            role = cur.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
