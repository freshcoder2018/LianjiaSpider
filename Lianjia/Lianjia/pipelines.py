# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymongo
# from Daomu import settings
# import pymysql


class LianjiaPipeline(object):
    def process_item(self, item, spider):
        print('============================')
        print(item['avgPrice'])
        print(item['dealTotalPrice'])
        print('============================')
        return item


# class DaomuMongoPipeline(object):
#     def __init__(self):
#         # 定义pymongo需要的变量
#         host = settings.MONGODB_HOST
#         port = settings.MONGODB_PORT
#         dbname = settings.MONGODB_DATABASE
#         tname = settings.MONGODB_TABLE
#         # 连接对象
#         conn = pymongo.MongoClient(host=host,
#                                    port=port)
#         # 创建库对象
#         db = conn[dbname]
#         # 集合对象
#         self.myset = db[tname]
#
#     def process_item(self,item,spider):
#         # 将item转为字典格式
#         bookDict = dict(item)
#         self.myset.insert(bookDict)
#         print("存入数据库成功!")
#
#
# class DaomuMysqlPipeline(object):
#     def __init__(self):
#         host = settings.MYSQL_HOST
#         user = settings.MYSQL_USER
#         pwd = settings.MYSQL_PWD
#         dbName = settings.MYSQL_DB
#
#         # 创建数据库连接对象
#         self.db = pymysql.connect(host=host,
#                             user=user,
#                             password=pwd,
#                             database=dbName,
#                             charset="utf8")
#         # 创建游标对象
#         self.cursor = self.db.cursor()
#
#     def process_item(self,item,spider):
#         ins = 'insert into Article values\
#                (%s,%s,%s,%s,%s)'
#         articleList = [
#                     item["bookName"],
#                     item["bookTitle"],
#                     item["zhNum"],
#                     item["zhName"],
#                     item["zhLink"],
#                 ]
#         self.cursor.execute(ins,articleList)
#         self.db.commit()
#         print("成功存入MySQL数据库")