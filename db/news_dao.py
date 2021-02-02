# -*- coding: utf-8 -*-
# @Time : 2021/2/2 0002
# @Author : yang
# @Email : 2635681517@qq.com
# @File : news_dao.py


from db.mysql_db import pool


class NewsDao(object):
    """查询待审批新闻列表"""

    def search_unreview_list(self, page):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = "SELECT n.id,n.title,t.type,u.username " \
                  "FROM t_news n JOIN t_type t ON n.type_id=t.id " \
                  "JOIN t_user u ON n.editor_id=u.id " \
                  "WHERE n.state=%s " \
                  "ORDER BY n.create_time DESC " \
                  "LIMIT %s,%s"
            cur.execute(sql, ("待审批", (page - 1) * 5, 5))
            result = cur.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
        """查询待审批新闻的总页数"""

    def search_unreview_count_page(self):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/5) FROM t_news WHERE state=%s"
            cur.execute(sql, ["待审批"])
            count_page = cur.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    """审批新闻"""

    def update_unreview_news(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cur = con.cursor()
            sql = "update t_news set state=%s where id = %s"
            cur.execute(sql, ("已审批", id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback(0)
            print(e)

        finally:
            if "con" in dir():
                con.close()

        """查询新闻列表"""

    def search_list(self, page):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = "SELECT n.id,n.title,t.type,u.username " \
                  "FROM t_news n JOIN t_type t ON n.type_id=t.id " \
                  "JOIN t_user u ON n.editor_id=u.id " \
                  "ORDER BY n.create_time DESC " \
                  "LIMIT %s,%s"
            cur.execute(sql, ((page - 1) * 5, 5))
            result = cur.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

        """查询新闻总页数"""

    def search_count_page(self):
        try:
            con = pool.get_connection()
            cur = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/5) FROM t_news"
            cur.execute(sql)
            count_page = cur.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

            """删除新闻"""

    def delete_by_id(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cur = con.cursor()
            sql = "delete from t_news where id =%s"
            cur.execute(sql, [id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback(0)
            print(e)

        finally:
            if "con" in dir():
                con.close()
