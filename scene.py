import sys
from Controller import Controller
ctrl = Controller.getInstance()

def run():
    ctrl.setCurrentModule('scene')#在脚本文件第一个被调用的函数里设置当前脚本
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)#在每段剧情函数的开头保存当前函数名称
    ctrl.addStoryText('日的暖阳如同一位慈祥的母亲，轻轻地穿透窗帘，斑驳的光影投在你的床头，宛如一幅淡淡的油画，充满温馨之意。你睁开沉睡的双眼，眼角的余光捕捉到了这一切，心中不禁涌出一股淡淡的满足感。你伸出双臂，大大地伸了个懒腰，身体的每一根骨头仿佛都在欢快地跳舞。你的心情也被这舒适感染，懒洋洋的快乐涌上心头。你轻轻地笑着起来，放假在家，这真是人生中最美好的时刻，无忧无虑，享受着自己的小天地。作为一名大一的大学生，你现在正处于放假的阶段。放假之余，你就如同重生一般，可以摆脱学习的压力，摆脱课程的束缚，可以每天睡到自然醒，不用去赶那要人命的早课了。你可以感受到床铺的温度，感受到阳光的温度，还有老家的温度，这一切都无比舒适。')
    ctrl.stopForNextStep()
    ctrl.addStoryText('这位先生/女士,欢迎来到旅途乐章：春节版')
    ctrl.addButton("是的",lambda:(ctrl.addStoryText('我:',end='',color='red'),ctrl.addStoryText('当然!',color='blue'),ctrl.clearPanel(),plot1()))
    ctrl.addButton('yes',lambda:(ctrl.addStoryText('你说的没错'),ctrl.clearPanel(),plot1()))

def plot1():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addTime(days=1)
    ctrl.setPosition('家')
    if ctrl.getMoney() < 114514:
        ctrl.setMoney(114514.00)
    ctrl.addStoryText('这位同志，你好')
    ctrl.addEntry(plot1Callback,'你好')

def plot1Callback(text):
    ctrl.addStoryText(text)
    ctrl.clearPanel()
    #ctrl.stopForNextStep()
    ctrl.addStoryText('完了')
#run()