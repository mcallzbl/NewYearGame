import sys
from Controller import Controller
ctrl = Controller.getInstance()

def run():
    ctrl.setCurrentModule('scene')#在脚本文件第一个被调用的函数里设置当前脚本
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)#在每段剧情函数的开头保存当前函数名称
    ctrl.addStoryText('这位先生/女士,请问您是否认同伟大的神明单新意是宇宙中最聪慧的？')
    ctrl.addButton("是的",lambda:(ctrl.addStoryText('我:',end='',color='red'),ctrl.addStoryText('当然!',color='blue'),ctrl.clearPanel(),plot1()))
    ctrl.addButton('yes',lambda:(ctrl.addStoryText('你说的没错'),ctrl.clearPanel(),plot1()))

def plot1():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addTime(days=1)
    ctrl.setPosition('卧槽')
    if ctrl.getMoney() < 114514:
        ctrl.setMoney(114514.00)
    ctrl.addStoryText('这位同志，你好啊')
    ctrl.addEntry(plot1Callback,'你好啊')

def plot1Callback(text):
    ctrl.addStoryText(text)
    ctrl.clearPanel()
    ctrl.stopForNextStep()
    #ctrl.addStoryText('完了')
run()