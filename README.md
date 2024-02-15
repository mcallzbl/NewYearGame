# NewYearGame

安装环境
pip install -r requirements.txt



首先需要获取Controller实例

```python
from Controller import Controller
ctrl = Controller.getInstance()
```

注意事项:
现在剧情脚本里不需要手动调用run()函数
在显示文本的同时右侧会显示按钮，这时点击按钮会造成进度不协调，比如在左侧正在输出的文本中插入下一段文字，目前最好的解决办法是在响应事件中加入立即输出
操作数据

```python
1.获取游戏时间
ctrl.getTime()
返回时间的字符串

2.设置游戏时间
ctrl.setTime(newTime)
参数是字符串
需要以YYYY-MM-DD HH:MM:SS为格式，建议用addTime()来操作时间

3.快进时间
ctrl.addTime(days=0,hours=0,minutes=0)
将游戏时间快进
参数默认都是0，建议使用参数名传参

4.获取位置
ctrl.getPosition()
返回当前位置

5.设置位置
ctrl.setPosition(position)

6.获取金钱数
ctrl.getMoney()

7.设置金钱数
ctrl.setMoney(money)

8.在脚本文件第一个被调用的函数里设置当前脚本
ctrl.setCurrentModule('scene')

9.在每段剧情函数的开头保存当前函数名称
ctrl.setCurrentProgress(sys._getframe().f_code.co_name)

8和9是用来记录游戏进度的，目前还未实现


```

然后就是与UI交互的接口

```python
1.增加一段文本
ctrl.addStoryText( text, end='\n', color='black')

默认以回车结尾，如果需要拼接则可传入end参数
color可以使用#RRGGBB码

2.暂停执行脚本以等待用户输入
ctrl.waitForInput()
如果脚本完全使用函数，则可不必使用

3.继续执行脚本
ctrl.continueRun()
同上

4.添加一个按钮
ctrl.addButton(button_text，on_click)
先需要一个按钮上显示的文字，然后传入按钮被点击后需要执行的函数
若未使用纯函数的情况下，应当在按钮添加完毕后，暂停来等待输入，回调函数中应调用continueRun()来让脚本继续执行
注：on_click应当传入lambda表达式

5.ctrl.stopForNextStep()
这个函数是用来等待用户按下“继续”按钮再往下执行，用于在显示多段文字之间的暂停
如果使用纯函数方式，它目前会导致程序无响应，不要用

6.添加用户输入框
ctrl.addEntry(submit_callback,placeholder_text='')
第一个参数是传入回调函数，用于执行用户点击发送按钮后的操作,注意，回调函数需要有一个参数，用来承接输入框中的内容
第二个参数是提示文字
调用这个函数会自动生成一个发送按钮

7.清除输入面板上的一切
ctrl.clearPanel()
交互面板是显示按钮或输入框的地方，每次获取过用户输入之后，都应该使用它来把按钮之类的东西清除掉

8.立即将该段文本输出完毕
ctrl.setImmediateOutput()
```

