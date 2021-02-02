# -*- coding: utf-8 -*-
# @Time : 2021/2/2 0002
# @Author : yang
# @Email : 2635681517@qq.com
# @File : user_service.py
from db.user_dao import UserDao


class UserService(object):
    __user_dao = UserDao()
    # 用户的登录service程序
    """service的作用是写业务逻辑的"""

    def login(self, username, password):
        result = self.__user_dao.login(username, password)
        return result

    """查询用户角色"""
    def search_user_role(self, username):
        role = self.__user_dao.search_user_role(username)
        return role