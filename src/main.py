# 상수 선언
VERSION = '0.0.0'
DEBUG = 1

from os import getcwd
if (DEBUG):
    print(getcwd())

from game import *

import json
with open('./src/locale/ko.json', 'r', encoding='utf8') as f:
    locale = json.load(f)
if (DEBUG):
    print('main.py', locale['debug']['loadLocale'])

