#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo

__author__ = 'ldx'
#MongoDb数据库操作类
#date 2015-07-01

class PyConnect(object):

    def __init__(self, host, port):                                                          #初始化链接并加载数据库
        #conn 类型<class 'pymongo.connection.Connection'>
        try:
            self.conn = pymongo.Connection(host, port)
        except Exception:
            print u'connection 地址为%s:%s'%(host,port)
            exit(0)

    def __del__(self):                                                                      #关闭链接
        self.conn.close()

    def use(self, dbname):                                                                 #连接数据库
                                                                                                      # 这种[]获取方式同样适用于shell,下面的collection也一样
                                                                                                       #db 类型<class 'pymongo.database.Database'>
        self.db = self.conn[dbname]

    def setCollection(self, collection):                                                  #设置聚集集合
        if not self.db:
            print u'没有找到指定的数据库'
            exit(0)
        else:
            self.coll = self.db[collection]

    def find(self, query = {}):                                                          #查询记录
        #注意这里query是dict类型
        if type(query) is not dict:
            print u'查询的类型有错误！'
            exit(0)
        try:
            #result类型<class 'pymongo.cursor.Cursor'>
            if not self.coll:
                print u'没有找到聚集集合！'
            else:
                result = self.coll.find(query)
        except NameError:
            print u'字段或名称错误！ ',query
            exit(0)
        return result

    def insert(self, data):                                                              #插入记录
        if type(data) is not dict:
            print u'参数不能为空!'
            exit(0)
        #insert会返回新插入数据的_id
        self.coll.insert(data)

    def remove(self, data):                                                             #删除记录
        if type(data) is not dict:
            print u'参数不能为空!'
            exit(0)
        #remove无返回值
        self.coll.remove(data)

    def update(self, data, setdata):                                                    #更新记录
        if type(data) is not dict or type(setdata) is not dict:
            print u'参数不能为空,或有误!'
            exit(0)
        #update无返回值
        self.coll.update(data,{'$set':setdata})

# if __name__ == '__main__':
#     connect = PyConnect('localhost', 27017)
#     connect.use('test_for_new')
#     connect.setCollection('collection1')
#     connect.insert({'a':10, 'b':1})
#     result = connect.find()
#     connect.update({'a':10, 'b':1}, {'b':10})
#     #x也是dict类型，非常好
#     for x in result:
#         if 'c' in x:
#             print x['_id'], x['a'], x['b'], x['c']
#         else:
#             print x['_id'], x['a'], x['b']
#     connect.remove({'a':10})


# #链接数据库
# def get_db(self):
#     conn = pymongo.Connection(host='127.0.0.1', port=27017)              #链接数据库的地址和端口，本地默认为Localhost  (host='127.0.0.1',port=27017
#     db = conn['mytest']                                                  #mytest数据库名
#     return db
#
# #查看所有聚集集合
# def get_Collection_names(db):
#     return db.collection_names()
