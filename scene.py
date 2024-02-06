import time
from UIUtils import UIUtils
from DataUtils import DataUtils
uiManager = UIUtils.getInstance()
dataManager = DataUtils.getInstance()

uiManager.addStoryText("欢迎来到旅行模拟器：春节特别版，希望你在这里玩的开心！")
uiManager.addStoryText('版本：v0.1')
def a():
    uiManager.addStoryText('冬日的暖阳如一位慈祥的母亲，轻轻地穿透了窗帘，斑驳的光影投在你的床头，就像一幅淡淡的油画，极尽温馨之意。你睁开沉睡的双眼，眼角的余光捕捉到这一切，心中不禁涌出一股淡淡的满足感。')
    uiManager.clearPanel()
    uiManager.continueRun()
    
uiManager.addButton('进入游戏',a)
uiManager.addButton('yes',lambda:(uiManager.clearPanel(),uiManager.addStoryText('他老牛b了'),uiManager.continueRun()))
uiManager.waitForInput()

uiManager.addButton('继续',lambda:(uiManager.clearPanel(),uiManager.continueRun()))
uiManager.waitForInput()
uiManager.addStoryText('你伸出双臂，大大地伸了个懒腰，身体的每一根骨头都仿佛在欢快地跳舞，你的心情也被这份舒适感染，一股懒洋洋的快乐涌上心头。你轻轻地笑了起来，哎，放假在家，这就是人生中最美好的一刻，无忧无虑，享受着属于自己的小天地。')
