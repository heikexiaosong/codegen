#!/usr/bin/env python
#coding:utf8
import pymssql

class DBUtils(object):

    """docstring for Hotel"""
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    def connect(self):
        self.conn = pymssql.connect(host='118.31.239.85',user='KRDMG',password='KRDMG',database='GAVEL_DMG', charset='utf8')

    def destory(self):
        self.conn.close()


    def query(self, sql):
        cur = self.conn.cursor()
        if not cur:
            raise Exception('数据库连接失败！')
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        return result
