# -*- coding: utf-8 -*-
# @Time : 2021/2/5 0005
# @Author : yang
# @Email : 2635681517@qq.com
# @File : mongo_news_dao.py

from db.mongo_db import client
from bson import ObjectId


class MongoNewsDao(object):
    """"添加新闻正文记录"""

    def insert(self, title, content):
        try:
            client.vega.news.insert_one({"title": title, "content": content})
        except Exception as e:
            print(e)

    """根据新闻标题查找新闻主键"""

    def search_id(self, title):
        try:
            news = client.vega.news.find_one({"title": title})
            return str(news["_id"])
        except Exception as e:
            print(e)

    def update(self, id, title, content):
        try:
            client.vega.news.update_one({"_id": ObjectId(id)},
                                        {"$set": {"title": title, "content": content}})
        except Exception as e:
            print(e)

            """根据新闻id查找内容"""
    def search_content_by_id(self, id):
        try:
            news = client.vega.news.find_one({"_id": ObjectId(id)})
            return news["content"]
        except Exception as e:
            print(e)
    """删除新闻mongo"""
    def delete_by_id(self, id):
        try:
            client.vega.news.delete_one({"_id": ObjectId(id)})
        except Exception as e:
            print(e)


