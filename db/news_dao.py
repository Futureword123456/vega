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
            sql = "select n.id,n.title,tt.type,u.username " \
                  "from t_news n join t_type tt on n.type_id = tt.id " \
                  "join t_user u on n.editor_id=u.id " \
                  "where n.state=%s " \
                  "order by n.create_time desc " \
                  "limit %s,%s"
            cur.execute(sql, ("待审批", (page - 1) * 5, 5))
            result = cur.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()


# service = NewsDao()
# rest = service.search_unreview_list(1)
# print(rest)