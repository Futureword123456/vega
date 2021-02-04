# -*- coding: utf-8 -*-
# @Time : 2021/2/4 0004
# @Author : yang
# @Email : 2635681517@qq.com
# @File : redis_news_dao.py


from db.redis_db import pool
import redis


class RedisNewsDao:
    def insert(self, id, title, username, type, content, is_top, create_time):
        """创建链接"""
        try:
            con = redis.Redis(
                connection_pool=pool
            )
        except Exception as e:
            print(e)

        try:
            con.hmset(id, {
                "title": title,
                "username": username,
                "type": type,
                "content": content,
                "is_top": is_top,
                "create_time": create_time
            })
            if is_top == 0:
                con.expire(id, 24 * 60 * 60)
        except Exception as e:
            print(e)
        finally:
            del con
        """删除redis"""
    def delete_cache(self,id):
        try:
            con = redis.Redis(
                connection_pool=pool
            )
        except Exception as e:
            print(e)
        try:
            con.delete(id)
        except Exception as e:
            print(e)
        finally:
            del con

