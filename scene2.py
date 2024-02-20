import sys
from Controller import Controller
ctrl = Controller.getInstance()
def night_before_travel():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setTime('2024-02-08 00:30:00')
    ctrl.setPosition('卧室中')

    ctrl.addStoryText("2月7日夜，你兴奋得睡不着觉。打开手机发现已经是午夜12点半。你决定：")
    ctrl.addStoryText('#0000FF选择：#0000FF')
    ctrl.addButton("发送旅游信息", lambda: (ctrl.clearPanel(), send_travel_info()))
    ctrl.addButton("打开b站找好康的", lambda: (ctrl.clearPanel(), browse_bilibili()))

def send_travel_info():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("谁能想到，你立刻得到了秒回。")
    ctrl.addStoryText("对方表示自己也正在哈尔滨，可以给你介绍介绍值得一看的景点，甚至可以见上一面。")
    ctrl.addStoryText("你匆匆忙忙地回复了“好的，晚安”受宠若惊，小心脏怦怦乱跳，仿佛回到了十七岁那年的雨季，更是睡不着觉了。")
    ctrl.addStoryText("最终折腾得你身心俱疲，不知道什么时候你进入了梦乡，身影模糊的ta与你在冰面上翩然起舞，就如同两颗露珠滑落草叶，最终汇聚成一颗晶莹水滴……你沉醉了。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), morning_of_departure()))

def browse_bilibili():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("点开那群英荟萃的粉色APP，在大数据的强烈导向下，你刷着刷着就刷到了宋浩高等数学。")
    ctrl.addStoryText("此时，评论区里面一个关于数形结合将抛物线面积转换成棱锥体积的论断吸引了你的眼球。")
    ctrl.addStoryText("你瞪着宋浩老师铺满弹幕的黑板和面孔，怎么也思索不出它的原理。")
    ctrl.addStoryText("于是你关掉屏幕苦思冥想，在抛物线终于变成棱锥的那一刻，它们扭曲了，变成了一座巍峨的——你认出那是——圣·索菲亚教堂，它倒映出一道虹光，不知道什么时候它不再是抛物线、不是棱锥、也不是数形结合了。")
    ctrl.addStoryText("你早已进入梦乡，睡得香甜。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), morning_of_departure()))

def morning_of_departure():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setTime('2024-02-08 07:15:00')
    ctrl.setPosition('火车站')
    ctrl.addStoryText("2月8日早晨，你们早已在火车站坐了半个多小时——妈妈总是这样，怕我们赶不上车，打好提前量。")
    ctrl.addStoryText("只是这提前量打的有点太好，就连火车检票口的屏幕还暗淡着，工作人员也没有来，但是已有很多人在等待。他们有的是赶春节回家的车，剩下的，就是像你们一样准备“游历春节”的了")
    ctrl.addStoryText("你开始在沈阳北站的候车厅漫无目的地游逛起来。")
    ctrl.addStoryText('#0000FF选择：#0000FF')
    ctrl.addButton("看看店铺", lambda: (ctrl.clearPanel(), look_at_shops()))
    ctrl.addButton("刷刷手机", lambda: (ctrl.clearPanel(), browse_phone()))

def look_at_shops():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你看到了一家俄罗斯风情店。老板娘待人和蔼、商品也很便宜。")
    ctrl.addStoryText("很快你的猜想得到了证实，你拿起一包巧克力，在纷繁复杂的俄文字母中你找到了产地：沈阳市。")
    ctrl.addStoryText("你瞬间对俄罗斯风情店失去了兴趣，悻悻地离开了。老板娘用非常标准的东北话送别了你。")
    ctrl.addStoryText("刚出店门，你就给高中结识的大民屯镇的同学发信息，确认是否有这么一家产能强大的食品厂。")
    ctrl.addStoryText("5分钟后，你得到了肯定的答复。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), on_the_train()))

def browse_phone():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你发现这块儿的移动热点可真多，于是你开始研究起他们的手机型号来。")
    ctrl.addStoryText("突然，一个名为酷派大神F2的热点不见了。你苦笑了一下，自己几年前也曾经用过这台冷门手机。")
    ctrl.addStoryText("你庆幸自己的手机不会突然罢工，给自己愉快的旅途添麻烦。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), on_the_train()))

def on_the_train():
    ctrl.setTime('2024-02-08 07:35:00')
    ctrl.setPosition('火车站')
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("时间过得总是又快又慢——快就快在期待的心情上，慢就慢在焦急的等待上。")
    ctrl.addStoryText("你一手一个，两个行李箱就这么被轻松地提了起来，你意识到，自己已经长大了，身体很棒。")
    ctrl.addStoryText("不一会儿，红头绿身的“老干部”和谐号列车就缓缓驶来。")
    ctrl.addStoryText("一时间，你居然有一种自己置身于9又3/4站台，即将与哈利·波特一起进入霍格沃茨魔法学院学习的错觉。")
    ctrl.addStoryText("很快你们被熙熙攘攘的人流淹没，列车员不断喊着“先下后上、文明礼让”的声音也仿佛投入湖中的盐块。在传入人群以后，再也没有得到回应。")
    ctrl.addStoryText("坐在火车靠窗的位置，你拥有着对窗帘和桌子的绝对掌控权。")
    ctrl.addStoryText("你从窗户往外看，美景在眼前飞速掠过。你不禁开始展开天马行空的想象：窗外是一卷巨大的手纸，印刷好了风景的图案；火车从北站出发一直到哈尔滨，这卷手纸也不断展开展开展开……到哈尔滨站，这一卷手纸已然展开成为一道亮丽的东三省白山黑水图，绝不逊色于任何一幅国画巨作。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), reminiscing_childhood()))

def reminiscing_childhood():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("水彩蜡笔和万花筒，画不出天边那一道彩虹。")
    ctrl.addStoryText("你想起罗大佑在《童年》里吟唱的童真童趣，会心的笑了。")
    ctrl.addStoryText("人永远也无法同时拥有青春和对青春的理解。")
    ctrl.addStoryText("你想起初中时你那俏皮可爱的同桌来。")
    ctrl.addStoryText("Ta仿佛是个全能的人才，手巧、身体棒还很温和，成绩虽说比不上你，但是也是班级里数一数二的存在。")
    ctrl.addStoryText("可惜你最后还是没能在ta一次次明的暗的示好中存活下来，ta中考失利，没有和你进入同一所高中。你们的人生也从此分道扬镳。初中学校仿佛家乡那永远矗立在北方的火车站，一共只有那么几趟车，分散向几个大致的地方；而高中则更像历史悠久的工业城市、铁路枢纽，无数车来车往，可能对于很多你认识的——你曾经认识的，无论是想见的、无所谓的、不想见的，你们已见了人生的最后一面。")
    ctrl.addStoryText("提到高中，你想起自己那挥斥方遒的日子来。")
    ctrl.addStoryText("那时，有些同学在桌上用课本堆砌了厚厚的城墙，有些则是桌面整洁笔耕不辍。")
    ctrl.addStoryText("你既同情又喜欢那些文具多、教辅多的同学：他们总是次次失利，却又在你借东西的时候堪比多啦A梦，什么都有。")
    ctrl.addStoryText("你想起每次数学课总是有那么几个“b哥”，他们在老师读出选择题答案是肆意地画着鲜红色的对号。")
    ctrl.addStoryText("英语课上，老师说出一个四级词汇，有些人甚至能如连珠炮响般，爆出它四五个你听都没听过的同义词……")
    ctrl.addStoryText("你倒是班里比较低调的，你会因为某次全对的实验填空暗喜，会在多选题错选、多选时黯然神伤。")
    ctrl.addStoryText("会因自己受到同学们的崇拜而惊讶，会在老师忽视b哥b姐，转而抓起默默抄笔记的你问问题时感到自豪。")
    ctrl.addStoryText("高中就是这样苦中作乐，有很多值得人深刻回忆的地方。")
    ctrl.addStoryText("你望向窗外，此时正是一条大河、两岸芦花。")
    ctrl.addStoryText("突然窗外一黑你们进入了隧道。")
    ctrl.addStoryText("随即便是一片光明、豁然开朗，一眼望不到边的银色平原。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), train_journey_continued()))
def train_journey_continued():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("如此开阔的视野打断了你的思维，所有车内的吵闹早已被你忽视。")
    ctrl.addStoryText("你变成了一个“两耳不闻窗内事”的倒反天罡人。")
    ctrl.addStoryText("我们的领袖毛主席在他豪言壮语的沁园春·雪中挥毫泼墨、浮白载笔的图画在火车出隧道的一刹那，铺天盖地地展开了。")
    ctrl.addStoryText("接着，美景拼命地试图挤进你的眼睛和大脑。")
    ctrl.addStoryText("你情不自禁地念出诗词的最后两句：数风流人物，还看今朝……")
    ctrl.addStoryText("或许，这也正是你选择计算机专业的缘故。")
    ctrl.addStoryText("以身报国，是你最大的梦想。")
    ctrl.addStoryText("不能穿上军装、保卫边疆，也可曲线救国、实干兴邦！")
    ctrl.addStoryText("你的思维如同一艘快艇行驶在波谲云诡的沧海，几经沉浮、数次折转，却总是航行着，航行着。")
    ctrl.addStoryText("你是向着太阳的方向开过去了吗？你没有给出自己答案。")
    ctrl.addButton("沉浸在回忆中", lambda: (ctrl.clearPanel(), immerse_in_memories()))

def immerse_in_memories():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setTime('2024-02-08 10:35:00')
    ctrl.setPosition('火车站')
    
    ctrl.addStoryText("你从对面的青年那里了解到，他来自山东聊城，你听说了辽工大在那边的录取状况和他们的高考分数后，吃惊地张大了嘴。")
    ctrl.addStoryText("火车上油油腻腻的15元盒饭吊不起你的胃口，你一遍又一遍看着12306上面的报站和时间点。")
    ctrl.addStoryText("信号时有时无，让你不能和他人保持联系、刷视频也很难。")
    ctrl.addStoryText("在你说出第114514遍“我受不了啦”之后，火车报站声音终于响起：等噔灯灯！")
    ctrl.addStoryText("各位旅客请注意，本次列车即将到达终点站;哈尔滨站。请各位旅客整理好随身物品和行李，准备下车。祝您旅途愉快！")
    ctrl.addStoryText("多么亲切的东北话！！")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), leaving_train_station()))
    


def leaving_train_station():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setTime('2024-02-08 16:55:00')
    ctrl.setPosition('火车站出站口')
    
    ctrl.addStoryText("你与父母总算是离开了熙熙攘攘的火车站。")
    ctrl.addStoryText("虽然刚刚下午四点多，但是哈尔滨的隆冬已经为城市熄了灯，")
    ctrl.addStoryText("而无数的高楼大厦却如同宿舍宵禁后精力旺盛的莘莘学子，仍是不知疲倦地挑灯夜战。")
    ctrl.addStoryText("外面不少出租车。只见几个如饥似渴的大叔立刻冲上来，问你们：上哪！上冰雪大世界不？")
    ctrl.addStoryText("要不是远处高楼林立、灯火辉煌，你还真以为自己到家了。")
    ctrl.addStoryText("你们决定：")
    ctrl.addButton("坐出租车", lambda: (ctrl.clearPanel(), take_taxi()))
    ctrl.addButton("步行", lambda: (ctrl.clearPanel(), walk()))


def take_taxi():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("司机大叔轻松地将你们的行李安置在了出租车后备箱里。他很是热情，一路和你们讲哈尔滨的特色和风土人情。")
    ctrl.addStoryText("很快就到了你们预定好的酒店。你们放好箱子，刚刚下午五点十分。")
    ctrl.addButton("选择活动", lambda: (ctrl.clearPanel(), choose_activity()))

def walk():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("虽然你一手一个沉重的行李箱，但是在轮子的加持下，外加风景的感染，你已经不再感到疲倦。")
    ctrl.addStoryText("步行两公里，来到了订好的酒店。你们放好东西，看了看手机，五点四十。")
    ctrl.addButton("选择活动", lambda: (ctrl.clearPanel(), choose_activity()))

def choose_activity():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    # 假设之前没有进行发送旅游信息的操作
    
    ctrl.setTime('2024-02-08 17:55:00')
    ctrl.setPosition('酒店')
    ctrl.addStoryText("你们决定：")
    ctrl.addButton("出去转转", lambda: (ctrl.clearPanel(), explore()))
    ctrl.addButton("酒店休息", lambda: (ctrl.clearPanel(), rest_in_hotel()))

def explore():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setPosition('夜市')
    ctrl.addStoryText("你和爸爸妈妈来到了熙熙攘攘热热闹闹的夜市。")
    ctrl.addStoryText("你随便挑了一会，转头已经找不到爸爸妈妈了——看来你们只能靠手机联系了。你又横穿了几条街。")
    ctrl.addButton("偶然的发现", lambda: (ctrl.clearPanel(), unexpected_discovery()))

def rest_in_hotel():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setTime('2024-02-08 20:55:00')
    
    ctrl.addStoryText("选择在酒店休息，你们决定早点休息，为明天的探索储备精力。")
    ctrl.addButton("开启第二天的旅程", lambda: (ctrl.clearPanel(),  explore_together()))
   




def unexpected_discovery():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
  
    ctrl.setPosition('街巷')
    ctrl.addStoryText("一个偶然，你看见一件你再熟悉不过的羽绒服——克莱因蓝色，鼓鼓囊囊简直像一个柔软的气球……你的心跳停了一下，听觉随之消失，动作也完全静止。真的是ta！")
    ctrl.addStoryText("你在夜市中偶然发现了一个熟悉的身影。")
    ctrl.addStoryText('#0000FF选择：#0000FF')
    ctrl.addButton("假装没看见", lambda: (ctrl.clearPanel(), pretend_not_to_see()))
    ctrl.addButton("走过去", lambda: (ctrl.clearPanel(), approach()))

def pretend_not_to_see():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你假装没看见ta。可是ta真的是回头就看见了你。")
    ctrl.addStoryText("Ta突然蹦了过来一个九天雷霆双脚蹬，给你的魂都吓到九阴白骨天外去了。")
    ctrl.addStoryText("你又害羞又激动，ta主动邀请你一起逛夜市，你欣然同意。")
    ctrl.addButton("与父母汇合", lambda: (ctrl.clearPanel(), meet_with_parents_after_market()))

def approach():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你为了给ta一个惊喜，先悄悄走到了他的背后。然后，立刻就是一个九天雷霆双脚蹬！")
    ctrl.addStoryText("ta又害羞又激动。于是你主动要求ta一起逛夜市，ta欣然同意了。")
    ctrl.addButton("与父母汇合", lambda: (ctrl.clearPanel(), meet_with_parents_after_market()))

def meet_with_parents_after_market():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("逛过夜市后，你和爸爸妈妈打电话汇合。你一路偷笑，他们不以为意。")
    ctrl.addStoryText("你们一起回到了酒店")
    # ctrl.addProgress("偶遇")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), rest_in_hotel_with_fireworks()))

# 定义在酒店休息并观看烟花的场景
def rest_in_hotel_with_fireworks():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你们决定不再出去，明天再展开旅程。突然，外面一阵烟花爆竹的响声。")
    ctrl.addStoryText("烟花易冷、美丽易逝。然而灯光秀更是让人眼花缭乱！")
    ctrl.addStoryText("看过灯光秀，一天的舟车劳顿便反馈给了你的身体。你一躺倒在枕头上，就再也没有醒来。")
    ctrl.addButton("继续", lambda: (ctrl.clearPanel(), morning()))

# 定义第二天早上的场景
def morning():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setTime('2024-02-09 06:55:00')
    ctrl.setPosition('酒店')
    ctrl.addStoryText("第二天早上。爸爸妈妈早早地将你喊起来，想拉着你一起按照他们结合很多旅游攻略的宇宙超级无敌天至尊自行总结攻略一起行动。")
    ctrl.addStoryText("但他们也知道你生性叛逆，说不定不愿意和他们一起逛。于是，他们采纳了你的意见：")
    ctrl.addStoryText('#0000FF选择：#0000FF')
    ctrl.addButton("一同探索", lambda: (ctrl.clearPanel(), explore_together()))
    ctrl.addButton("自由旅行", lambda: (ctrl.clearPanel(), choose_own_adventure()))



def choose_own_adventure():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你的选择在爸爸妈妈的意料之中。你早已经在微信上和crush打好招呼。")
    ctrl.addStoryText("本来紧张兮兮、话都不敢说的你们在昨晚逛夜市时已经熟络，你们都等不及要见到对方一起游玩了。")
    ctrl.addStoryText("你谢绝了爸爸妈妈的邀请，并美其名曰：让他们享受二人世界。")
    ctrl.addStoryText("爸爸妈妈也没有起疑心，可能他们也确实觉得，放孩子自己去玩更自由一些。")
    ctrl.addStoryText("看来，不只是爸爸妈妈要享受二人世界，你和你的那个ta也可以享受二人世界了。")
    ctrl.addButton("前往见crush", lambda: (ctrl.clearPanel(),early_morning()))
    
def early_morning():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你想起了今天和她的约定，你的心跳不禁加速。你快速地穿好衣服，准备去见她。")
    ctrl.addButton("出发去教堂", lambda: (ctrl.clearPanel(), goto_church()))

def goto_church():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setTime('2024-02-09 07:55:00')
    ctrl.setPosition('索菲亚教堂前的广场')
    ctrl.addStoryText("你到了索菲亚教堂前的广场，那里已经有几对情侣在拍照留念。你在人群中寻找她的身影。")
    ctrl.addStoryText("不一会儿，你看到了她，穿着红色的羽绒服，在雪地上特别显眼。你走上前，带着早晨的问候和一颗跳动的心。")
    ctrl.addButton("与她会面", lambda: (ctrl.clearPanel(), meet_her()))

def meet_her():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你们的目光相遇，她的笑容如同拥抱，温暖而熟悉。你们没有言语，只是一起开始了这一天的旅程。")
    ctrl.addStoryText('#0000FF选择：#0000FF')
    ctrl.addButton("一起漫步", lambda: (ctrl.clearPanel(), walk_together()))
    ctrl.addButton("去冰雕展", lambda: (ctrl.clearPanel(), visit_ice_sculptures()))

def walk_together():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setPosition('中央大街')
    ctrl.addStoryText("你们沿着中央大街漫步，古老的建筑像是在诉说着往日的故事。你们在一家俄式餐厅享用了早餐，她对每一道菜都充满了好奇。")
    ctrl.addStoryText("在你们的谈笑中，你发现了生活中的另一种乐趣。")
    ctrl.addButton("继续探索", lambda: (ctrl.clearPanel(), continue_exploration()))

def visit_ice_sculptures():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
   
    ctrl.addStoryText("在户外的冰雕展览中，你们被那些精致的冰雕艺术品深深吸引。她在每一个冰雕前都会驻足欣赏，你则在一旁静静地欣赏着她专注的样子。")
    ctrl.addStoryText('#0000FF选择：#0000FF')
    ctrl.addButton("一起滑雪", lambda: (ctrl.clearPanel(), go_skiing()))
    ctrl.addButton("看夕阳", lambda: (ctrl.clearPanel(), watch_sunset()))

def continue_exploration():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你们的旅行还在继续，每个角落都充满了新的故事。你们决定去滑雪，尽管都不太擅长，但那份快乐和自由，是你们共同的记忆。")
    ctrl.addButton("滑雪结束", lambda: (ctrl.clearPanel(), after_skiing()))

def go_skiing():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name) 
    ctrl.setPosition('小型滑雪场')
    ctrl.setTime('2024-02-09 15:40:00')
    ctrl.addStoryText("在小型滑雪场上，你们尽情地享受着滑雪的乐趣。每一次摔倒，你们都会相视而笑，然后再次站起来。")
    ctrl.addButton("休息一下", lambda: (ctrl.clearPanel(), take_a_break()))

def watch_sunset():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setPosition('咖啡馆')
    ctrl.addStoryText("你们找到了一个可以俯瞰整个城市的高地，一起静静地看着夕阳，感受着那份宁静和美好。")
    ctrl.addButton("夜幕下的咖啡馆", lambda: (ctrl.clearPanel(), coffee_under_stars()))

def take_a_break():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你们在滑雪场边的小屋中休息，喝着热巧克力，回味着滑雪的快乐时光。")
    ctrl.addButton("结束一天的旅行", lambda: (ctrl.clearPanel(), end_day()))

def coffee_under_stars():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("夜幕降临，你们在一家古朴咖啡馆的暖光中坐下，分享着彼此的故事，直到星光开始闪烁。")
    ctrl.addButton("倾听心声", lambda: (ctrl.clearPanel(), listen_to_heart()))

def after_skiing():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setPosition('小型滑雪场')
    ctrl.setTime('2024-02-09 19:40:00')
    ctrl.addStoryText("滑雪后，你们在附近的咖啡馆里坐下，让温暖的气氛和热腾腾的饮料解冻你们的身体。")
    ctrl.addButton("深夜的表白", lambda: (ctrl.clearPanel(), night_confession()))

def listen_to_heart():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("在咖啡馆里，你听到了她的心声，她的梦想，她的希望。你发现自己深深地被她吸引。")
    ctrl.addButton("表达情感", lambda: (ctrl.clearPanel(), express_feelings()))

def night_confession():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你看着她，深吸一口气，然后说出了藏在心底的话：“在这个如梦如幻的地方，我找到了我生命中最真实的感觉。那就是，我爱你。”")
    ctrl.addStoryText("她的眼中闪过泪光，她紧紧握住了你的手。")
    ctrl.addButton("珍藏这一刻", lambda: (ctrl.clearPanel(), cherish_moment()))

def express_feelings():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("在那个温馨的咖啡馆里，你向她表达了你的情感：“我喜欢你，不仅是现在，还有未来的每一个日出日落。”")
    ctrl.addStoryText("她微笑着，眼中充满了感动，你们的手指紧紧交缠。")
    ctrl.addButton("结束一天的旅行", lambda: (ctrl.clearPanel(), end_day()))

def cherish_moment():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("那一刻，你们都沉默了。你们知道，这个瞬间，这份情感，将会被你们永远珍藏。")
    ctrl.addButton("结束一天的旅行", lambda: (ctrl.clearPanel(), end_day()))

def end_day():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你们走出咖啡馆，夜空中的星星似乎也在为你们庆祝。你们的手紧紧相握，一起走在回旅馆的路上，心中充满了对未来的期待。")
    ctrl.addButton("结束", lambda: (ctrl.clearPanel(), choose_next__destination()))








def explore_together():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setPosition('哈尔滨工业大学')
    ctrl.setTime('2024-02-09 9:40:00')
    ctrl.addStoryText("多么难得的一次家庭聚会！你知道，自己上大学以后，与父母在一起的时间变得越来越少。")
    ctrl.addStoryText("你选择牺牲自己的小小野心，和他们一同行动。爸爸妈妈自然是喜出望外。")
    ctrl.addStoryText("妈妈还亲自为你拉上了羽绒服的拉链。不知不觉你已经高出妈妈一头，你小时候她拉着你散步的身影渐渐模糊。")
    ctrl.addStoryText("你觉得，自己的选择是正确的。看着父母开心，你自己也如同吃了满满一勺三氯蔗糖一般，从舌尖一直甜到了心里。")
    # ctrl.addAchievement("全家福")
    ctrl.addButton("前往哈尔滨工业大学", lambda: (ctrl.clearPanel(), visit_hit()))

# 定义访问哈尔滨工业大学的场景
def visit_hit():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你和爸爸妈妈的第一站，就是当地甚至全国最强的高校——哈尔滨工业大学。")
    ctrl.addStoryText("哈尔滨工业大学“规格严格、功夫到家”的校训，激励着每一届哈工学子，即使在最艰难的时候，也从未动摇。")
    ctrl.addStoryText("随着时代的发展，在哈工大被美国列入高危名单以后，“功夫到家”便更有了新的含义。")
    ctrl.addStoryText("它时时刻刻如警钟般激励着规范着哈工学子们的言行。")
    ctrl.addStoryText("你想起去年参观的中国第一所现代大学——天津大学校内无处不在的“1895”，以及隔壁南开大学三步一见的标语“我是爱南开的”……")
    ctrl.addStoryText("果然每一所大学都有属于自己的、无处不在的校园文化。")
    ctrl.addStoryText("你和父母走进哈工大校门，他们提议，让你这个大学生带领他们，看看大学校园内有什么值得参观的地方。")
    ctrl.addButton("开始校园之旅", lambda: (ctrl.clearPanel(), visit_souvenir_shop()))


def visit_souvenir_shop():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你最喜欢的就是收集校徽。到了哈工大，自然要立刻将哈工大的校徽收入囊中。")
    ctrl.addStoryText("只是让你失望的是，最便宜的小方盒校徽早已被先行一步的“南方小土豆”和无数慕名而来的学子风卷残云般吃干抹净。")
    ctrl.addStoryText("但是你并没有屈服于售罄的穷鬼套餐，你忍痛割爱，129元拿下了包含一支钢笔、一个不锈钢书签和一枚金属校徽的超级礼盒。")
    ctrl.addStoryText("你很是开心，爸爸妈妈也没有责备你乱花钱。显然他们经常看网上的高等学府视频，哈工大几乎可以称得上他们心中的圣地。")
    ctrl.addButton("结束校园之旅", lambda: (ctrl.clearPanel(), end_campus_tour())) 



# 之前的校园之旅最后一部分应该连接到这个选择
def end_campus_tour():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setTime('2024-02-09 15:40:00')
    ctrl.setPosition('附近的校园餐厅')
    ctrl.addStoryText("经过一天的校园之旅，你们决定去附近的餐厅享用晚餐。")
    ctrl.addStoryText("这是一次愉快的家庭旅行的开始。")
    choose_next__destination()

def choose_next__destination():
    ctrl.setTime('2024-02-10 07:40:00')
    ctrl.setPosition('酒店')
    ctrl.addStoryText("一夜无话。第三天，也是你们此次哈尔滨之旅的最后一天，你们准备前往哈尔滨冰雪大世界")
    ctrl.addButton("到达冰雪大世界", lambda: (ctrl.clearPanel(), go_to_harbin())) 

     
def go_to_harbin():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setTime('2024-02-10 07:45:00')
    ctrl.setPosition('冰雪大世界')
    ctrl.addStoryText("随着你们踏入了冰雪大世界，一片由冰晶构成的城堡映入眼帘，在阳光下闪耀着耀眼的光芒。")
    ctrl.addStoryText("你的父母也被这壮观的景象所吸引，你们决定先去探索这个冰雕城堡。")
    ctrl.addStoryText('#0000FF选择：#0000FF')
    ctrl.addButton("询问导游故事的更多细节", lambda: (ctrl.clearPanel(), ask_guide_more()))
    ctrl.addButton("自己探索城堡的其他部分", lambda: (ctrl.clearPanel(), explore_castle()))

def ask_guide_more():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你对这些民间故事产生了浓厚的兴趣，向导游提出了问题。")
    ctrl.addStoryText("导游看到你的热情，便更加生动地讲述起来，甚至引用了一些方言和动作，让整个故事更加栩栩如生。")
    ctrl.addButton("继续听导游讲解", lambda: (ctrl.clearPanel(), continue_with_guide()))

def continue_with_guide():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你选择继续听导游讲解，了解更多关于这些壁画背后的故事。")
    ctrl.addButton("继续探索城堡", lambda: (ctrl.clearPanel(), continue_exploring_castle()))

def explore_castle():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setTime('2024-02-10 07:59:00')
    ctrl.addStoryText("你决定离开团队，自己探索城堡的秘密。")
    ctrl.addStoryText("你走过一条条蜿蜒曲折的冰廊，每个转角都有新的惊喜。")
    ctrl.addStoryText("在一个隐蔽的角落里，你发现了一座小型冰雕，它是一只栩栩如生的冰狼，那精湛的工艺让你不禁佩服起雕刻者的技艺。")
    ctrl.addButton("继续探索城堡", lambda: (ctrl.clearPanel(), continue_exploring_castle()))

def continue_exploring_castle():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你继续在城堡内部探索，发现了更多精美的冰雕作品。")
    ctrl.addButton("探索户外滑梯区", lambda: (ctrl.clearPanel(), explore_castle_outdoors()))

def explore_castle_outdoors():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setTime('2024-02-10 08:30:00')
    ctrl.addStoryText("探索完城堡，你们来到了户外的冰滑梯区。这里有各种高低不同的滑梯，孩子们在这里尖叫着，欢笑着。")
    ctrl.addStoryText('#0000FF选择：#0000FF')
    ctrl.addButton("勇敢尝试最高的滑梯", lambda: (ctrl.clearPanel(), try_highest_slide()))
    ctrl.addButton("选择一条中等高度的滑梯", lambda: (ctrl.clearPanel(), try_medium_slide()))

def try_highest_slide():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你决定挑战最高的一条滑梯。站在滑梯的顶端，你几乎可以俯瞰整个冰雪大世界。你深吸一口气，然后放开身体，顺着滑梯飞速下滑，那种速度和刺激让你的心跳加速，直到滑到底部，你才大声地笑了出来。")
    ctrl.addButton("参观冰上舞蹈表演", lambda: (ctrl.clearPanel(), visit_ice_dance_performance()))

def try_medium_slide():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你选择了一条不那么惊险的滑梯，你的父母也加入了你的行列。你们一起坐在滑梯上，随着冰面的滑动，你们的笑声在冰雪大世界里回荡。")
    ctrl.addButton("参观冰上舞蹈表演", lambda: (ctrl.clearPanel(), visit_ice_dance_performance()))

def visit_ice_dance_performance():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setTime('2024-02-10 10:40:00')
    ctrl.addStoryText("在体验了冰川裂缝后，你们来到了一个宽敞的空地，这里正在举行一场冰上舞蹈表演。舞者们穿着华丽的服装，在冰面上旋转跳跃，他们的表演优雅而充满力量，让你们都为之动容。")
    ctrl.addStoryText('#0000FF选择：#0000FF')
    ctrl.addButton("观看舞蹈表演", lambda: (ctrl.clearPanel(), watch_dance_performance()))
    ctrl.addButton("参加冰上舞蹈教学", lambda: (ctrl.clearPanel(), join_ice_dance_lesson()))

def watch_dance_performance():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你们选择在一旁观看。随着音乐的起伏，舞者们的动作也随之变化，他们似乎与冰面融为一体，每一个动作都那么的完美。你们被这场表演深深吸引，直到最后一刻都不愿离去。")
    ctrl.addButton("在摄影区拍照留念", lambda: (ctrl.clearPanel(), take_family_photos()))

def join_ice_dance_lesson():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("一个舞蹈教师邀请游客一起加入。你鼓起勇气，和你的父母一起踏上冰面。开始时你们摇摇晃晃，但在教师的指导下，你们渐渐找到了节奏，虽然步伐不是很协调，但笑声和欢呼声充满了整个空间。")
    ctrl.addButton("在摄影区拍照留念", lambda: (ctrl.clearPanel(), take_family_photos()))

def take_family_photos():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("在离开前，你们来到了一个专门的摄影区，这里有专业的摄影师帮游客拍照留念。")
    ctrl.addStoryText('#0000FF选择：#0000FF')
    ctrl.addButton("拍一张传统的全家福", lambda: (ctrl.clearPanel(), take_traditional_family_photo()))
    ctrl.addButton("尝试一些有趣的创意照", lambda: (ctrl.clearPanel(), take_creative_photos()))

def take_traditional_family_photo():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你们选择了一个看起来很有北国风情的背景，一家人紧紧相依，面带微笑。这张照片定格了你们旅行中的幸福时刻，将成为家庭相册中的珍贵一页。")
    ctrl.addButton("结束旅程", lambda: (ctrl.clearPanel(), end_of_ice_snow_journey()))

def take_creative_photos():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.addStoryText("你们在摄影师的建议下，尝试了一些创意拍摄。比如装作被冰雕怪兽追赶的样子，或者模仿冰雕上的动作，这些有趣的照片让你们的旅行增添了不少欢乐。")
    ctrl.addButton("结束旅程", lambda: (ctrl.clearPanel(), end_of_ice_snow_journey()))

def end_of_ice_snow_journey():
    ctrl.setCurrentProgress(sys._getframe().f_code.co_name)
    ctrl.setTime('2024-02-10 11:37:00')
    ctrl.setPosition('返程')
    ctrl.addStoryText("当你们最终离开冰雪大世界，踏上回家的路时，你们的心中充满了满足和快乐。这次旅行不仅让你们领略了冰雪的魅力，更加深了家人之间的情感。这段旅程，这些记忆，将会成为你们生命中宝贵的财富。")
    ctrl.changeScript('scene','farewell2')
 
