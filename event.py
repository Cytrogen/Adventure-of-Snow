# 事件树


from setting import *


def eventTree():
    global chara, story
    number = 1

    # number为循环次数，或事件总数，总计14次（前期）
    while number <= 14:
        tag = random.randint(1, 7)
        while story[f'{tag}']['no'] == number:
            attriUI()
            print(f"※ 第{story[f'{tag}']['no']}个事件：\n")
            print(story[f"{tag}"]['description']['eventDescription'])

            nextEvent = ifChoice(tag)

            if 'null' in nextEvent:
                print("\n※ 判断失败，你死了！ ※")
                time.sleep(3)
                input("\n※ 回车以接受自己死亡的命运 ※")
                os._exit()
            else:
                print(nextEvent)

            number = number + 1
            time.sleep(1)
            input("\n※ 回车以继续前进 ※")
            os.system("clear")


def ifChoice(tag):
    global chara, story

    if story[f"{tag}"]['description']['is_choice']:
        num = 1
        print('\n')

        # 输出所有的选项
        printAllChoices(num, tag)
        
        inputChoice = int(input("\n※ 你的选择是？\n> "))

        # print("开始查错")
        checkInputChoice(tag, inputChoice)

        num = 1
        # print("开始找inputChoice")
        while num <= story[f'{tag}']['choice'][f'{inputChoice}']['requirement']['times']:
            # print("开始找attriNeeded")
            attriNeeded = story[f'{tag}']['choice'][f'{inputChoice}']['requirement'][f'{num}']['attributes']['name']
                    
            # print("开始检查属性数值")
            if chara['attribute'][f'{attriNeeded}'] >= story[f'{tag}']['choice'][f'{inputChoice}']['requirement'][f'{num}']['attributes']['volume']:
                # print("开始获取所需道具名")
                invenNeeded = story[f'{tag}']['choice'][f'{inputChoice}']['requirement'][f'{num}']['inventory']['name']
                    
                # print("开始检查道具名")
                if 'null' in invenNeeded:
                    num = num + 100
                else:
                    charaInven = chara['inventory'][f'{invenNeeded}']

                    # 获取所需的道具值
                    invenVolume = story[f'{tag}']['choice'][f'{inputChoice}']['requirement'][f'{num}']['inventory']['volume']

                    # print("开始检查道具数值")
                    # 如果角色道具值大于所需道具值
                    if charaInven >= invenVolume:
                        # 获取下一个事件描述号码
                        print("\n\n")
                        nextEvent = story[f'{tag}']['choice'][f'{inputChoice}']['requirement'][f'{num}']['if_true']["eventDescription"]
                        # 结算奖励
                        # inputChoice = str(inputChoice)
                        # num = str(num)
                        rewardYesChoice(tag, num, inputChoice)
                        num = num + 100
                    else:
                        # print("num + 1")
                        num = num + 1
            # 如果角色属性小于所需属性
            else:
                num = num + 1
                # 如果没有直接死亡
                if not story[f'{tag}']['choice'][f'{inputChoice}']['requirement'][f'{num}']['if_false']['killed']:
                    print("\n\n")
                    nextEvent = story[f'{tag}']['choice'][f'{inputChoice}']['requirement'][f'{num}']['if_false']['eventDescription']
                    # 开始惩罚
                    punish(tag, num, inputChoice)
                # 直接死亡
                else:
                    nextEvent = 'null'
    else:
        # 直接奖励
        rewardNoChoice(tag)
        nextEvent = story[f'{tag}']['description']['if_true']['eventDescription']
        
    return nextEvent


def printAllChoices(num, tag):
    global story
    while num <= story[f"{tag}"]['choice']['times']:
        print(str(num) + '. ' + story[f"{tag}"]['choice'][f'{num}']['text'])
        num += 1


def checkInputChoice(tag, inputChoice):
    global story
    while inputChoice <= 0 or inputChoice >= (story[f'{tag}']['choice']['times'] + 1):
        inputChoice = int(input("\n※ 这不是一个有效的选择，请重试\n※ 你的选择是？\n> "))


def rewardNoChoice(tag):
    global story, chara
    attrName = story[f'{tag}']['reward']['attributes']['attr']
    chara['attribute'][f'{attrName}'] = chara['attribute'][f'{attrName}'] + story[f'{tag}']['reward']['attributes']['volume']

    inveName = story[f'{tag}']['reward']['inventory']['inve']
    chara['inventory'][f'{inveName}'] = chara['inventory'][f'{inveName}'] + story[f'{tag}']['reward']['inventory']['volume']
    save()


def rewardYesChoice(tag, num, inputChoice):
    global story, chara
    rewardAttr = story[f'{tag}']['choice'][f'{inputChoice}']['requirement'][f'{num}']['if_true']['reward']['attributes']['name']
    rewardInve = story[f'{tag}']['choice'][f'{inputChoice}']['requirement'][f'{num}']['if_true']['reward']['inventory']['name']

    chara['attribute'][f'{rewardAttr}'] = chara['attribute'][f'{rewardAttr}'] + story[f'{tag}']['choice'][f'{inputChoice}']['requirement'][f'{num}']['if_true']['reward']['attributes']['volume']
    chara['inventory'][f'{rewardInve}'] = chara['inventory'][f'{rewardInve}'] - story[f'{tag}']['choice'][f'{inputChoice}']['requirement'][f'{num}']['if_true']['reward']['inventory']['volume']
    save()


def punish(tag, num, inputChoice):
    global story, chara
    punishAttr = story[f'{tag}']['choice'][f'{inputChoice}']['requirement'][f'{num}']['if_false']['punishment']['attributes']['name']
    punishInve = story[f'{tag}']['choice'][f'{inputChoice}']['requirement'][f'{num}']['if_false']['punishment']['inventory']['name']

    chara['attribute'][f'{punishAttr}'] = chara['attribute'][f'{punishAttr}'] - story[f'{tag}']['choice'][f'{inputChoice}']['requirement'][f'{num}']['if_false']['punishment']['attributes']['volume']
    chara['inventory'][f'{punishInve}'] = chara['inventory'][f'{punishInve}'] - story[f'{tag}']['choice'][f'{inputChoice}']['requirement'][f'{num}']['if_false']['punishment']['inventory']['volume']
    save()