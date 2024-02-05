import sqlite3
from sqlite3 import Error
from datetime import datetime, timedelta
class DataUtils:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            
        return cls._instance
    
    def __init__(self) :
        self.db_file = 'pp.dat'
        try:
            with sqlite3.connect(self.db_file) as self.conn:
                if self.conn is not None:
                    self.create_table()
                pass
        except sqlite3.Error as e:
            print(f"数据库错误: {e}")
    
    @staticmethod
    def getInstance():
        if DataUtils._instance is None:
            DataUtils()
        return DataUtils._instance
    
    def create_connection(self):
        """创建一个数据库连接到SQLite数据库"""
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(e)
        return conn

    def create_table(self):
        """创建数据表"""
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
        """更新或插入游戏数据到数据库"""
        cur = self.conn.cursor()
        # 检查表中是否已有数据
        cur.execute("SELECT COUNT(*) FROM game_data")
        if cur.fetchone()[0] == 0:
            # 如果没有数据，则插入
            sql = ''' INSERT INTO game_data(game_time,position,money)
                      VALUES(?,?,?) '''
            cur.execute(sql, (game_time, position, money))
        else:
            # 如果有数据，则更新
            sql = ''' UPDATE game_data
                      SET game_time=?, position=?, money=? '''
            cur.execute(sql, (game_time, position, money))
        self.conn.commit()

    def get_game_data(self):
        """获取游戏数据"""
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM game_data")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    def setGameTime(self, game_time):
        self.update_single_field("game_time", game_time)
    
    def addTime(self, days=0,hours=0,minutes=0):
        """增加特定的时间到game_time"""
        current_time_str = self.getTime()
        if current_time_str is not None:
            # 将字符串格式的时间转换为datetime对象
            current_time = datetime.strptime(current_time_str, "%Y-%m-%d %H:%M")
            # 计算新的时间
            new_time = current_time + timedelta(days=days,hours=hours,minutes=minutes)
            # 更新游戏时间
            self.set_game_time(new_time.strftime("%Y-%m-%d %H:%M"))
        else:
            print("当前没有可用的游戏时间来增加。")

    def setPosition(self, position:str):
        self.update_single_field("position", position)

    def setMoney(self, money):
        self.update_single_field("money", money)

    # General method to update a single field
    def update_single_field(self, field, value):
        cur = self.conn.cursor()
        sql = f''' UPDATE game_data
                  SET {field} = ?
                  WHERE rowid = 1 '''
        cur.execute(sql, (value,))
        self.conn.commit()

    def getTime(self):
        return self.get_single_field("game_time")

    def getPosition(self):
        return self.get_single_field("position")

    def getMoney(self):
        return self.get_single_field("money")

    def get_single_field(self, field):
        cur = self.conn.cursor()
        cur.execute(f"SELECT {field} FROM game_data WHERE rowid = 1")
        result = cur.fetchone()
        if result:
            return result[0]
        return None

    def closeConnection(self):
        """关闭数据库连接"""
        if self.conn:
            self.conn.close()
