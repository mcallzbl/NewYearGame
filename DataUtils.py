# Creation Date: 2024-02-07
# Last Modified Date: 2024-02-18
# version: 1.0
# Author: mcallzbl
# Copyright: Copyright (c) Youright Team. All rights reserved.

import sqlite3
from sqlite3 import Error
import os
import sys

class DataUtils:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) :
        self.conn = None
        self.create_connection()
        self.closeConnection()
        self.offset = 0
        self.money = self.get_single_field("money")
        self.time = self.get_single_field("game_time")
        self.music = self.get_single_field('music')
        self.position = self.get_single_field('position')
        self.script = self.get_single_field('script_name')
        self.function = self.get_single_field('function_name')

    def increase_offset(self, increment:int):
        self.offset += increment
    
    @staticmethod
    def getInstance():
        if DataUtils._instance is None:
            DataUtils()
        return DataUtils._instance
    
    #连接数据库
    def create_connection(self):
        self.db_file = os.path.join(self.getRelativePath(),'pp.dat')
        file_exists = os.path.isfile(self.db_file)
        self.conn = sqlite3.connect(self.db_file)
        if not file_exists:
            self.create_table()

    #创建表
    def create_table(self):
        create_table_sql = """ CREATE TABLE IF NOT EXISTS game_data (
                                        game_time text NOT NULL,
                                        position text NOT NULL,
                                        money integer NOT NULL,
                                        script_name text NOT NULL,
                                        function_name text NOT NULL,
                                        music text NOT NULL
                                    ); """
        create_table_sql2 = '''CREATE TABLE IF NOT EXISTS messages (
                                    id INTEGER PRIMARY KEY, 
                                    content TEXT)
                                '''

        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
            c.execute(create_table_sql2)
            self.update_or_insert_game_data('2024-01-15 08:00','家',145.14,'scene','run','bgm')
        except Error as e:
            print(e)

    #更新或插入游戏数据
    def update_or_insert_game_data(self, game_time, position, money,script_name, function_name,music):
        self.create_connection()
        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM game_data")
        if cur.fetchone()[0] == 0:
            sql = ''' INSERT INTO game_data(game_time,position,money, script_name, function_name,music)
                      VALUES(?,?,?,?,?,?) '''
            cur.execute(sql, (game_time, position, money,script_name, function_name,music))
        else:
            sql = ''' UPDATE game_data
                      SET game_time=?, position=?, money=?, script_name=?, function_name=?,music=? '''
            cur.execute(sql, (game_time, position, money,script_name, function_name,music))
        self.conn.commit()
        self.closeConnection()

    #插入一条历史记录
    def insert_message(self, content):
        self.create_connection()
        cur = self.conn.cursor()
        cur.execute("INSERT INTO messages (content) VALUES (?)", (content,))
        self.conn.commit()
        self.closeConnection()

    #读取历史记录
    def load_history(self,limit):
        self.create_connection()
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM messages ORDER BY id DESC LIMIT ? OFFSET ?", (limit, self.offset,))
        result = cur.fetchall()
        self.conn.commit()
        self.closeConnection()
        return result

    #获取游戏记录
    def get_game_data(self):
        self.create_connection()
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM game_data")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        self.closeConnection()

    #设置游戏时间
    def setGameTime(self, game_time):
        self.update_single_field("game_time", game_time)
        self.time = game_time

    #设置游戏中的位置
    def setPosition(self, position:str):
        self.update_single_field("position", position)
        self.position = position

    #设置游戏中的金钱
    def setMoney(self, money):
        self.update_single_field("money", money)
        self.money = money
    
    #设置游戏bgm
    def setMusic(self,music):
        self.update_single_field("music", music)
        self.music = music

    #设置当前正在执行的函数
    def setFunction(self,function_name):
        self.update_single_field("function_name", function_name)
        self.function = function_name

    #设置当前正在执行的脚本
    def setScript(self,script_name):
        self.update_single_field("script_name", script_name)
        self.script = script_name

    #更新一项数据
    def update_single_field(self, field, value):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            sql = f''' UPDATE game_data
                    SET {field} = ?
                    WHERE rowid = 1 '''
            cur.execute(sql, (value,))
            conn.commit()

    #获取游戏中的时间
    def getTime(self)->str:
        return self.time

    #获取当前bgm
    def getMusic(self)->str:
        return self.music

    #获取游戏中的位置
    def getPosition(self)->str:
        return self.position
    
    #获取游戏中的金钱
    def getMoney(self):
        return self.money
    
    #获取当前正在执行的脚本
    def getScript(self):
        return self.script
    
    #获取当前正在执行的函数
    def getFunction(self):
        return self.function

    #获取一项数据
    def get_single_field(self, field):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            cur.execute(f"SELECT {field} FROM game_data WHERE rowid = 1")
            result = cur.fetchone()
            if result:
                return result[0]
        return None

    #关闭数据库连接
    def closeConnection(self):
        if self.conn:
            self.conn.close()

    #获取资源文件目录
    def getResourcePath(self)->str:
        if getattr(sys, 'frozen', False):
            return sys._MEIPASS
        else: 
            script_path = os.path.abspath(__file__)
            script_dir = os.path.dirname(script_path)
            return script_dir
        
    #获取相对目录    
    def getRelativePath(self)->str:
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        return script_dir
