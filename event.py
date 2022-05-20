# 事件树


from setting import *


chara = {}
chara = json.load(open(charaPath, 'r', encoding='utf8'))
story = json.load(open(storyPath, 'r', encoding="UTF-8"))


# 目标：
# 游戏分为 前期、中期、后期
#
# 魔王线：
# 前期故事发生在森林外围，在第15个固定事件【哥布林洞穴】结束
# 中期故事发生在森林内部，在第45个固定事件【魔王城】结束
#       第25个事件将必定出现围绕着6个属性的路线选择
# 后期故事发生在魔王城内部，在第90个固定事件【魔王讨伐】结束


def eventTree():
    global chara, story
    number = 1

    # number为循环次数，或事件总数，总计14次（前期）
    while number <= 14:
        # 事先声明
        event = story['0']

        # 如果"no"非当前的事件数，则循环一直到匹配为止
        while event['no'] != number:
            # tag为事件编号
            tag = random.randint(1, 2)
            event = story[f'{tag}']

        attriUI()

        # 该事件可以出现在第no个事件的随机范围内
        print(f"\n※ 第{event['no']}个事件：\n")

        # storyTimes为该事件会有几次文本
        # 最初的事件介绍为1，完成选择后的文本为2，以此类推
        #
        # 如果该事件的storyTimes的is_continue为真，即这之后还有一次选择和文本，就循环一直到最后的storyTimes的is_continue为假
        storyTimes = 1
        event = event['description']
        choice = 1
        print(event[f'{storyTimes}'][f'{choice}Descript'])

        while event[f'{storyTimes}']['is_continue']:
            # choiceTimes为该事件的storyTimes的选项数量
            choiceTimes = event[f'{storyTimes}']['choice']['times']
            num = 1

            # 循环choiceTimes次以展现出所有的有效选项
            while num <= choiceTimes:
                print(event[f'{storyTimes}']['choice'][f'{num}'])
                num = num + 1
            choice = int(input("※ 你的选择是？\n> "))

            while choice <= 0 or choice >= choiceTimes:
                choice = int(input("\n※ 这不是一个有效的选择，请重试\n※ 你的选择是？\n> "))
            
            storyTimes = storyTimes + 1
            print(event[f'{storyTimes}'][f'{choice}Descript'])

        # 事件完成后结算奖励
        # 未完成
        event = event['gain']
        chara['attribute']['str'] += event['attribute']['str']
        chara['attribute']['agi'] += event['attribute']['agi']
        chara['attribute']['phy'] += event['attribute']['phy']
        chara['attribute']['per'] += event['attribute']['per']
        chara['attribute']['int'] += event['attribute']['int']
        chara['attribute']['cha'] += event['attribute']['cha']
        save()

        number += 1
        time.sleep(3)
        input("\n※ 回车以继续前进 ※")
        os.system("clear")