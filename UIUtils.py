# Date 2024-2-07-12
# version 1.0
# by mcallzbl
import tkinter as tk 
from tkinter import ttk
from tkinter import scrolledtext
from ttkthemes import ThemedTk
from DataUtils import DataUtils
import threading
import sys,os
import importlib
import queue
import pygame
class UIUtils:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) :
        self.root = ThemedTk(theme='arc')
        self.root.title("旅途乐章：春节版")

        self.dataManager = DataUtils.getInstance()

        self.root.grid_rowconfigure(0, weight=0) 
        self.root.grid_rowconfigure(1, weight=7) 
        self.root.grid_rowconfigure(2, weight=3) 

        # 状态栏
        self.status_bar = ttk.Frame(self.root, height=25)
        self.status_bar.grid(row=0, column=0, sticky='ew')
        self.root.grid_columnconfigure(0, weight=1)

        # 状态栏内的标签 - 使用grid而非pack
        self.time_label = ttk.Label(self.status_bar, text=self.dataManager.getTime())
        self.time_label.grid(row=0, column=0, padx=10)

        self.money_label = ttk.Label(self.status_bar, text="￥" + str(self.dataManager.getMoney()))
        self.money_label.grid(row=0, column=1, padx=10)

        self.location_label = ttk.Label(self.status_bar, text="当前位置: " + self.dataManager.getPosition())
        self.location_label.grid(row=0, column=2, padx=10)
        
        # 故事文本
        self.story_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.story_text.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        self.story_text.config(state='disabled')
        
        # 交互面板
        self.interactivePanel = ttk.Frame(self.root)
        self.interactivePanel.grid(row=2, column=0, sticky='ew')
        self.root.grid_rowconfigure(2, weight=1)

        self.event = threading.Event()
        self.thread = threading.Thread(target=self.runScript)
        self.thread.start()
        self.queue = queue.Queue()
        self.root.after(100,self.process_queue)

        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(self.dataManager.getRelativePath(),'Resource/bgm'))
        # 播放音乐
        pygame.mixer.music.play(-1)  # 参数-1表示循环播放

    
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
        def addTextToUI(text):
            self.story_text.config(state='normal')
            self.story_text.insert(tk.END, text + "\n")
            self.story_text.see(tk.END) 
            self.story_text.config(state='disabled')
        self.queue.put(lambda:addTextToUI(text))
    
    def process_queue(self):
        try:
            task = self.queue.get_nowait()
            task()
            self.root.after(0, self.process_queue)
        except Exception as e:
            pass
            #print(e)
        finally:
            self.root.after(100, self.process_queue)

    def showOn(self):
        self.root.mainloop()

    def addButton(self, button_text, on_click=None):
        def addButtonToUI(button_text, on_click):
            button = ttk.Button(self.interactivePanel, text=button_text, command=on_click)
            button.pack()
        self.queue.put(lambda:addButtonToUI(button_text=button_text, on_click=on_click))
    
    def clearPanel(self):
        def clearPanelOnUI():
            for widget in self.interactivePanel.winfo_children():
                widget.destroy()
        self.queue.put(lambda:clearPanelOnUI())

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
        self.event.clear()

    def addEntry(self, submit_callback,placeholder_text=''):
        self.entry = ttk.Entry(self.interactivePanel)
        self.entry.insert(0, placeholder_text)
        self.entry.pack(side='top', expand=True, fill='x')  # 使输入框自适应宽度
        self.addButton('发送',submit_callback)
    
    def getUserInput(self)->str:
        return self.entry.get()
    
    def stopThread(self):
        self.event.set()
        self.thread.join()

    def onClosing(self):
        self.root.destroy()
        self.stopThread()
        pygame.mixer.music.stop()
        pygame.quit()
    
    def stopForNextStep(self):
        self.waitForInput()
        self.addButton("继续",self.continueRun)
    