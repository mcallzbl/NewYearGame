# Creation Date: 2024-02-07
# Last Modified Date: 2024-02-19
# version: 1.0
# Author: mcallzbl
# Copyright: Copyright (c) Youright Team. All rights reserved.

import re
import sys
import time
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel,QMainWindow,QPushButton
from PyQt6.QtCore import QMetaObject,Qt,pyqtSlot
from PyQt6.QtGui import QFont, QFontDatabase,QTextCharFormat, QColor,QIcon,QTextCursor
from DataUtils import DataUtils 
import pygame
import os
import threading
import importlib
import queue
class UIUtils(QMainWindow):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(UIUtils, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self._initUI()
    
    #初始化UI
    def _initUI(self):
        self.setWindowTitle("旅途乐章：春节版")
        self.resize(800, 600)
        self.dataManager = DataUtils.getInstance()
        self.setWindowIcon(QIcon(os.path.join(self.dataManager.getResourcePath(),'Resource/icon')))
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.mainLayout = QHBoxLayout(centralWidget)
        self.rightPanel = QWidget()
        self.rightPanelLayout = QVBoxLayout(self.rightPanel)

        self._initStoyText()
        self._initStatusBar()
        self._initInteractivePanel()
        self._initMusic()
        
        self.queue = queue.Queue()
        self.isPaused = False
        self.immediate_output = False
        self.running = True
        self.thread = None
        self.color_pattern = re.compile(r'#([A-Fa-f0-9]{6})')

        
    
    #初始化故事文本
    def _initStoyText(self):
        fontID = QFontDatabase.addApplicationFont(os.path.join(self.dataManager.getResourcePath(),'Resource/font1'))
        fontFamilies = QFontDatabase.applicationFontFamilies(fontID)
        font = QFont(fontFamilies[0],20)

        self.storyWidget = QWidget()
        self.storyLayout = QVBoxLayout(self.storyWidget)
        self.story_text = QTextEdit()
        self.story_text.setFont(font)
        self.story_text.setReadOnly(True)
        self.storyLayout.addWidget(self.story_text)
        self.story_text.verticalScrollBar().valueChanged.connect(self._loadMoreHistory)
    
    #初始化状态栏
    def _initStatusBar(self):
        # 状态标签
        self.status_bar = QWidget()
        self.status_layout = QVBoxLayout(self.status_bar)
        self.status_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.time_label = QLabel()
        self.setTime(self.dataManager.getTime())
        fontID = QFontDatabase.addApplicationFont(os.path.join(self.dataManager.getResourcePath(),'Resource/font2'))
        fontFamilies = QFontDatabase.applicationFontFamilies(fontID)
        font = QFont(fontFamilies[0],25)
        self.time_label.setFont(font)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.status_layout.addWidget(self.time_label)

        self.money_label = QLabel()
        self.setMoney(self.dataManager.getMoney())
        fontID = QFontDatabase.addApplicationFont(os.path.join(self.dataManager.getResourcePath(),'Resource/font2'))
        fontFamilies = QFontDatabase.applicationFontFamilies(fontID)
        font = QFont(fontFamilies[0],15)
        self.money_label.setFont(font)
        self.money_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.status_layout.addWidget(self.money_label)

        self.location_label = QLabel()
        self.setPosition(self.dataManager.getPosition())
        fontID = QFontDatabase.addApplicationFont(os.path.join(self.dataManager.getResourcePath(),'Resource/font2'))
        fontFamilies = QFontDatabase.applicationFontFamilies(fontID)
        font = QFont(fontFamilies[0],15)
        self.location_label.setFont(font)
        self.location_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.status_layout.addWidget(self.location_label)
        self.rightPanelLayout.addWidget(self.status_bar)

    #初始化交互面板
    def _initInteractivePanel(self):
        self.interactivePanel = QWidget()
        self.interactiveLayout = QVBoxLayout(self.interactivePanel)
        self.rightPanelLayout.addWidget(self.interactivePanel)
        self.mainLayout.addWidget(self.storyWidget, 8)
        self.mainLayout.addWidget(self.rightPanel, 2)
    
    #初始化背景音乐
    def _initMusic(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(self.dataManager.getResourcePath(),'Resource/'+self.dataManager.getMusic()))
        pygame.mixer.music.play(-1) 

    #在交互区添加一个输入框
    def addEntry(self, submit_callback, placeholder_text=''):
        container = QWidget()
        layout = QHBoxLayout()
        entry = QTextEdit(self.interactivePanel)
        entry.setPlaceholderText(placeholder_text)
        entry.setStyleSheet("""
            QTextEdit {
                border: 2px solid #a9a9a9;
                border-radius: 10px;
                min-height : 30px;
                max-height : 30px;
                padding: 5px; 
            }
        """)

        layout.addWidget(entry)
        submitButton = QPushButton("发送", self.interactivePanel)
        submitButton.clicked.connect(lambda: self.runMethod(lambda: submit_callback(entry.toPlainText())))
        submitButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; 
                color: white; 
                min-height: 30px;
                border-style: solid;
                border-width: 2px;
                border-radius: 10px; 
                border-color: #4CAF50;
                padding: 6px; 
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(submitButton)
        container.setLayout(layout)
        layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.interactiveLayout.addWidget(container)

    #添加UI操作任务
    def add_task(self, task):
        self.queue.put(task)
        self._processQueue()

    #写入故事文本
    def addStoryText(self, text, end='\n', color='black', add_to_top=False):
        cursor = self.story_text.textCursor()
        default_format = self.createCharFormat(color)
        if add_to_top:
            cursor.movePosition(QTextCursor.MoveOperation.Start)
            self.setImmediateOutput()
        else:
            cursor.movePosition(QTextCursor.MoveOperation.End)
            self.skipText()
        self.story_text.setTextCursor(cursor)
        position_before_insertion = cursor.position() if add_to_top else None

        text_position = 0
        for char, format in self.parseText(text, default_format):
            if not self.running:
                break
            cursor.insertText(char, format)
            self.story_text.ensureCursorVisible()
            if not self.immediate_output:
                QApplication.processEvents()
                time.sleep(0.1)
            text_position += 1

        cursor.insertText(end, format)

        if add_to_top and position_before_insertion is not None:
            cursor.setPosition(position_before_insertion)
            cursor.movePosition(QTextCursor.MoveOperation.Down)

        if not add_to_top:
            self.clearInteractivePanel()
        self.offImmediateOutput()
        self.story_text.ensureCursorVisible()
        self.continueRun()
    
    #加载历史文本
    def loadInitialHistory(self):
        while not self.story_text.verticalScrollBar().isVisible():
            more_history = self._getMoreHistory()
            if more_history == None:
                break
            else :
                self.addStoryText(more_history,add_to_top=True)
            if self.story_text.verticalScrollBar().maximum() > 0:
                break 

    #处理UI操作任务
    @pyqtSlot()
    def process_queue(self):
        while not self.isPaused and not self.queue.empty():
            try:
                task = self.queue.get_nowait()
                task()
            except Exception as e:
                pass

    #调用UI操作
    def _processQueue(self):
        QMetaObject.invokeMethod(self._instance,"process_queue", Qt.ConnectionType.QueuedConnection)
    
    #更换背景音乐
    def changeMusic(self,newMusic):
        fadeout_duration = 500
        pygame.mixer.music.fadeout(fadeout_duration)
        while pygame.mixer.music.get_busy():
            pygame.time.delay(100)
        new_music_path = os.path.join(self.dataManager.getRelativePath(),'Resource/'+newMusic)
        pygame.mixer.music.load(new_music_path)
        pygame.mixer.music.play(-1)
    
    #设置文本立即输出
    def setImmediateOutput(self):
        self.immediate_output = True
    
    #关闭文本立即输出
    def offImmediateOutput(self):
        self.immediate_output = False

    #获取UIUtil实例
    @staticmethod
    def getInstance():
        if UIUtils._instance is None:
            UIUtils()
        return UIUtils._instance
    
    #当滚动条滚动到最上面时，加载历史
    def _loadMoreHistory(self, value):
        if value == self.story_text.verticalScrollBar().minimum():
            more_history = self._getMoreHistory()
            if more_history != None:
                self.add_task(lambda:self.addStoryText(more_history,add_to_top=True))

    #从数据库中读取历史
    def _getMoreHistory(self):
        history = self.dataManager.load_history(1)
        self.dataManager.increase_offset(1)
        if len(history) == 1:
            return history[0][1]
        else :
            return None 

    #根据颜色创建Format
    def createCharFormat(self, color_code):
        format = QTextCharFormat()
        if color_code.startswith('#'):
            red, green, blue = int(color_code[1:3], 16), int(color_code[3:5], 16), int(color_code[5:], 16)
            format.setForeground(QColor(red, green, blue))
        else:
            format.setForeground(QColor(color_code))
        return format

    #解析文本
    def parseText(self, text, default_format):
        buffer = ''
        format = default_format
        for char in text:
            if char == '#' and not buffer:
                buffer = '#'
            elif buffer:
                buffer += char
                if len(buffer) == 7:
                    format = self.getCharFormatFromBuffer(buffer, default_format)
                    buffer = ''
                    yield ('', format)
                elif len(buffer) > 7:
                    yield from self.yieldBufferedText(buffer[:-1], default_format)
                    char, buffer = buffer[-1], ''
            else:
                yield (char, format)

        if buffer:
            yield from self.yieldBufferedText(buffer, default_format)  

    def yieldBufferedText(self, buffer, default_format):
        for buffered_char in buffer:
            yield (buffered_char, default_format)      

    #获取格式
    def getCharFormatFromBuffer(self, buffer, default_format):
        match = self.color_pattern.match(buffer)
        if match:
            return self.createCharFormat(match.group(0))
        else:
            return default_format

    #在交互区添加一个按钮
    def addButton(self, button_text, on_click=None):
        button = QPushButton(button_text, self.interactivePanel)
        button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; 
                color: white; 
                border-style: solid;
                border-width: 2px;
                min-height: 40px;
                border-radius: 10px; 
                border-color: #4CAF50;
                padding: 6px; 
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        
        if on_click:
            button.clicked.connect(lambda:self.runMethod(on_click))
        self.interactiveLayout.addWidget(button)

    #加载故事模块
    def load_story_module(self,story_name):
        if story_name in sys.modules:
            del sys.modules[story_name]
        module = importlib.import_module(story_name)
        return module

    #运行指定脚本
    def runScript(self,script,function):
        print(script+function)
        story_module = self.load_story_module(script)
        self.thread = threading.Thread(target=getattr(story_module,function))
        self.thread.start()
        
    def changeScript(self,script,function):
        if self.thread.is_alive():
            self.thread.join()
        self.runScript(script,function)

    #运行指定函数
    def runMethod(self,method):
        self.thread.join()
        self.thread = threading.Thread(target=method)
        self.thread.start()

    #添加跳过按钮
    def skipText(self):
        self.addButton("跳过",lambda:(self.setImmediateOutput(),self.clearInteractivePanel))
        self.waitForInput()

    #让线程停止
    def stopThread(self):
        self.thread.join()

    #设置屏幕上显示的UI
    def setTime(self,newTime:str):
        self.time_label.setText(newTime[5:])

    #设置屏幕上显示的金钱数
    def setMoney(self,newMoney):
        self.money_label.setText("<span style = 'font-size:20pt;'>￥</span> " + str(newMoney))
    
    #设置屏幕上显示的位置
    def setPosition(self,newPosition:str):
        self.location_label.setText('当前位置:'+newPosition)

    #窗口关闭时调用
    def closeEvent(self, event):
        pygame.mixer.music.stop()
        pygame.quit()
        self.stopThread()
        self.close()
        event.accept()
        self.running = False

    #展示窗口
    def showOn(self):
        self.show()
        self.loadInitialHistory()
        self.runScript(self.dataManager.getScript(),self.dataManager.getFunction())
        sys.exit(self.app.exec())

    #暂停等待输入
    def waitForInput(self):
        self.isPaused = True    

    #继续执行
    def continueRun(self):
        self.isPaused = False
        QMetaObject.invokeMethod(self, "process_queue", Qt.ConnectionType.QueuedConnection)

    #清除交互面板上全部组件
    def clearInteractivePanel(self):
        while self.interactiveLayout.count():
            widget = self.interactiveLayout.takeAt(0).widget()  
            if widget is not None: 
                widget.deleteLater()

                