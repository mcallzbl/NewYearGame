# Date 2024-02-08
# version 1.0
# by mcallzbl
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel,QMainWindow,QPushButton,QLineEdit
from PyQt6.QtCore import QMetaObject,Qt,pyqtSlot
from PyQt6.QtGui import QFont, QFontDatabase,QTextCharFormat, QColor
from DataUtils import DataUtils 
# from Controller import Controller
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
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("旅途乐章：春节版")
        self.resize(800, 600)
        self.dataManager = DataUtils.getInstance()
        # self.ctrl = Controller.getInstance()

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        mainLayout = QHBoxLayout(centralWidget)
        
        # 故事文本
        fontID = QFontDatabase.addApplicationFont(os.path.join(self.dataManager.getRelativePath(),'Resource/font1'))
        fontFamilies = QFontDatabase.applicationFontFamilies(fontID)
        font = QFont(fontFamilies[0],20)

        self.storyWidget = QWidget()
        self.storyLayout = QVBoxLayout(self.storyWidget)
        self.story_text = QTextEdit()
        self.story_text.setFont(font)
        self.story_text.setReadOnly(True)
        self.storyLayout.addWidget(self.story_text)
        
        # 状态和交互面板容器
        self.rightPanel = QWidget()
        self.rightPanelLayout = QVBoxLayout(self.rightPanel)
        
        # 状态标签
        self.status_bar = QWidget()
        self.status_layout = QVBoxLayout(self.status_bar)
        self.status_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.time_label = QLabel()
        self.setTime(self.dataManager.getTime())
        fontID = QFontDatabase.addApplicationFont(os.path.join(self.dataManager.getRelativePath(),'Resource/font2'))
        fontFamilies = QFontDatabase.applicationFontFamilies(fontID)
        font = QFont(fontFamilies[0],25)
        self.time_label.setFont(font)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.status_layout.addWidget(self.time_label)

        self.money_label = QLabel()
        self.setMoney(self.dataManager.getMoney())
        fontID = QFontDatabase.addApplicationFont(os.path.join(self.dataManager.getRelativePath(),'Resource/font2'))
        fontFamilies = QFontDatabase.applicationFontFamilies(fontID)
        font = QFont(fontFamilies[0],15)
        self.money_label.setFont(font)
        self.money_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.status_layout.addWidget(self.money_label)

        self.location_label = QLabel()
        self.setPosition(self.dataManager.getPosition())
        fontID = QFontDatabase.addApplicationFont(os.path.join(self.dataManager.getRelativePath(),'Resource/font2'))
        fontFamilies = QFontDatabase.applicationFontFamilies(fontID)
        font = QFont(fontFamilies[0],15)
        self.location_label.setFont(font)
        self.location_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.status_layout.addWidget(self.location_label)

        self.rightPanelLayout.addWidget(self.status_bar)
        
        # 交互面板
        self.interactivePanel = QWidget()
        self.interactiveLayout = QVBoxLayout(self.interactivePanel)
        self.rightPanelLayout.addWidget(self.interactivePanel)

        # 将故事文本区域和右侧面板添加到主布局
        mainLayout.addWidget(self.storyWidget, 8)  # 左侧故事文本区域，比例为7
        mainLayout.addWidget(self.rightPanel, 2)   # 右侧状态和交互面板，比例为3

        #背景音乐
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(self.dataManager.getRelativePath(),'Resource/bgm'))
        pygame.mixer.music.play(-1) 

        self.event = threading.Event()
        self.thread = threading.Thread(target=self.runScript)
        self.thread.start()
        self.queue = queue.Queue()

    @pyqtSlot()
    def process_queue(self):
        try:
            task = self.queue.get_nowait()
            task()
        except Exception as e:
            pass

    def add_task(self, task):
        self.queue.put(task)
        QMetaObject.invokeMethod(self._instance,"process_queue", Qt.ConnectionType.QueuedConnection)

    @staticmethod
    def getInstance():
        if UIUtils._instance is None:
            UIUtils()
        return UIUtils._instance

    def addStoryText(self, text, end='\n', color='black'):
        cursor = self.story_text.textCursor()
        format = QTextCharFormat()
        format.setForeground(QColor(color))
        cursor.insertText(text+end, format)
        self.story_text.ensureCursorVisible()

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
            button.clicked.connect(on_click)
        self.interactiveLayout.addWidget(button)

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
       # self.interactiveLayout.addWidget(entry)
        submitButton = QPushButton("发送", self.interactivePanel)
        submitButton.clicked.connect(lambda: submit_callback(entry.toPlainText()))
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

    def load_story_module(self,story_name):
        if story_name in sys.modules:
            del sys.modules[story_name]
        module = importlib.import_module(story_name)
        return module

    def runStory(self,story_name):
        story_module = self.load_story_module(story_name)
        #story_module.run_story() 

    def runScript(self):
        self.runStory('scene')

    def runMethod(self,method):
        self.thread.join()
        self.thread = threading.Thread(target=method)
        self.thread.start()

    def stopThread(self):
        self.event.set()
        self.thread.join()

    def setTime(self,newTime:str):
        self.time_label.setText(newTime[5:])

    def setMoney(self,newMoney):
        self.money_label.setText("<span style = 'font-size:20pt;'>￥</span> " + str(newMoney))

    def setPosition(self,newPosition:str):
        self.location_label.setText('当前位置:'+newPosition)

    def closeEvent(self, event):
        pygame.mixer.music.stop()
        pygame.quit()
        self.stopThread()
        self.close()
        event.accept()

    def showOn(self):
        self.show()
        sys.exit(self.app.exec())

    def waitForInput(self):
        self.event.wait()

    def continueRun(self):
        self.event.set()
        self.event.clear()

    def clearInteractivePanel(self):
        for i in reversed(range(self.interactiveLayout.count())):
            widget = self.interactiveLayout.itemAt(i).widget()
            if widget is not None: 
                widget.deleteLater()