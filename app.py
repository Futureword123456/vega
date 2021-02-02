# -*- coding: utf-8 -*-
# @Time : 2021/2/2 0002
# @Author : yang
# @Email : 2635681517@qq.com
# @File : app.py

# 控制台输入或者输出
from colorama import Fore, Back, Style
from getpass import getpass
from service.user_service import UserService
from service.role_sevice import RoleService
# 清理控制台
import os
import sys
from service.news_service import NewService

sys.setrecursionlimit(1000000)  # 例如这里设置为一百万
import time

__user_service = UserService()
__news_service = NewService()
__role_service = RoleService()

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
        result = __user_service.login(username, password)
        # 登录成功
        if result == True:
            # 查询用户的身份
            role = __user_service.search_user_role(username)
            # 清空屏幕

            while True:
                os.system("cls")
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
                                page = 1
                                while True:
                                    os.system("cls")
                                    count_page = __news_service.search_unreview_count_page()
                                    result = __news_service.search_unreview_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTGREEN_EX,
                                              "\n\t%d\t%s\t%s\t%s" % (index + 1, one[1], one[2], one[3]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-----------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-----------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback、返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev、上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext、下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t请输入操作编号:")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < count_page:
                                        page += 1
                                    elif 1 <= int(opt) <= 5:
                                        news_id = result[int(opt) - 1][0]
                                        __news_service.update_unreview_news(news_id)
                                    elif opt == "back":
                                        break

                            elif opt == "2":
                                page = 1
                                while True:
                                    os.system("cls")
                                    count_page = __news_service.search_count_page()
                                    result = __news_service.search_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTGREEN_EX,
                                              "\n\t%d\t%s\t%s\t%s" % (index + 1, one[1], one[2], one[3]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-----------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-----------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback、返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev、上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext、下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t请输入操作编号:")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < count_page:
                                        page += 1
                                    elif 1 <= int(opt) <= 5:
                                        news_id = result[int(opt) - 1][0]
                                        __news_service.delete_by_id(news_id)
                            elif opt == "back":
                                break
                    elif opt == "2":
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTGREEN_EX, "\n\t1、添加用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t2、修改用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t3、删除用户")
                            print(Fore.LIGHTRED_EX, "\n\tback、返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t请输入操作编号:")
                            if opt == "back":
                                break
                            elif opt == "1":
                                os.system("cls")
                                username = input("\n\t用户名:")
                                password = getpass("\n\t密码:")
                                repassword = getpass("\n\t重复密码")
                                if password != repassword:
                                    print("\n\t两次密码不一致(3秒自动返回)")
                                    time.sleep(3)
                                    continue
                                email = input("\n\t邮箱:")
                                result = __role_service.search_list()
                                for index in range(len(result)):
                                    one = result[index]
                                    print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, one[1]))
                                print(Style.RESET_ALL)
                                opt = input("\n\t角色编号:")
                                role_id = result[int(opt) - 1][0]
                                __user_service.insert(username, password, email, role_id)
                                print("\n\t保存成功(3秒自动返回)")
                                time.sleep(3)
                            elif opt == "2":
                                page = 1
                                while True:
                                    os.system("cls")
                                    count_page = __user_service.search_count_page()
                                    result = __user_service.search_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTGREEN_EX,
                                              "\n\t%d\t%s\t%s" % (index + 1, one[1], one[2]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-----------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-----------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback、返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev、上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext、下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t请输入操作编号:")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < count_page:
                                        page += 1
                                    elif 1 <= int(opt) <= 5:
                                        os.system("cls")
                                        user_id = result[int(opt) - 1][0]
                                        username = input("\n\t新用户名:")
                                        password = input("\n\t新密码:")
                                        repassword = input("\n\t再次新密码:")
                                        if password != repassword:
                                            print(Fore.LIGHTRED_EX, "\n\t两次密码不一样")
                                            print(Style.RESET_ALL)
                                            time.sleep(3)
                                            break
                                        email = input("\n\t新用户邮箱:")
                                        result = __role_service.search_list()
                                        for index in range(len(result)):
                                            one = result[index]
                                            print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, one[1]))
                                        print(Style.RESET_ALL)
                                        opt = input("\n\t角色编号:")
                                        role_id = result[int(opt) - 1][0]
                                        opt = input("\n\t是否保存(Y/N)")
                                        if opt == "Y" or opt == "y":
                                            __user_service.update(user_id, username, password, email, role_id)
                                            print("\n\t保存成功(3秒自动返回)")
                                            time.sleep(3)
                            elif opt == "3":
                                page = 1
                                while True:
                                    os.system("cls")
                                    count_page = __user_service.search_count_page()
                                    result = __user_service.search_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTGREEN_EX,
                                              "\n\t%d\t%s\t%s" % (index + 1, one[1], one[2]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-----------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-----------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback、返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev、上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext、下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t请输入操作编号:")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < count_page:
                                        page += 1
                                    elif 1 <= int(opt) <= 5:
                                        os.system("cls")
                                        user_id = result[int(opt) - 1][0]
                                        __user_service.delete_by_id(user_id)
                                        print("\n\t删除成功(3秒自动返回)")
                                        time.sleep(3)
                    elif opt == "back":
                        break
                    elif opt == "exit":
                        sys.exit(0)
        else:
            print("\n\t登录失败,3秒后自动返回")
            time.sleep(3)
    elif opt == "2":
        sys.exit(0)
