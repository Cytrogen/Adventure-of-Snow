# 游戏开始页面 & 配置角色页面


from config import *


# 角色数据读取
chara = {}
chara = json.load(open(charaPath, 'r', encoding='utf8'))
system = json.load(open(welcomePath, 'r', encoding="UTF-8"))


# 开始欢迎
def welcome():
    global system
    titlePost = system["title"]
    hint = json.load(open(welcomePath, 'r', encoding="UTF-8")).get('hint')
    hintPost = random.choice(hint)

    os.system('clear')
    print(titlePost + '\n\n' + hintPost)


# 测试用函数
def resetChara():
    global chara
    time.sleep(1)
    reset = input("\n> 要重置角色的所有数值吗？[Y / 其他键]：")
    if reset == 'Y' or reset == 'y':
        chara['name'] = ''
        chara['gender'] = 0
        chara['sexori'] = 0
        chara['money'] = 15
        chara['attribute']['str'] = 0
        chara['attribute']['agi'] = 0
        chara['attribute']['phy'] = 0
        chara['attribute']['int'] = 0
        chara['attribute']['per'] = 0
        chara['attribute']['cha'] = 0
        chara['inventory']['bottle'] = False
        chara['inventory']['bottleWater'] = False
        chara['inventory']['palacePass'] = False
        chara['inventory']['bow'] = False
        chara['inventory']['woodenBox'] = 0
        chara['inventory']['berry'] = 0
        chara['reset'] = True
        
        # 无法正确运行的
        #chara = {
        #    'name': '',
        #    'gender': 0,
        #    'sexori': 0,
        #    'money': 15,
        #    'attribute': {
        #        'str': 0,
        #        'agi': 0,
        #        'phy': 0,
        #        'int': 0,
        #        'per': 0,
        #        'cha': 0
        #    },
        #    'inventory': {
        #        'bottle': False,
        #        'bottleWater': False,
        #        'palacePass': False,
        #        'bow': False,
        #        'woodenBox': 0,
        #        'berry': 0
        #    },
        #    'reset': True
        #}

        save()
    else:
        chara['reset'] = False
    os.system("clear")


# 角色初始化
def initChara():
    global chara
    if chara['reset']:
        name = input("※ 生命，我该如何称呼你？\n> ")

        # 当条件为真时循环
        gender = int(input("\n※ 你的性别是？[1为男/2为女]\n> "))
        while gender <= 0 and gender >= 3:
            gender = int(input("\n※ 请按照规则输入\n※ 你的性别是？[1为男/2为女]\n> "))
        sexori = int(input("\n※ 你的性取向是？[1为男/2为女]\n> "))
        while sexori <= 0 and sexori >= 3:
            sexori = int(input("\n※ 请按照规则输入\n※ 你的性取向是？[1为男/2为女]\n> "))
        print("\n※ 原来如此，生命……\n※ 现在，你的冒险即将开始……")
        chara['name'] = f'{name}'
        chara['gender'] = gender
        chara['sexori'] = sexori
        save()
        time.sleep(1)
        input("\n※ 回车以开始游戏 ※")
    else:
        print("※ 欢迎回来，生命，你的冒险即将继续……")
        time.sleep(1)
        input("\n※ 回车以开始游戏 ※")


# 开始游戏时人物属性随机生成
# 总计点数30，随机划分给六个属性
def attriGener():
    global chara
    totalPoints = 30
    times = 6

    while times >= 0 and totalPoints >= 0:


        pass


# 人物属性顶端UI
def attriUI():
    global chara
    name = chara['name']
    str = chara['attribute']['str']
    agi = chara['attribute']['agi']
    phy = chara['attribute']['phy']
    int = chara['attribute']['int']
    per = chara['attribute']['per']
    cha = chara['attribute']['cha']
    money = chara['money']

    os.system("clear")
    print(name + '\n' + 
            f'力量：{str}\n' + f'敏捷：{agi}\n' + f'体质：{phy}\n' + 
            f'智力：{int}\n' + f'感知：{per}\n' + f'魅力：{cha}\n' + 
            f'金币：{money}\n' +
            '—————————————————————————————')


# 保存数据
def save():
    with open(charaPath, 'w', encoding='utf8') as f:
        json.dump(chara, f, ensure_ascii=False, indent=4)