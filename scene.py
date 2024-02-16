import sys
from Controller import Controller
ctrl = Controller.getInstance()

def run():
    ctrl.setCurrentModule('scene')#在脚本文件第一个被调用的函数里设置当前脚本
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)#在每段剧情函数的开头保存当前函数名称
    ctrl.addStoryText('欢迎来到“旅行模拟器：春节特别版！')
    ctrl.addButton("进入游戏",lambda:(ctrl.clearPanel(),getup()))
   

def getup():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
   
    ctrl.setPosition('卧室中')
    if ctrl.getMoney() < 114514:
        ctrl.setMoney(114514.00)
    ctrl.addStoryText('#4CAF50冬日的暖阳如同一位慈祥的母亲，轻轻地穿透窗帘，斑驳的光影投在你的床头，宛如一幅淡淡的油画，充满温馨之意。')
    ctrl.addStoryText('你睁开沉睡的双眼，眼角的余光捕捉到了这一切，心中不禁涌出一股淡淡的满足感。你伸出双臂，大大地伸了个懒腰，身体的每一根骨头仿佛都在欢快地跳舞。你的心情也被这舒适感染，懒洋洋的快乐涌上心头。')
    ctrl.addButton("起床",lambda:(ctrl.clearPanel(),get_up_at_once()))
    ctrl.addButton("再睡一会",lambda:(ctrl.clearPanel(),continue_sleep()))

def continue_sleep():
    ctrl.addStoryText("你又一次闭上了眼睛，哎，这么好的时间怎么能不拿来睡觉呢？")
    ctrl.addStoryText("过了不知多久，你又一次睁开双眼，发现你的妈妈正站在你的床前。")
    ctrl.addStoryText('"你醒了？"她笑着说，"现在已经是十点了，小懒虫别睡了，快点起床吧。虽然放假了，但是也不能如此作息不规律呀，昨天晚上是不是又熬夜了？"')
   
    ctrl.addButton("起床", lambda: (ctrl.clearPanel(), get_up_at_once()))

def get_up_at_once():
    ctrl.addStoryText("你掀开被子坐了起来，等自己清醒了几分后起身下床，穿好衣服后走出了你的卧室。")
    ctrl.addStoryText("今天是周末，你的爸爸妈妈都在家休息。你的爸爸妈妈现在正坐在客厅的沙发里，你的妈妈在看一本都市小说，而你的爸爸则在刷着手机，浏览着某些网页。")
    ctrl.addButton("前去洗漱", lambda: (ctrl.clearPanel(), next_scene()))

def next_scene():
    ctrl.addStoryText("洗漱完毕后，你进入了客厅，坐在了餐桌旁，准备找一些吃的。")
    ctrl.addStoryText("你找到了几块面包，又拿了一瓶酸奶，坐在餐桌旁开始吃。")
    ctrl.addStoryText("你发现你的爸爸妈妈好像在谋划着什么事情，于是你好奇地问道，'爸妈，你们在干嘛？'")
    ctrl.addButton("询问爸妈", lambda: (ctrl.clearPanel(), ask_parents()))

def ask_parents():
    ctrl.addStoryText("你的爸爸向你挥了挥他的手机，'最近哈尔滨的冰雪大世界又一次走红，我想着我们能不能假期也去那儿玩一玩呢？'")
    ctrl.addStoryText("'好啊，那去哪儿玩呢？'")
    ctrl.addStoryText("你的爸爸说，'最近哈尔滨的冰雪大世界又一次走红了，今年的各种活动筹备比往年做得更好，我们可以去那儿玩一玩。'")
    ctrl.addStoryText("你的妈妈说：'要是嫌太冷的话，咱们也可以去趟海南，回孩子他姥爷家玩玩。'")
    plan_vacation()

def plan_vacation():
    ctrl.addStoryText("选择：去哈尔滨/去海南")
    ctrl.addButton("去哈尔滨", lambda: (ctrl.clearPanel(), go_to_harbin()))
    ctrl.addButton("去海南", lambda: (ctrl.clearPanel(), go_to_hainan()))

def go_to_harbin():
    ctrl.addStoryText("你想了想说道，'确实，今年哈尔滨的文旅宣传做得相当好，据说今年投入冰雪大世界运营的资金是往年的好几倍呢。我的朋友圈和抖音也快要被哈尔滨刷屏了，要不我们这个假期也去一趟？'")
    choose_transportation() 

def go_to_hainan():
    ctrl.addStoryText("'我有个老叔什么时候去海南了？'你的爸爸说，'你老叔跟他的朋友合伙在海南投资了一座果汁厂，现在正在生产椰汁。他在那边干了不久便成功买下了一套房子，前几天他说等你放假了就带你一起，一家人来海南玩几天。'")
    ctrl.addStoryText("'好啊,'你的妈妈说，'正好我也想去海南。'")
    choose_transportation()

def choose_transportation():
    ctrl.addStoryText("你爸爸说行那那就这么定了，今年咱们也体验一把游历春节的潮流！我看看出行方式。")
    ctrl.addStoryText("选择坐高铁或坐飞机或坐绿皮火车")
    ctrl.addButton("坐飞机", lambda: (ctrl.clearPanel(), choose_flight()))
    ctrl.addButton("坐高铁", lambda: (ctrl.clearPanel(), choose_high_speed_train()))
    ctrl.addButton("坐绿皮火车", lambda: (ctrl.clearPanel(), choose_train()))

def choose_flight():
    ctrl.addStoryText("你对你的爸爸说把咱们坐飞机吧，飞机更方便更快。")
    ctrl.addStoryText("你的妈妈说哎呀还是坐高铁吧，高铁更快更安全还能欣赏一路上的风光。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), success_in_get_ticket()))

def choose_high_speed_train():
    ctrl.addStoryText("你对你的爸爸说爸咱们坐高铁吧，高铁更快更安全并且还能欣赏一路上的风光。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), success_in_get_ticket()))

def choose_train():
    ctrl.addStoryText("你对你的爸爸说爸咱们坐绿皮火车吧，体验一下慢节奏的旅行。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), success_in_get_ticket()))
      
def success_in_get_ticket():
    ctrl.addStoryText('你的爸爸打开了高铁12306并开始查询相应的车票。过了一会儿他高兴地拍了拍手说好了我已经成功地抢到了三张票，时间是2月8号早上7点40从新民北站发车前往叉叉叉。你妈妈慢点起来说好啊我已经迫不及待了。')
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), plan_vacation_days()))

def plan_vacation_days():
    ctrl.addStoryText("现在是1月19日，距离旅游还有一段时间，你寻思着假期该怎么安排呢？")
    night_before_departure()

def night_before_departure():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("时间飞逝，很快到了2月7日的晚上。家里的气氛格外热闹，你们一家人围坐在客厅里，一边检查装好的行李，一边讨论着第二天的出行细节。")
    ctrl.addStoryText("“明天的火车是早上7点40分，我们最好7点前20前就到北站。”爸爸说，一边检查着票务信息。")
    ctrl.addStoryText("“我准备了一些小吃和水果，可以在火车上吃。”妈妈从厨房拿出一袋零食，放在行李旁边。")
    ctrl.addButton("检查个人物品", lambda: (ctrl.clearPanel(), check_personal_items()))
    ctrl.addButton("询问是否需要带其他东西", lambda: (ctrl.clearPanel(), ask_if_need_to_bring_other_items()))

def check_personal_items():
    ctrl.addStoryText("你决定再次检查自己的背包，确保所有必需品都已经打包。你确认了手机充电器、耳机、阅读材料以及旅行必备的药物都已经放在了容易拿取的位置。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), prepare_for_tomorrow()))

def ask_if_need_to_bring_other_items():
    ctrl.addStoryText("你看着父母忙碌的身影，问道，“还有什么我可以帮忙准备的吗？”妈妈想了想，说，“去看看洗漱包，牙膏和牙刷都准备好了吗？”你立刻去卫生间检查洗漱包，确保一切洗漱用品齐全。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), prepare_for_tomorrow()))

def prepare_for_tomorrow():
    ctrl.addStoryText("最终，一切准备就绪，你们决定早点休息，以便第二天能精神饱满地出发。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), early_morning()))

def early_morning():
    ctrl.addStoryText("2月8日清晨5点，天空还未完全亮起。家中的闹钟准时响起，打破了宁静的清晨。你们迅速起床，进行最后的准备。穿上简单舒适的衣服，双肩背上行李，你们三人便出发了。")
    ctrl.addStoryText("外面的空气带着清冷，但家中温暖的记忆和即将开始的旅行让你感到兴奋。爸爸开车，妈妈在副驾驶座上检查着物品，而你，坐在后座上，通过窗户看着城市逐渐苏醒。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), arrival_at_train_station()))

def arrival_at_train_station():
    ctrl.addStoryText("车子在清晨的街道上行驶，没有平日的喧嚣，一切都显得格外宁静。在爸爸熟练的驾驶下，你们在6点50分到达了新民北站。车站前已经有了其他旅客的身影，大家都带着期待的表情，准备开始自己的旅程。")
    ctrl.addButton("进站安检", lambda: (ctrl.clearPanel(), enter_station_security_check()))
    ctrl.addButton("在站台外稍作休息", lambda: (ctrl.clearPanel(), rest_outside_station()))

def enter_station_security_check():
    ctrl.addStoryText("你们决定尽早进站，以免赶时间。安检过程井然有序，不一会儿，你们就通过了安检，来到了候车大厅。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), wait_for_train()))

def rest_outside_station():
    ctrl.addStoryText("你们找了个靠近入口的长椅坐下，看着来来往往的人群。爸爸提醒，“我们不要休息太久，还是早点进站比较好。”")
    ctrl.addButton("进站安检", lambda: (ctrl.clearPanel(), enter_station_security_check()))

def wait_for_train():
    ctrl.addStoryText("不久后，你们站起身，带着行李，踏入了高铁站内。随着列车的到来，你们的旅程即将拉开序幕。这不仅是一场跨越千里的旅行，更是一段家人共度的宝贵时光。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), onboard_train()))

def onboard_train():
    # ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("登上站台，你发现已经有很多人在排队了。你和爸爸妈妈按顺序排起了队，等待高铁的到来。")
    ctrl.addStoryText("“四号站台有列车进入，四号站台有列车进入”伴随着广播的声音响起，一列“和谐号”高铁动车组徐徐驶入站台。")
    ctrl.addStoryText("妈妈问：“咱们是哪节车厢来着？”你掏出手机，点开了“铁路12306”。")
    # ctrl.addTextInput("请输入你的车厢和座位信息：", submit_seat_info)
    sit_down()
def submit_seat_info(seat_info):
    ctrl.addStoryText(f"你、你的爸爸和你的妈妈登上了对应的车厢，开始寻找属于你们的座位。{seat_info}……你找到了指定的座位，但是发现那里已经有人了。")
    ctrl.addButton("再次查看12306上的座位信息", lambda: (ctrl.clearPanel(), check_seat_info_again()))
    ctrl.addButton("上前询问", lambda: (ctrl.clearPanel(), ask_in_person()))

def check_seat_info_again():
    ctrl.addStoryText("你又一次打开了12306，找到了座位信息，发现他们坐的就是你们的位置。")
    ctrl.addButton("上前询问", lambda: (ctrl.clearPanel(), ask_in_person()))

def ask_in_person():
    ctrl.addTextInput("请输入你的询问内容：", submit_inquiry)

def submit_inquiry(inquiry):
    if "请" in inquiry or "谢谢" in inquiry or "能" in inquiry:
        ctrl.addStoryText("他们查看了自己的座位信息，发现他们坐错了位置，于是说到”哎呀，不好意思啊小伙子，我们坐错位置了“。")
        ctrl.addButton("落座", lambda: (ctrl.clearPanel(), sit_down()))
    else:
        ctrl.addStoryText("老人给我上了一课。")
        ctrl.addButton("落座", lambda: (ctrl.clearPanel(), sit_down_unpleasant()))

def sit_down():
    ctrl.addStoryText("你和父母坐到了自己的座位上，开始享受这次旅行。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), start_journey()))

def sit_down_unpleasant():
    ctrl.addStoryText("你心里闷闷不乐，没有跟你的爸爸妈妈说一句话。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), start_journey()))

def start_journey():
    ctrl.addStoryText("高铁启动了，广播提示音响起：“欢迎乘坐本次列车！本次列车的始发站是沈阳北站，终到站是广州站，途经北京、上海、长沙等城市，全程预计耗时15小时，请各位乘客注意安全，祝您旅途愉快。”")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), enjoy_the_scenery()))

def enjoy_the_scenery():
    ctrl.addStoryText("海南，我们来了！")
    ctrl.addStoryText("随着新民北站那悠长而振奋人心的汽笛声在晨曦微光中嘹亮奏响，你与父母携手迈开了这场跨越中国南北、直指海南岛的梦幻之旅。高铁车厢内明亮宽敞且设施完备，座椅设计融入了人性化考量，每一寸空间都精心雕琢以确保旅途中最大程度的舒适体验，每一个细节之处无不彰显出现代交通科技的便捷高效。车窗外的世界如同一部缓缓拉开序幕的纪录片，伴随着列车的疾速奔驰，不断变换着一幅幅生动的画面，讲述着华夏大地的丰富多样和地域变迁。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), arrival_in_hainan()))

def arrival_in_hainan():
    ctrl.addStoryText("次日清晨，曙光初照，列车驶过了陆地的最后一段距离，当它稳稳跨过桥梁的一刹那，眼前的视野豁然开朗，海天一线的壮观景象令人惊艳不已。这是你首次如此亲密地感受到大海那无边无际的辽阔，碧波万顷中，浪花翻滚跳跃，仿佛是海洋以其热烈的姿态张开宽广的怀抱，热情欢迎远方的客人。当你终于踏上这片湿润而温暖的海南土地，感受着咸涩清新的海风轻轻拂过脸颊，那种属于海洋的独特气息深深地烙印在心中，成为你对这个热带天堂最初也是最深刻的印象。这一全新的开始，昭示着一段充满奇妙冒险与惊喜发现的旅程就此揭开华丽的篇章。")
    ctrl.addButton("进入梦乡", lambda: (ctrl.clearPanel(), new_day_in_hainan()))

def new_day_in_hainan():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("清晨，海浪拍打着沙滩，如音乐般唤醒你的梦境。你伸手拿起旁边的手机，瞟了一眼时钟，早上6点30分。在家的话，你可能还会继续贪睡一会儿。但此刻，充满了期待和兴奋的心情让你立刻清醒 — 因为，你们即将踏上美丽的海南岛，度过美好的假期！")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), breakfast()))

def breakfast():
    ctrl.addStoryText("在选择中，你迈开步伐进入新的一天：起床洗漱和享用早餐。你穿上轻松的度假装，开始悠然洗漱。洗漱一新后，你与父母一同来到酒店的餐厅。琳琅满目的早餐自助台上摆放着各类美食，咖啡香气弥漫在空气中。品尝着美味的海鲜，你们目送外面的美景，享受阳光的拥抱。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), visit_volcano_park()))

def visit_volcano_park():
    ctrl.addStoryText("早餐过后，你们回到房间，整理行李，并搭乘出租车前往渡口。渡船的声音独特而动听，在码头平稳地停泊。你们扛着行李，踏上了往返海南的渡船。不久后，渡船发出启航的汽笛声，载着一船的旅客向海南岛驶去。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), arrival_in_hainan()))

def arrival_in_hainan():
    ctrl.addStoryText("啊，海南！期待和兴奋充满着你的内心。这座岛屿究竟蕴含着怎样的魅力，将揭晓在你脚下的征程中。接着你们的海南之旅，计划中的下一站是火山口国家地质公园，一个以熔岩岩洞和火山遗迹为特色的自然景观。你们一家人早早地从酒店出发，准备前往这个大自然的奇妙造物。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), explore_volcano_park()))

def explore_volcano_park():
    ctrl.addStoryText("进入火山口国家地质公园，一片原始森林气息扑面而来。高大的热带树木遮天蔽日，偶尔可以看到几缕阳光透过密集的树冠洒落下来。你深深地吸了一口清新的空气，感到身心都为之一振。")
    ctrl.addButton("探索熔岩隧道", lambda: (ctrl.clearPanel(), explore_lava_tunnel()))
    ctrl.addButton("登顶火山口", lambda: (ctrl.clearPanel(), climb_to_volcano_crater()))

def explore_lava_tunnel():
    ctrl.addStoryText("你们跟随着导游的步伐，走进了一条熔岩隧道。隧道内部凉爽湿润，墙壁上的岩石纹路记录着火山曾经的狂暴。导游详细地讲解着这些岩石的形成过程，你听得津津有味。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), after_volcano_park()))

def climb_to_volcano_crater():
    ctrl.addStoryText("你们决定挑战一下自己，登上火山口。虽然火山已经沉寂许久，但登顶的过程仍然令人兴奋。沿途可以看到各种火山喷发形成的岩石和火山灰，这些都是大自然力量的见证。")
    ctrl.addButton("拍摄全景照片", lambda: (ctrl.clearPanel(), take_panoramic_photo()))
    ctrl.addButton("录制旅行Vlog", lambda: (ctrl.clearPanel(), record_travel_vlog()))

def take_panoramic_photo():
    ctrl.addStoryText("你拿出手机，打开全景模式，慢慢地转动身体，捕捉360度的火山口美景。这张照片将会是一份珍贵的纪念，记录下你们一家在海南的美好时光。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), after_volcano_park()))

def record_travel_vlog():
    ctrl.addStoryText("你打开相机，开始录制你们的旅行Vlog。首先，你对着镜头介绍这个火山口的历史和地质意义。然后，你转向你的父母，让他们分享一下登顶的感受。你的父母略带羞涩地站在镜头前，但很快就被你的鼓励所感染，开始讲述他们的感受和这次旅行的意义。录制结束后，你知道这将是一个很好的纪念片段，记录你们一家人共同经历的冒险。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), after_volcano_park()))

def after_volcano_park():
    ctrl.addStoryText("午后的阳光开始变得柔和，你们结束了在火山口国家地质公园的探险，带着满满的收获和美好的记忆，返回了酒店。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), evening_in_hainan()))

def evening_in_hainan():
    ctrl.addStoryText("在酒店休息片刻之后，你们决定去海边看日落。海南的海边在傍晚时分特别迷人，金色的阳光洒在波光粼粼的海面上，海浪轻轻拍打着沙滩，发出宁静而又悦耳的声音。")
    ctrl.addButton("沿着海边散步", lambda: (ctrl.clearPanel(), walk_along_beach()))
    ctrl.addButton("找个好位置拍摄日落", lambda: (ctrl.clearPanel(), take_sunset_photo()))

def walk_along_beach():
    ctrl.addStoryText("你们赤脚踩在细软的沙滩上，沿着海岸线慢慢散步。海风轻拂过脸颊，带来一丝凉爽。你们在沙滩上留下了一串串脚印，就像是在这片海域留下了自己的印记。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), dinner()))

def take_sunset_photo():
    ctrl.addStoryText("你找到了一个视野开阔的位置，架好相机，等待日落的那一刻。随着太阳缓缓下沉，天空的颜色从蓝变成了橘黄，然后是深红和紫色，美得令人窒息。你按下快门，捕捉了这一刻的美丽。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), dinner()))

def dinner():
    ctrl.addStoryText("日落之后，天色渐渐暗淡下来，你们在海边的一家餐厅享用晚餐。餐后，你们回到酒店，结束了这充实而又愉快的一天。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), end_of_day()))

def end_of_day():
    ctrl.addStoryText("这天晚上，你躺在床上，回想着一天的经历，感到无比满足。你知道，这次海南之旅将会是你一生中难忘的记忆之一。你带着对接下来几天旅程的期待，渐渐进入了梦乡。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), second_day_in_hainan()))


def second_day_in_hainan():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("第二天的阳光在海口骑楼老街的瓷砖上反射出温暖的光芒，你和家人早早地出发，准备探索这个充满历史故事的地方。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), visit_old_street()))

def visit_old_street():
    ctrl.addStoryText("你们走在被称为“博爱路”的老街上，爸爸指着一座骑楼说：“看，这些骑楼是海口的灵魂，它们见证了这座城市的变迁。”妈妈则兴奋地拿出相机，记录下这些具有东南亚风情的建筑。骑楼的每一处细节都让你们驻足欣赏，从精致的雕饰到色彩斑斓的彩瓷，每一幅图案都仿佛在诉说着一个古老的故事。")
    ctrl.addButton("参观历史悠久的四牌楼", lambda: (ctrl.clearPanel(), visit_four_archways()))
    ctrl.addButton("逛一逛老街的特色店铺", lambda: (ctrl.clearPanel(), visit_specialty_shops()))

def visit_four_archways():
    ctrl.addStoryText("你们来到了四牌楼前，这座建筑历经600多年风雨，依旧屹立在这里。导游详细地讲解了四牌楼的历史背景，以及它在海南文化中的重要地位。你们还得知，这里是海口骑楼老街的标志性建筑，也是一处不可多得的摄影地点。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), take_family_photo()))

def visit_specialty_shops():
    ctrl.addStoryText("你们漫步在老街上，每一家店铺都有其独特的魅力。你们走进一家售卖手工艺品的店铺，店内摆满了各式各样的工艺品，每一件都是手工制作，充满了海南的地方特色。")
    ctrl.addButton("买一些纪念品", lambda: (ctrl.clearPanel(), buy_souvenirs()))
    ctrl.addButton("和店主学习制作工艺品", lambda: (ctrl.clearPanel(), learn_handicraft_with_shopkeeper()))

def take_family_photo():
    ctrl.addStoryText("参观结束后，你们决定在四牌楼前拍一张全家福，留下这难忘的时刻。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), afternoon_in_hainan()))

def buy_souvenirs():
    ctrl.addStoryText("你挑选了一些精美的手工艺品作为纪念品，包括一些独特的彩瓷摆件和手绘扇子。你知道这些不仅能作为旅行的纪念，也可以作为送给朋友的独特礼物。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), afternoon_in_hainan()))

def learn_handicraft_with_shopkeeper():
    ctrl.addStoryText("店主是一个热情的海南阿姨，见你们对手工艺品感兴趣，便邀请你们体验制作。你们在她的指导下，尝试了制作简单的手工饰品。虽然第一次手工不太熟练，但在阿姨的鼓励下，你们还是做出了几件小巧的手工艺品，这个过程充满了乐趣。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), afternoon_in_hainan()))

def afternoon_in_hainan():
    ctrl.addStoryText("午后的阳光开始变得温柔，你们在骑楼下的长廊中找了一家评价很高的咖啡馆坐下来，享受一杯香浓的咖啡。妈妈说：“这就是海口人的生活，慢节奏，享受每一刻。”你们一边品味咖啡，一边观察着街上的行人，感受着这个城市独有的气息。")
    ctrl.addButton("在咖啡馆里休息一会儿", lambda: (ctrl.clearPanel(), rest_in_cafe()))
    ctrl.addButton("继续探索老街其他区域", lambda: (ctrl.clearPanel(), continue_exploring_old_street()))

def rest_in_cafe():
    ctrl.addStoryText("你们在咖啡馆里休息，享受轻松的氛围。你打开笔记本，记录下今天的所见所闻，这些文字将成为旅行的美好回忆。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), evening_in_haikou()))

def continue_exploring_old_street():
    ctrl.addStoryText("你们离开咖啡馆，继续在老街上漫步。每走过一段，就有不同的惊喜出现。你们还尝试了一些当地的小吃，比如海南粉和清补凉，这些美食让你们的味蕾也经历了一次旅行。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), evening_in_haikou()))

def evening_in_haikou():
    ctrl.addStoryText("夜幕降临时，海口骑楼老街变得更加热闹。路灯逐渐亮起，老街上的霓虹灯也开始闪烁。你们在这灯火辉煌中结束了一天的探索，带着满满的收获和愉悦的心情返回酒店。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), third_day_in_hainan()))


def third_day_in_hainan():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("第三天，阳光明媚，一家人早早地来到了海口市的绿肺——万绿园。这个占地约83公顷的公园，不仅是海口市最大的开放性热带海滨生态园林风景区，也是市民休闲运动的理想场所。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), visit_green_park()))

def visit_green_park():
    ctrl.addStoryText("你们首先来到了大门区，入口处的热带植物造型迎接着每一位游客。爸爸建议：“这么多景区，我们可以分头行动，然后分享各自看到的美景。”")
    ctrl.addButton("分头行动", lambda: (ctrl.clearPanel(), split_up()))
    ctrl.addButton("一起行动", lambda: (ctrl.clearPanel(), stick_together()))

def split_up():
    ctrl.addStoryText("你决定前往竹林区，而爸爸妈妈则去了内湖区。在茂密的竹林中，你感受到了一股清新的气息，绿色的竹叶在阳光下闪闪发光，你不由得拿出手机记录下这一刻。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), meet_calligrapher()))

def meet_calligrapher():
    ctrl.addStoryText("在竹林深处，你偶遇了一位正在练习书法的老先生，他看上去颇有些高人之姿。")
    ctrl.addButton("观看老先生书法", lambda: (ctrl.clearPanel(), watch_calligraphy()))
    ctrl.addButton("邀请老先生一起参观", lambda: (ctrl.clearPanel(), invite_calligrapher()))

def watch_calligraphy():
    ctrl.addStoryText("你静静地站在一旁，看着老先生挥毫泼墨，每一笔每一划都透露着力与美的结合。老先生注意到了你的兴趣，便问你是否想尝试一下。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), parents_experience()))

def invite_calligrapher():
    ctrl.addStoryText("你上前与老先生攀谈，并邀请他一起游览万绿园。老先生微笑着接受了，他带你走到了一些不为人知的园中秘境，讲述了许多关于万绿园的故事。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), parents_experience()))

def stick_together():
    ctrl.addStoryText("你们决定一起行动，共同探索万绿园的每一个景点。你们一边欣赏着美景，一边分享着各自的感受，这种亲密的家庭氛围让旅行变得更加有意义。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), parents_experience()))

def parents_experience():
    ctrl.addStoryText("与此同时，爸爸妈妈在内湖区享受着湖面的宁静，水面上偶尔有几只水鸟掠过，悠然自得。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), afternoon_in_wanlvyuan()))

def afternoon_in_wanlvyuan():
    ctrl.addStoryText("午后，你们在草坪区汇合，一起分享了各自的经历。妈妈拿出了她拍摄的内湖美景，而你则展示了老先生送你的书法作品。")
    ctrl.addButton("在草坪上休息", lambda: (ctrl.clearPanel(), rest_on_lawn()))
    ctrl.addButton("去儿童游乐区体验游乐设施", lambda: (ctrl.clearPanel(), visit_playground()))

def rest_on_lawn():
    ctrl.addStoryText("你们找了个舒适的地方，铺开野餐布，享受着自带的小食。微风吹过，带来海边的咸味，让这个午后的休息时间更添几分惬意。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), evening_in_wanlvyuan()))

def visit_playground():
    ctrl.addStoryText("尽管名为“儿童游乐区”，但里面的设施却也吸引了大人们的注意。你们一起尝试了旋转木马和迷你过山车，尽情地回味童年的乐趣。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), evening_in_wanlvyuan()))

def evening_in_wanlvyuan():
    ctrl.addStoryText("傍晚时分，一家人在热带观赏植物区散步，万绿园的夜晚别有一番风味。灯光下的植物显得更加生动，夜晚的花香也格外浓郁。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), end_of_day_in_wanlvyuan()))

def end_of_day_in_wanlvyuan():
    ctrl.addStoryText("在万绿园度过了一个充满活力和宁静的一天后，你们满载而归，心中充满了对大自然的敬畏和对家庭时光的珍惜。这一天的经历，无疑成为了旅途中的一段美好回忆。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), fourth_day_in_hainan()))

def fourth_day_in_hainan():
    ctrl.addStoryText("随着高铁缓缓驶入三亚站，一家人迎来了他们在“东方夏威夷”——亚龙湾的精彩一天。亚龙湾以其“天下第一湾”的美誉，吸引了世界各地的游客，而今天，它将以其碧海、蓝天、柔软的沙滩、清新的空气和温暖的阳光迎接你们。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), visit_yalong_bay()))

def visit_yalong_bay():
    ctrl.addStoryText("一出站，阳光洒在你们的脸上，你感受到了海南特有的热带风情。爸爸提议：“亚龙湾的海滩是最美的，我们先去那里吧。”妈妈则兴奋地想要去看看那些华丽的酒店，而你对亚龙湾的自然风光充满了期待。")
    ctrl.addButton("直接去海滩", lambda: (ctrl.clearPanel(), go_directly_to_beach()))
   
def go_directly_to_beach():
    ctrl.addStoryText("你们决定先沉浸在亚龙湾美丽的海滩中。沙滩上的沙子细腻柔软，如同踏在细糖上，海水清澈透明，可以清晰地看到脚下的小鱼在游弋。你们找了一个靠近水边的地方，铺开沙滩毯，准备享受一天的海滩时光。")
    ctrl.addButton("阳光浴", lambda: (ctrl.clearPanel(), sunbathe()))
    ctrl.addButton("海水浴", lambda: (ctrl.clearPanel(), swim()))

def sunbathe():
    ctrl.addStoryText("你躺在沙滩上，闭上眼睛，感受着阳光在你的皮肤上跳跃。微风拂过，带来海水的咸味和远处椰林的清香。你听着海浪轻轻拍打沙滩的声音，感觉像是大自然在播放它最悠扬的乐章。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), afternoon_in_yalong_bay()))

def swim():
    ctrl.addStoryText("你迫不及待地跑向海水，浪花亲吻着你的脚踝，冷凉而清新。你深呼吸一口海风中的咸湿气息，然后一头扎进波光粼粼的海浪中。水中的世界静谧而神秘，五彩斑斓的鱼儿在你身边来回穿梭，仿佛在欢迎你的到来。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), afternoon_in_yalong_bay()))

def afternoon_in_yalong_bay():
    ctrl.addStoryText("在享受了一段美好的海水浴后，你回到沙滩上，看到爸爸妈妈也同样享受着海水的清凉。你们互相嬉戏，偶尔还会相互泼洒海水，笑声融入海风，成为亚龙湾上的另一道美丽风景。")
    ctrl.addStoryText("午后，阳光开始变得温柔，你们决定去探索亚龙湾的其他美景。沿着海滩行走，椰影婆娑，你们来到了一片红树林。这里的红树林生长在清澈的海水中，根部交错形成了独特的自然景观。")
    ctrl.addButton("探索红树林", lambda: (ctrl.clearPanel(), explore_mangrove_forest()))
    ctrl.addButton("参加海上运动", lambda: (ctrl.clearPanel(), participate_in_water_sports()))

def explore_mangrove_forest():
    ctrl.addStoryText("你们穿梭在红树林的树荫下，感受着这片原始的自然之美。红树林间的小道上，偶尔会有彩蝶飞舞，鸟鸣声在林间回响，让人仿佛远离了世界的喧嚣，进入了一片宁静的天地。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), evening_in_yalong_bay()))

def participate_in_water_sports():
    ctrl.addStoryText("亚龙湾的海上运动中心提供了丰富的活动，你们选择了划皮划艇。在专业教练的指导下，你们乘着皮划艇在海湾中畅游，从水面上欣赏亚龙湾的美景，又是一番不同的体验。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), evening_in_yalong_bay()))

def evening_in_yalong_bay():
    ctrl.addStoryText("傍晚时分，你们回到海滩，正好赶上日落的美景。夕阳将天空染成了金色，海面也被镀上了一层橘黄，美得让人心醉。你们在这美妙的时刻，静静地坐在沙滩上，享受着家人之间的温馨。")
    ctrl.addButton("在沙滩上享受夕阳", lambda: (ctrl.clearPanel(), enjoy_sunset_on_beach()))
    ctrl.addButton("在海边餐厅用晚餐", lambda: (ctrl.clearPanel(), have_dinner_on_seaside()))

def enjoy_sunset_on_beach():
    ctrl.addStoryText("你们选择在沙滩上继续欣赏这难得的夕阳美景。随着太阳缓缓沉入海平线，天空中的云彩变得五彩斑斓，你们拿出手机，记录下这一刻的美好。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), end_of_day_in_yalong_bay()))

def have_dinner_on_seaside():
    ctrl.addStoryText("亚龙湾的海边餐厅以其美味的海鲜闻名。你们选择了一家看起来很有情调的餐厅，坐在露天区域，可以一边用餐一边欣赏海景。餐厅的灯光柔和，与海边的夜色相得益彰，美食加上美景，让这个晚上变得更加浪漫。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), end_of_day_in_yalong_bay()))

def end_of_day_in_yalong_bay():
    ctrl.addStoryText("晚餐过后，一家人散步回酒店，海风轻拂，星空璀璨，亚龙湾的夜晚宁静而美丽。今天在亚龙湾的经历，将成为你们记忆中最宝贵的财富之一。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), fourth_day_in_hainan()))

def fourth_day_in_hainan():
    ctrl.addStoryText("随着高铁缓缓驶入三亚站，一家人迎来了他们在“东方夏威夷”——亚龙湾的精彩一天。亚龙湾以其“天下第一湾”的美誉，吸引了世界各地的游客，而今天，它将以其碧海、蓝天、柔软的沙滩、清新的空气和温暖的阳光迎接你们。")
    ctrl.addButton("继续",lambda: (ctrl.clearPanel(), evening_in_yalong_bay()))
def evening_in_yalong_bay():
    ctrl.addStoryText("傍晚时分，你们回到海滩，正好赶上日落的美景。夕阳将天空染成了金色，海面也被镀上了一层橘黄，美得让人心醉。你们在这美妙的时刻，静静地坐在沙滩上，享受着家人之间的温馨。")
    ctrl.addButton("在沙滩上享受夕阳", lambda: (ctrl.clearPanel(), enjoy_sunset_on_beach()))
    ctrl.addButton("在海边餐厅用晚餐", lambda: (ctrl.clearPanel(), have_dinner_at_seaside_restaurant()))

def enjoy_sunset_on_beach():
    ctrl.addStoryText("你们选择在沙滩上继续欣赏这难得的夕阳美景。随着太阳缓缓沉入海平线，天空中的云彩变得五彩斑斓，你们拿出手机，记录下这一刻的美好。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), end_of_day_in_yalong_bay()))

def have_dinner_at_seaside_restaurant():
    ctrl.addStoryText("亚龙湾的海边餐厅以其美味的海鲜闻名。你们选择了一家看起来很有情调的餐厅，坐在露天区域，可以一边用餐一边欣赏海景。餐厅的灯光柔和，与海边的夜色相得益彰，美食加上美景，让这个晚上变得更加浪漫。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), end_of_day_in_yalong_bay()))

def end_of_day_in_yalong_bay():
    ctrl.addStoryText("晚餐过后，一家人散步回酒店，海风轻拂，星空璀璨，亚龙湾的夜晚宁静而美丽。今天在亚龙湾的经历，将成为你们记忆中最宝贵的财富之一。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), last_day_in_sanya()))

def last_day_in_sanya():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("在三亚之旅的最后一天，阳光依旧温暖而明媚，一家人来到了著名的三亚千古情景区，准备观看那场让人瞩目的大型歌舞——《三亚千古情》。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), visit_sanya_love_forever_park()))

def visit_sanya_love_forever_park():
    ctrl.addStoryText("到达景区，你们首先被那座宏大的舞台建筑所震撼。它不仅仅是一个表演的场所，更像是一座时光穿梭机，准备带领你们穿越到古老的三亚。")
    ctrl.addButton("先了解景区的历史文化", lambda: (ctrl.clearPanel(), learn_about_park_history()))
    ctrl.addButton("直接进入剧场等待演出开始", lambda: (ctrl.clearPanel(), wait_for_show_to_start()))

def learn_about_park_history():
    ctrl.addStoryText("你们选择先参加景区的历史文化导览。导游带领你们穿梭在景区内，详细讲解了落笔洞的神秘传说，冼夫人英雄事迹的展览，以及海上丝路的历史。这些故事让你们对即将观看的演出有了更深的理解。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), wait_for_show_to_start()))

def wait_for_show_to_start():
    ctrl.addStoryText("你们决定直接进入剧场，找到了自己的座位。剧场的设计让你们惊叹，360度全景剧幕让整个空间无死角，巨型悬空透明膜让人感觉自己就在故事之中。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), watch_show()))

def watch_show():
    ctrl.addStoryText("演出开始了，舞台上的演员们以精湛的舞技和声情并茂的歌声，将三亚的千年历史展现得淋漓尽致。在《三亚千古情》的演绎下，你们仿佛真的经历了鉴真东渡时的惊涛骇浪，听到了鹿回头美丽传说中的海浪声。")
    ctrl.addButton("与演员互动", lambda: (ctrl.clearPanel(), interact_with_actors()))
    ctrl.addButton("全神贯注观看演出", lambda: (ctrl.clearPanel(), watch_show_intently()))

def interact_with_actors():
    ctrl.addStoryText("在演出的互动环节，你们有幸被选中上台体验。在众人的注视下，你们与演员共舞，跟随着他们的步伐旋转跳跃，感受着舞台上的光芒和热情。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), after_show()))

def watch_show_intently():
    ctrl.addStoryText("你们选择沉浸在这场视听盛宴中，不愿错过任何一个细节。随着故事的推进，你们被舞台上的每一个动作、每一句歌词所感动，完全被这场演出俘获。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), after_show()))

def after_show():
    ctrl.addStoryText("演出结束后，一家人在出口处久久不愿离去。爸爸感慨地说：“这不仅仅是一场演出，它是三亚的灵魂，是历史与现代的完美结合。” 妈妈感动地补充说：“这是我们在三亚最难忘的经历，也是这次旅行最美好的收官。”")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), leaving_sanya()))

def leaving_sanya():
    ctrl.addStoryText("在离开景区的路上，你们互相分享着各自的感受和这次旅行中的点点滴滴。三亚千古情景区的壮丽和《三亚千古情》的震撼，成为了你们旅程中宝贵的记忆，也让这次三亚之旅画上了完美的句号。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), on_the_plane()))

def on_the_plane():
    ctrl.addStoryText("随着飞机平稳地腾空而起，三亚的海岸线渐渐远去，一家人的旅行也接近了尾声。在高空中，他们围坐在一起，窗外是流云和天空的壮丽景色，他们开始畅谈这次旅行的所见所闻所感。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), share_travel_experiences()))

def share_travel_experiences():
    ctrl.addStoryText("爸爸打开话匣子，首先提到了在三亚千古情景区的震撼体验：“那场演出真是超乎想象，它不只是展示了三亚的历史，更是一次视觉和听觉的盛宴。”")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), mom_shares_experience()))

def mom_shares_experience():
    ctrl.addStoryText("妈妈接着说：“我最喜欢的是在亚龙湾的海滩上，那里的沙子和海水，还有那边的阳光，都是那么的温暖和舒适。我觉得那几天我们就像住在了天堂里。”")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), you_share_experience()))

def you_share_experience():
    ctrl.addStoryText("你则回忆起在红树林中的宁静时刻：“那片红树林给我留下了深刻的印象，那里的自然美景和平静，让我感到心灵都被净化了。”")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), sibling_shares_experience()))

def sibling_shares_experience():
    ctrl.addStoryText("弟弟或妹妹兴奋地插话：“我喜欢海口骑楼老街，那些老建筑真的很酷，而且那天我们还学习了制作手工艺品，这些都是很宝贵的经历。”")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), family_discussion()))

def family_discussion():
    ctrl.addStoryText("一家人谈论着，每个人的脸上都洋溢着幸福的笑容。旅行中的每个瞬间，无论是宁静的自然景观还是震撼的文化演出，都成为了他们共同记忆的一部分。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), dad_shares_final_thoughts()))

def dad_shares_final_thoughts():
    ctrl.addStoryText("爸爸深情地说：“这次旅行让我们作为一个家庭更加紧密了，我们共同经历了这么多，看到了三亚的美，感受到了海南的温暖。”")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), mom_agrees()))

def mom_agrees():
    ctrl.addStoryText("妈妈点头赞同：“是的，这次旅行不仅让我们放松了身心，更重要的是我们一起创造了美好的回忆。”")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), you_contemplate()))

def you_contemplate():
    ctrl.addStoryText("你看着窗外的云层，思绪飞扬：“我们不只是旅行到了一个地方，我们旅行到了过去，感受了文化，现在又带着所有的美好回到现实。”")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), farewell()))

def farewell():
    ctrl.addStoryText("飞机在云端穿行，一家人的谈话还在继续，他们讨论着下一次的旅行目的地，每个人都充满了期待。旅行的意义不仅在于目的地的风景，更在于途中的陪伴和回家后的回忆。这次三亚之旅，无疑给每个家庭成员留下了深刻的印象，成为了他们共同生活中宝贵的一部分。亲爱的玩家，")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), end_message()))

def end_message():
    ctrl.addStoryText("随着这趟虚拟旅程的结束，我们希望你的心中充满了欢乐与温馨，就如同你刚刚完成的这段奇妙之旅。在三亚的碧海蓝天下，我们一起探索了自然的奥秘，体验了文化的深厚，分享了家庭间的温情，这些宝贵的记忆将永远珍藏在我们的心中。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), end_message_part2()))

def end_message_part2():
    ctrl.addStoryText("虽然现在我们要告别，但请记住，旅行的魅力在于每次出发都是一次新的开始。无论是在现实世界还是在游戏的世界里，新的冒险总是等待着我们去发现。我们期待在未来的旅程中再次与你相遇，探索更多未知的世界，创造更多难忘的故事。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), end_message_part3()))

def end_message_part3():
    ctrl.addStoryText("感谢你陪伴我们度过了这段美好的时光。直到下次再见，愿你的日子如同三亚的阳光一样温暖，愿你的生活如这次旅行般精彩无比。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), end_message_part4()))

def end_message_part4():
    ctrl.addStoryText("再见了，亲爱的旅伴，直到下一个旅程的召唤。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), end_message_part5()))

def end_message_part5():
    ctrl.addStoryText("温馨地，你的旅行游戏团队")

