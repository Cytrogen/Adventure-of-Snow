# 游戏主程序


from config import *


welcomePath = os.path.join(TEXT_PATH, "welcome.json")


title = json.load(open(welcomePath, 'r', encoding="UTF-8")).get('title')
titlePost = random.choice(title)
print(titlePost)

hint = json.load(open(welcomePath, 'r', encoding="UTF-8")).get('hint')
hintPost = random.choice(hint)
print('\n' + hintPost)