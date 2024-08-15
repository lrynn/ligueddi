# 상수 선언
VERSION = '0.0.0'
DEBUG = 1

from os import getcwd
if (DEBUG):
    print(getcwd())

from game import *

if (DEBUG):
    print('main.py', locale['debug']['loadLocale'])

# 앙 리그띠 코드 불러오기