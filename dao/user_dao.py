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

    """插入数据添加用户信息"""

    def insert(self, username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cur = con.cursor()
            # sql = "insert into t_user(username, password, email, role_id) " \
            #       "values (%s,HEX(AES_DECRYPT(%s,'HelloWorld')),%s,%s)"
            sql = "INSERT INTO t_user(username,password,email,role_id) " \
                  "VALUES(%s,HEX(AES_ENCRYPT(%s,'HelloWorld')),%s,%s)"
            cur.execute(sql, (username, password, email, role_id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)

        finally:
            if "con" in dir():
                con.close()
        """查询用户的总页数"""
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = "select ceil(count(*) /5) from t_user"
            cur.execute(sql)
            count_page = cur.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
    """查询用户记录分页"""
    def search_list(self, page):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = "SELECT u.id,u.username,r.role " \
                  "FROM t_user u JOIN t_role r " \
                  "ON u.role_id=r.id " \
                  "ORDER BY u.id " \
                  "LIMIT %s,%s"
            cur.execute(sql, ((page - 1) * 5, 5))
            result = cur.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    """修改用户信息"""
    def update(self,id,username,password,email,role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cur = con.cursor()
            # sql = "insert into t_user(username, password, email, role_id) " \
            #       "values (%s,HEX(AES_DECRYPT(%s,'HelloWorld')),%s,%s)"
            sql = "update t_user set username=%s," \
                  "password = hex(aes_encrypt(%s,'HelloWorld'))," \
                  "email = %s,role_id=%s " \
                  "where id =%s"
            cur.execute(sql, (username, password, email, role_id,id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)

        finally:
            if "con" in dir():
                con.close()

    """删除用户信息"""
    def delete_by_id(self,id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cur = con.cursor()
            # sql = "insert into t_user(username, password, email, role_id) " \
            #       "values (%s,HEX(AES_DECRYPT(%s,'HelloWorld')),%s,%s)"
            sql = "delete from t_user where id=%s"
            cur.execute(sql, [id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)

        finally:
            if "con" in dir():
                con.close()
        """查询用户id"""
    def search_useid(self,username):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = "select id from t_user where username = %s"
            cur.execute(sql, [username])
            count_page = cur.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
