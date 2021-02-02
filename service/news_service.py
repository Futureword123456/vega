# -*- coding: utf-8 -*-
# @Time : 2021/2/2 0002
# @Author : yang
# @Email : 2635681517@qq.com
# @File : news_service.py

from db.news_dao import NewsDao


class NewService(object):
    __new_dao = NewsDao()

    def search_unreview_list(self, page):
        return self.__new_dao.search_unreview_list(page)
