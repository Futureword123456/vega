# -*- coding: utf-8 -*-
# @Time : 2021/2/2 0002
# @Author : yang
# @Email : 2635681517@qq.com
# @File : role_sevice.py

from  db.role_dao import RoleDao
class RoleService():
    __role_dao = RoleDao()
    # 查询角色列表
    def search_list(self):
        result = self.__role_dao.search_list()
        return result