# Date 2024-02-08
# version 1.0
# by mcallzbl
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
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("旅途乐章：春节版")
        self.resize(800, 600)
        self.dataManager = DataUtils.getInstance()
        self.setWindowIcon(QIcon(os.path.join(self.dataManager.getResourcePath(),'Resource/icon')))
        # self.ctrl = Controller.getInstance()

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        mainLayout = QHBoxLayout(centralWidget)
        
        # 故事文本
        fontID = QFontDatabase.addApplicationFont(os.path.join(self.dataManager.getResourcePath(),'Resource/font1'))
        fontFamilies = QFontDatabase.applicationFontFamilies(fontID)
        font = QFont(fontFamilies[0],20)

        self.storyWidget = QWidget()
        self.storyLayout = QVBoxLayout(self.storyWidget)
        self.story_text = QTextEdit()
        self.story_text.setFont(font)
        self.story_text.setReadOnly(True)
        self.storyLayout.addWidget(self.story_text)
        self.story_text.verticalScrollBar().valueChanged.connect(self.loadMoreHistory)
        
        # 状态和交互面板容器
        self.rightPanel = QWidget()
        self.rightPanelLayout = QVBoxLayout(self.rightPanel)
        
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
        
        # 交互面板
        self.interactivePanel = QWidget()
        self.interactiveLayout = QVBoxLayout(self.interactivePanel)
        self.rightPanelLayout.addWidget(self.interactivePanel)

        mainLayout.addWidget(self.storyWidget, 8)
        mainLayout.addWidget(self.rightPanel, 2)

        #背景音乐
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(self.dataManager.getResourcePath(),'Resource/bgm'))
        pygame.mixer.music.play(-1) 
        
        self.queue = queue.Queue()
        self.isPaused = False
        self.immediate_output = False
        self.running = True
        self.color_pattern = re.compile(r'#([A-Fa-f0-9]{6})')
    
    def loadInitialHistory(self):
        while not self.story_text.verticalScrollBar().isVisible():
            more_history = self.getMoreHistory()
            if more_history == None:
                break
            else :
                self.addStoryText(more_history,add_to_top=True)
            if self.story_text.verticalScrollBar().maximum() > 0:
                break 

    @pyqtSlot()
    def process_queue(self):
        while not self.isPaused and not self.queue.empty():
            try:
                task = self.queue.get_nowait()
                task()
            except Exception as e:
                pass

    def processQueue(self):
        QMetaObject.invokeMethod(self._instance,"process_queue", Qt.ConnectionType.QueuedConnection)

    def add_task(self, task):
        self.queue.put(task)
        self.processQueue()

    def setImmediateOutput(self):
        self.immediate_output = True
    
    def offImmediateOutput(self):
        self.immediate_output = False

    @staticmethod
    def getInstance():
        if UIUtils._instance is None:
            UIUtils()
        return UIUtils._instance
    
    def loadMoreHistory(self, value):
        if value == self.story_text.verticalScrollBar().minimum():
            more_history = self.getMoreHistory()
            if more_history != None:
                self.add_task(lambda:self.addStoryText(more_history,add_to_top=True))

    def getMoreHistory(self):
        history = self.dataManager.load_history(1)
        self.dataManager.increase_offset(1)
        if len(history) == 1:
            return history[0][1]
        else :
            return None 

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
        self.finalizeTextAddition()

    def createCharFormat(self, color_code):
        format = QTextCharFormat()
        if color_code.startswith('#'):
            red, green, blue = int(color_code[1:3], 16), int(color_code[3:5], 16), int(color_code[5:], 16)
            format.setForeground(QColor(red, green, blue))
        else:
            format.setForeground(QColor(color_code))
        return format

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

    def getCharFormatFromBuffer(self, buffer, default_format):
        match = self.color_pattern.match(buffer)
        if match:
            return self.createCharFormat(match.group(0))
        else:
            return default_format
        
    def finalizeTextAddition(self):
        self.offImmediateOutput()
        self.story_text.ensureCursorVisible()
        self.continueRun()

    # def addStoryText(self, text, end='\n', color='black'):
    #     cursor = self.story_text.textCursor()
    #     default_format = QTextCharFormat()
    #     default_format.setForeground(QColor(color))
    #     color_pattern = re.compile(r'#([A-Fa-f0-9]{6})')

    #     buffer = '' 
    #     format = default_format 

    #     self.skipText() 
    #     text_position = 0
    #     for char in text:
    #         if not self.running:
    #             break
    #         if char == '#' and not buffer:
    #             buffer = '#' 
    #         elif buffer:
    #             buffer += char  
    #             if len(buffer) == 7: 
    #                 match = color_pattern.match(buffer)
    #                 if match:
    #                     color_code = match.group(0)
    #                     red = int(color_code[1:3], 16)
    #                     green = int(color_code[3:5], 16)
    #                     blue = int(color_code[5:], 16)
    #                     format = QTextCharFormat()  
    #                     format.setForeground(QColor(red, green, blue))
    #                     buffer = '' 
    #                 else:
    #                     for buffered_char in buffer[:-1]: 
    #                         cursor.insertText(buffered_char, default_format)
    #                     char = buffer[-1] 
    #                     buffer = char 
    #         else:
    #             cursor.insertText(char, format)  
    #             self.story_text.ensureCursorVisible()
    #             QApplication.processEvents()
    #             if not self.immediate_output:
    #                 time.sleep(0.1)
    #         text_position += 1
    #     if buffer:
    #         cursor.insertText(buffer, default_format)
    #     cursor.insertText(end, format)
    #     self.offImmediateOutput()
    #     self.story_text.ensureCursorVisible()
    #     self.clearInteractivePanel()
    #     self.continueRun()

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

    def load_story_module(self,story_name):
        if story_name in sys.modules:
            del sys.modules[story_name]
        module = importlib.import_module(story_name)
        return module

    def runScript(self,script,function):
        story_module = self.load_story_module(script)
        self.thread = threading.Thread(target=getattr(story_module,function))
        self.thread.start()

    def runMethod(self,method):
        self.thread.join()
        self.thread = threading.Thread(target=method)
        self.thread.start()

    def skipText(self):
        self.addButton("跳过",lambda:(self.setImmediateOutput(),self.clearInteractivePanel))
        self.waitForInput()

    def stopThread(self):
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
        self.running = False

    def showOn(self):
        self.show()
        self.loadInitialHistory()
        self.runScript(self.dataManager.getScript(),self.dataManager.getFunction())
        sys.exit(self.app.exec())

    def waitForInput(self):
        self.isPaused = True    

    def continueRun(self):
        self.isPaused = False
        QMetaObject.invokeMethod(self, "process_queue", Qt.ConnectionType.QueuedConnection)

    def clearInteractivePanel(self):
        while self.interactiveLayout.count():
            widget = self.interactiveLayout.takeAt(0).widget()  
            if widget is not None: 
                widget.deleteLater()

                