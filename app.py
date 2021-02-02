# -*- coding: utf-8 -*-
# @Time : 2021/2/2 0002
# @Author : yang
# @Email : 2635681517@qq.com
# @File : app.py

# 控制台输入或者输出
from colorama import Fore, Back, Style
from getpass import getpass
from service.user_service import UserService
# 清理控制台
import os
import sys

sys.setrecursionlimit(1000000)  # 例如这里设置为一百万
import time

__user_service = UserService()
while True:
    os.system("cls")
    print(Fore.LIGHTBLUE_EX, "\n\t====================")
    print(Fore.LIGHTBLUE_EX, "\n\t欢迎使用新闻管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\t====================")
    print(Fore.LIGHTGREEN_EX, "\n\t1、登录系统")
    print(Fore.LIGHTGREEN_EX, "\n\t2、退出系统")
    print(Style.RESET_ALL)
    opt = input("\n\t请输入操作编号:")
    if opt == "1":
        username = input("\n\t用户名:")
        password = getpass("\n\t密码:")
        rest = __user_service.login(username, password)
        # 登录成功
        if rest == True:
            # 查询用户的身份
            role = __user_service.search_user_role(username)
            # 清空屏幕
            os.system("cls")
            while True:
                if role == "新闻编辑":
                    print("test")
                elif role == "管理员":
                    print(Fore.LIGHTGREEN_EX, "\n\t1、新闻管理")
                    print(Fore.LIGHTGREEN_EX, "\n\t2、用户管理")
                    print(Fore.LIGHTRED_EX, "\n\tback、退出登录")
                    print(Fore.LIGHTRED_EX, "\n\texit、退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t请输入操作编号:")
                    if opt == "1":
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTGREEN_EX, "\n\t1、审批新闻")
                            print(Fore.LIGHTGREEN_EX, "\n\t2、删除新闻")
                            print(Fore.LIGHTRED_EX, "\n\tback、返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t请输入操作编号:")
                            if opt == "1":
                                pass



                    elif opt == "back":
                        break
                    elif opt == "exit":
                        sys.exit(0)
        else:
            print("\n\t登录失败,3秒后自动返回")
            time.sleep(3)
    elif opt == "2":
        sys.exit(0)
