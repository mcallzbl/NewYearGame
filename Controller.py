# Creation Date: 2024-02-07
# Last Modified Date: 2024-02-19
# version: 1.0
# Author: mcallzbl
# Copyright: Copyright (c) Youright Team. All rights reserved.

import os
import queue
from DataUtils import DataUtils
from UIUtils import UIUtils
from datetime import datetime, timedelta
class Controller:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) :
        self.dataManager = DataUtils.getInstance()
        self.uiManager = UIUtils.getInstance()
        self.messageQueue = queue.Queue()
    
    @staticmethod
    def getInstance():
        if Controller._instance is None:
            Controller()
        return Controller._instance
    
    def write_texts_to_database(self):
        while not self.messageQueue.empty():
            message = self.messageQueue.get()
            self.dataManager.insert_message(message)
            self.dataManager.increase_offset(1)
    
    def add_text_to_queue(self,text:str):
        self.messageQueue.put(text)
    
    def addButton(self,text,on_click):
        self.uiManager.add_task(lambda:self.uiManager.addButton(text,on_click))

    def addStoryText(self, text:str, end='\n', color='black'):
        self.add_text_to_queue(text)
        self.addButton("跳过",lambda:(self.setImmediateOutput()))
        self.uiManager.add_task(lambda:(self.uiManager.waitForInput(),self.uiManager.addStoryText(text,end,color)))
        self.uiManager.add_task(lambda:self.uiManager.clearInteractivePanel())

    def addTime(self, days=0, hours=0, minutes=0, seconds=0):
        current_time_str = self.getTime()
        if current_time_str is not None:
            try:
                # 尝试按照包含秒的格式解析时间
                current_time = datetime.strptime(current_time_str, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    # 如果失败，尝试按照不包含秒的格式解析时间
                    current_time = datetime.strptime(current_time_str, "%Y-%m-%d %H:%M")
                except ValueError:
                    print("无法解析的时间格式")
                    return
            # 添加时间
            new_time = current_time + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
            # 如果原始时间字符串包含秒，那么新的时间字符串也应该包含秒
            if ":00" in current_time_str:
                self.setTime(new_time.strftime("%Y-%m-%d %H:%M:%S"))
            else:
                self.setTime(new_time.strftime("%Y-%m-%d %H:%M"))
        else:
            print("当前没有可用的游戏时间来增加。")

    def waitForInput(self):
        self.uiManager.add_task(lambda: self.uiManager.waitForInput())

    def continueRun(self):
        self.uiManager.continueRun()

    def clearPanel(self):
        self.uiManager.clearInteractivePanel()
        #self.uiManager.add_task(lambda:self.uiManager.clearInteractivePanel())

    def addEntry(self, submit_callback=None, placeholder_text=''):
        self.uiManager.add_task(lambda:self.uiManager.addEntry(submit_callback,placeholder_text))

    def stopForNextStep(self):
        self.addButton("继续",lambda:(self.uiManager.clearInteractivePanel(),self.continueRun()))
        self.waitForInput()

    def setImmediateOutput(self):
        self.uiManager.setImmediateOutput()

    def setTime(self,newTime:str):
        self.uiManager.setTime(newTime)
        self.dataManager.setGameTime(newTime)

    def addMoney(self,money):
        self.setMoney(self.getMoney+money)

    def setMoney(self,newMoney):
        self.uiManager.add_task(lambda:self.uiManager.setMoney(newMoney))
        self.dataManager.setMoney(newMoney)

    def setPosition(self,newPosition:str):
        self.uiManager.add_task(lambda:self.uiManager.setPosition(newPosition))
        self.dataManager.setPosition(newPosition)

    def setMusic(self,newMusic:str):
        self.dataManager.setMusic(newMusic)
        self.uiManager.add_task(lambda:self.uiManager.changeMusic(newMusic))

    def setCurrentModule(self,module:str):
        self.dataManager.setScript(module)

    def setCurrentProgress(self,progress:str):
        self.write_texts_to_database()
        self.dataManager.setFunction(progress)

    def getTime(self)->str:
        return self.dataManager.getTime()
    
    def getMoney(self):
        return self.dataManager.getMoney()

    def getPosition(self)->str:
        return self.dataManager.getPosition()
    
    def appendToFile(self,filename,line_to_append):
        path = os.path.join(self.dataManager.getRelativePath(),filename)
        with open(path, 'a', encoding='utf-8') as file:
            file.write(line_to_append + '\n')

    def readTolist(self,filename):
        path = os.path.join(self.dataManager.getRelativePath(),filename)
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]

    def changeScript(self,newScript:str,newFunction:str):
        self.setCurrentModule(newScript)
        self.setCurrentProgress(newFunction)
        self.uiManager.add_task(lambda:self.uiManager.changeScript(newScript,newFunction))

    def addAboutUsButton(self):
       # self.addButton('关于我们',)
        while not self.messageQueue.empty():
            self.messageQueue.get()
        #self.uiManager.add_task(lambda:self.dataManager.reCreateDB())
        self.dataManager.offset = 0
        self.uiManager.add_task(lambda:self.uiManager.addButton('关于我们',lambda:(self.uiManager.about_us(),self.uiManager.clearStory(),self.clearPanel()),immediate=True))
        
        