# 存各种乱七八糟的东西的


import os
import time
import random
from pathlib import Path
from decimal import Decimal
try:
    import ujson as json
except ModuleNotFoundError:
    import json