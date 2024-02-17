# Date 2024-02-08
# version 1.0
# by mcallzbl
import os
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
    
    @staticmethod
    def getInstance():
        if Controller._instance is None:
            Controller()
        return Controller._instance
    
    def addButton(self,text,on_click):
        self.uiManager.add_task(lambda:self.uiManager.addButton(text,on_click))

    def addStoryText(self, text, end='\n', color='black'):
        self.uiManager.add_task(lambda:self.uiManager.addStoryText(text,end,color))

    def addTime(self, days=0,hours=0,minutes=0):
        current_time_str = self.getTime()
        if current_time_str is not None:
            current_time = datetime.strptime(current_time_str, "%Y-%m-%d %H:%M")
            new_time = current_time + timedelta(days=days,hours=hours,minutes=minutes)
            self.setTime(new_time.strftime("%Y-%m-%d %H:%M"))
        else:
            print("当前没有可用的游戏时间来增加。")

    def waitForInput(self):
        self.uiManager.add_task(lambda: self.uiManager.waitForInput())

    def continueRun(self):
        self.uiManager.continueRun()

    def clearPanel(self):
        self.uiManager.clearInteractivePanel()
        # self.uiManager.add_task(lambda:self.uiManager.clearInteractivePanel())

    def addEntry(self, submit_callback=None, placeholder_text=''):
        self.uiManager.add_task(lambda:self.uiManager.addEntry(submit_callback,placeholder_text))

    def stopForNextStep(self):
        self.addButton("继续",lambda:(self.uiManager.clearInteractivePanel(),self.continueRun()))
        self.waitForInput()

    def setImmediateOutput(self):
        self.uiManager.setImmediateOutput()

    def setTime(self,newTime):
        self.uiManager.add_task(lambda:self.uiManager.setTime(newTime))
        self.dataManager.setGameTime(newTime)

    def setMoney(self,newMoney):
        self.uiManager.add_task(lambda:self.uiManager.setMoney(newMoney))
        self.dataManager.setMoney(newMoney)

    def setPosition(self,newPosition):
        self.uiManager.add_task(lambda:self.uiManager.setPosition(newPosition))
        self.dataManager.setPosition(newPosition)

    def setCurrentModule(self,module):
        self.dataManager.setScript(module)

    def setCurrentProgress(self,progress):
        self.dataManager.setFunction(progress)

    def getTime(self)->str:
        return self.dataManager.getTime()
    
    def getMoney(self):
        return self.dataManager.getMoney()

    def getPosition(self):
        return self.dataManager.getPosition()
    
    def append_line_to_file(self,filename,line_to_append):
        path = os.path.join(self.dataManager.getRelativePath(),filename)
        with open(path, 'a', encoding='utf-8') as file:
            file.write(line_to_append + '\n')

    def read_file_to_list(self,filename):
        path = os.path.join(self.dataManager.getRelativePath(),filename)
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]


    