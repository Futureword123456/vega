# -*- coding: utf-8 -*-
# @Time : 2021/2/4 0004
# @Author : yang
# @Email : 2635681517@qq.com
# @File : type_service.py

from dao.type_dao import TypeDao


class TypeService(object):
    __type_dao = TypeDao()

    def search_list(self):
        result = self.__type_dao.search_list()
        return result
