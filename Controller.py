# Date 2024-02-08
# version 1.0
# by mcallzbl
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
        self.uiManager.waitForInput()

    def continueRun(self):
        self.uiManager.continueRun()

    def clearPanel(self):
        self.uiManager.add_task(lambda:self.uiManager.clearInteractivePanel())

    def addEntry(self, submit_callback=None, placeholder_text=''):
        self.uiManager.add_task(lambda:self.uiManager.addEntry(submit_callback,placeholder_text))

    def stopForNextStep(self):
        self.addButton("继续",lambda:self.uiManager.continueRun())
        self.waitForInput()

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
        pass

    def setCurrentProgress(self,progress):
        pass

    def getTime(self)->str:
        return self.dataManager.getTime()
    
    def getMoney(self):
        return self.dataManager.getMoney()

    def getPosition(self):
        return self.dataManager.getPosition()
    