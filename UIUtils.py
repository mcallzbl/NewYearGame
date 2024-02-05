import tkinter as tk
from tkinter import scrolledtext
from DataUtils import DataUtils
import threading
import sys
import importlib
class UIUtils:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) :
        self.root = tk.Tk()
        self.root.title("旅途乐章：春节版")

        self.dataManager = DataUtils.getInstance()

         # 创建状态栏
        self.status_bar = tk.Frame(self.root, height=25, bg='grey')
        self.status_bar.pack(fill='x', side='top', anchor='w')

        # 在状态栏中添加Label显示信息
        self.time_label = tk.Label(self.status_bar, text=self.dataManager.getTime(), bg='grey')
        self.time_label.pack(side='left', padx=10)

        self.money_label = tk.Label(self.status_bar,  text="￥" + str(self.dataManager.getMoney()), bg='grey')
        self.money_label.pack(side='left', padx=10)

        self.location_label = tk.Label(self.status_bar, text="当前位置: " + self.dataManager.getPosition(), bg='grey')
        self.location_label.pack(side='left', padx=10)

        # 配置主窗口的grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        self.story_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=10)
        self.story_text.pack(pady=10)
        
        self.interactivePanel = tk.Frame(self.root)
        self.interactivePanel.pack(fill='x', side='bottom', anchor='w')

        self.event = threading.Event()
        self.thread = threading.Thread(target=self.runScript)
        self.thread.start()

        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)
    
    @staticmethod
    def getInstance():
        if UIUtils._instance is None:
            UIUtils()
        return UIUtils._instance
    
    def setTime(self, new_time:str):
        self.time_label.config(text=new_time)

    def setMoney(self, new_money):
        # 假设self.money_label是金钱标签的实例变量
        self.money_label.config(text="￥" + str(new_money))

    def addStoryText(self, text:str):
        self.story_text.insert(tk.END, text + "\n")
        self.story_text.see(tk.END)  # 自动滚动到新增内容的位置

    def showOn(self):
        self.root.mainloop()

    def addButton(self, button_text, on_click=None):
        button = tk.Button(self.interactivePanel, text=button_text, command=on_click)
        button.pack()
    
    def clearPanel(self):
        """清除面板上的所有元素"""
        for widget in self.interactivePanel.winfo_children():
            widget.destroy()

    def load_story_module(self,story_name):
        if story_name in sys.modules:
            # 如果模块已加载，先卸载它
            del sys.modules[story_name]
        # 动态加载指定的剧情脚本模块
        module = importlib.import_module(story_name)
        return module

    def runStory(self,story_name):
        story_module = self.load_story_module(story_name)
        #story_module.run_story() 

    def runScript(self):
        self.runStory('scene')
    
    def waitForInput(self):
        self.event.wait()

    def continueRun(self):
        self.event.set()

    def addEntry(self, submit_callback,placeholder_text=''):
        self.entry = tk.Entry(self.interactivePanel)
        self.entry.insert(0, placeholder_text)
        self.entry.pack(side='top', expand=True, fill='x')  # 使输入框自适应宽度
        self.addButton('发送',submit_callback)
    
    def getUserInput(self)->str:
        return self.entry.get()
    
    def stopThread(self):
        self.event = True
        self.thread.join()

    def onClosing(self):
        self.root.destroy()
        self.stopThread()
    
    def stopForNextStep(self):
        self.stopThread()
        self.addButton("继续",self.continueRun)
    