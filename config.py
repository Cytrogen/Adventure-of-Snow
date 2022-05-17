# 存各种配置的


from data_source import *


# 文件路径PATH
TEXT_PATH = Path("story/")
STORY_PATH = Path("story/story/")
CHARA_PATH = Path("character/")

# json数据读取
welcomePath = os.path.join(TEXT_PATH, "welcome.json")
charaPath = os.path.join(CHARA_PATH, "character.json")
