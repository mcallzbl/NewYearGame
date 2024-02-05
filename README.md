# NewYearGame

```python
首先需要获取操作UI和数据的实例
from UIUtils import UIUtils
from DataUtils import DataUtils
uiManager = UIUtils.getInstance()
dataManager = DataUtils.getInstance()
```

首先是操作数据的接口（以下是在与存档文件进行交互）

```python
1.获取游戏时间
dataManager.getTime()
返回时间的字符串

2.设置游戏时间
dataManager.setGameTime(game_time)
参数是字符串

3.快进时间
dataManager.addTime(days=0,hours=0,minutes=0)
将游戏时间快进
参数默认都是0，建议使用参数名传参

4.获取位置
dataManager.getPosition()
返回当前位置

5.设置位置
dataManager.setPosition(position)

6.获取金钱数
dataManager.getMoney()

7.设置金钱数
dataManager.setMoney(money)


```

然后就是与UI交互的接口

```python
1.设置显示的时间
uiManager.setTime(new_time)

2.设置显示的金钱数
uiManager.setMoney(new_money)

3.增加一行文本
uiManager.addStoryText(text)

4.暂停执行脚本以等待用户输入
uiManager.waitForInput()

5.继续执行脚本
uiManager.continueRun()

6.添加一个按钮
uiManager.addButton(button_text，on_click)
先需要一个按钮上显示的文字，然后传入按钮被点击后需要执行的函数
应当在按钮添加完毕后，暂停来等待输入，回调函数中应调用continueRun()来让脚本继续执行

7.uiManager.stopForNextStep()
这个函数是用来等待用户按下“继续”按钮再往下执行，用于在显示多段文字之间的暂停

8.添加用户输入框
uiManager.addEntry(submit_callback,placeholder_text='')
第一个参数是传入一个函数，用于执行用户点击发送按钮后的操作
第二个参数是提示文字

9.获取输入框的文字
uiManager.getUserInput()
需要用这个函数来获取用户所输入的内容

10.清除输入面板上的一切
uiManager.clearPanel()
输入面板是显示按钮或输入框的地方，每次获取过用户输入之后，都应该使用它来把按钮之类的东西清除掉
```

