# 存各种乱七八糟的东西的


import os
import random
from pathlib import Path
try:
    import ujson as json
except ModuleNotFoundError:
    import json