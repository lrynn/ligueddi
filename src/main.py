# 상수 선언
VERSION = '0.0.0'
DEBUG = 1

import os
if (DEBUG):
    print(os.getcwd())

import json
with open('./src/locale/ko.json', 'r', encoding='utf8') as f:
    locale = json.load(f)
if (DEBUG):
    print(locale['debug']['loadLocale'])

