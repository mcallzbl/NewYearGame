# Date 2024-02-07
# version 1.0
# by mcallzbl
import sqlite3
from sqlite3 import Error
import os

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
    
    @staticmethod
    def getInstance():
        if DataUtils._instance is None:
            DataUtils()
        return DataUtils._instance
    
    def create_connection(self):
        self.db_file = os.path.join(self.getRelativePath(),'pp.dat')
        file_exists = os.path.isfile(self.db_file)
        self.conn = sqlite3.connect(self.db_file)
        if not file_exists:
            self.create_table()

    def create_table(self):
        create_table_sql = """ CREATE TABLE IF NOT EXISTS game_data (
                                        game_time text NOT NULL,
                                        position text NOT NULL,
                                        money integer NOT NULL
                                    ); """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
            self.update_or_insert_game_data('2024-01-15 08:00','家',145.14)
        except Error as e:
            print(e)

    def update_or_insert_game_data(self, game_time, position, money):
        self.create_connection()
        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM game_data")
        if cur.fetchone()[0] == 0:
            sql = ''' INSERT INTO game_data(game_time,position,money)
                      VALUES(?,?,?) '''
            cur.execute(sql, (game_time, position, money))
        else:
            sql = ''' UPDATE game_data
                      SET game_time=?, position=?, money=? '''
            cur.execute(sql, (game_time, position, money))
        self.conn.commit()
        self.closeConnection()

    def get_game_data(self):
        self.create_connection()
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM game_data")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        self.closeConnection()

    def setGameTime(self, game_time):
        self.update_single_field("game_time", game_time)

    def setPosition(self, position:str):
        self.update_single_field("position", position)

    def setMoney(self, money):
        self.update_single_field("money", money)

    def update_single_field(self, field, value):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            sql = f''' UPDATE game_data
                    SET {field} = ?
                    WHERE rowid = 1 '''
            cur.execute(sql, (value,))
            conn.commit()

    def getTime(self)->str:
        return self.get_single_field("game_time")

    def getPosition(self)->str:
        return self.get_single_field("position")

    def getMoney(self):
        return self.get_single_field("money")

    def get_single_field(self, field):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            cur.execute(f"SELECT {field} FROM game_data WHERE rowid = 1")
            result = cur.fetchone()
            if result:
                return result[0]
        return None

    def closeConnection(self):
        if self.conn:
            self.conn.close()

    def getRelativePath(self)->str:
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        return script_dir
