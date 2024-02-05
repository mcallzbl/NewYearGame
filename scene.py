from UIUtils import UIUtils
from DataUtils import DataUtils
uiManager = UIUtils.getInstance()
dataManager = DataUtils.getInstance()

uiManager.addStoryText("shanxinyi太牛逼了")
uiManager.addStoryText('这位客人，你是否认为单新意的智慧天下无双？')
def a():
    uiManager.addStoryText('是的，我认为他是神')
    uiManager.continueRun()

uiManager.addButton('是的',a)
uiManager.addButton('yes',lambda:(uiManager.addStoryText('他老牛b了'),uiManager.continueRun()))
uiManager.waitForInput()
uiManager.clearPanel()