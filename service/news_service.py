# -*- coding: utf-8 -*-
# @Time : 2021/2/2 0002
# @Author : yang
# @Email : 2635681517@qq.com
# @File : news_service.py

from db.news_dao import NewsDao
from db.redis_news_dao import RedisNewsDao


class NewService(object):
    __news_dao = NewsDao()
    __redis_dao = RedisNewsDao()

    def search_unreview_list(self, page):
        result = self.__news_dao.search_unreview_list(page)
        return result

    """查询待审批新闻的总页数"""

    def search_unreview_count_page(self):
        count_page = self.__news_dao.search_unreview_count_page()
        return count_page

        """审批新闻"""

    def update_unreview_news(self, id):
        self.__news_dao.update_unreview_news(id)

    """查询新闻列表"""

    def search_list(self, page):
        result = self.__news_dao.search_list(page)
        return result

        """查询新闻总页数"""

    def search_count_page(self):
        count_page = self.__news_dao.search_count_page()
        return count_page

        """删除新闻"""

    def delete_by_id(self, id):
        self.__news_dao.delete_by_id(id)

    """添加新闻"""

    def insert(self, title, editor_id, type_id, content_id, is_top):
        self.__news_dao.insert(title, editor_id, type_id, content_id, is_top)

    """"查找用于缓存的记录"""

    def search_catch(self, id):
        result = self.__news_dao.search_catch(id)
        return result

    """向redis保存数据"""

    def cache_news(self, id, title, username, type, content, is_top, create_time):
        self.__redis_dao.insert(id, title, username, type, content, is_top, create_time)

        """删除redis"""
    def delete_cache(self,id):
        self.__redis_dao.delete_cache(id)

    """根据id查询"""

    def search_id(self, id):
        result=self.__news_dao.search_id(id)
        return result

        """更改新闻"""
    def update(self, id, title, type_id, content_id, is_top):
        """修改新闻记录"""
        self.__news_dao.update(id, title, type_id, content_id, is_top)
        """删除redis"""
        self.delete_cache(id)