from Controller import Controller
ctrl = Controller.getInstance()

ctrl.addStoryText("欢迎来到旅行模拟器：春节特别版，希望你在这里玩的开心！",end='')
ctrl.addStoryText('版本：v0.1')
ctrl.addStoryText('\n')
ctrl.addStoryText("单新意太牛逼了",color='blue')
ctrl.addStoryText('这位客人，你是否认为单新意的智慧天下无双？')
ctrl.addTime(days=1)
print(ctrl.getPosition())
