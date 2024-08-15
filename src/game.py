# 디버그용 상수 선언
DEBUG = 1

import json
from math import sqrt

from numpy import number
with open('./src/locale/ko.json', 'r', encoding='utf8') as f:
    locale = json.load(f)

from ball import *
from player import *

class GameBall(Ball):
    def calcDistanceToPlayer(self, team, pos, i):
        playerPos = playerList[team][pos][i].position
        return sqrt((self.position[0] - playerPos[0])**2 + (self.position[1] - playerPos[1])**2)

    def findPlayerByDist(self, checkNear=True):
        result = [[], []]
        for team in range(2):
            for pos in range(1,4):
                for i in range(len(playerList[team][pos])):
                    if (checkNear):
                        if (calcDistanceToPlayer(team, pos, i) < calcDistanceToPlayer(result[0], result[1], result[2])):
                            result[team] = [team, pos, i]
                    else:
                        if (calcDistanceToPlayer(team, pos, i) > calcDistanceToPlayer(result[0], result[1], result[2])):
                            result[team] = [team, pos, i]
        return result
    
def displayTime(tick, minute45=False):
    if (minute45):
        pass
    else:
        minute = str(89 - (tick // 60))
        if (len(minute)==1):
            minute = '0' + minute
        sec = str(59 - (tick % 60))
        if (len(sec)==1):
            sec = '0' + sec
        return minute + " : " + sec
    
playerList = [[0,[],[],[]], [0,[],[],[]]]

class Blue:
    pass

class Red:
    pass

class BlueGoaley(Blue, Goaley):
    pass

tick = 45*60*2
    
eventTrigger = False
infoLevel = 0 # 0: 전부, 1: 주요, 2: 핵심
eventName = ''
eventLevel = 1
while (tick):
    tick -= 1
    if (eventTrigger and infoLevel < eventLevel):
        print(displayTime(tick))
        print(locale['game']['eventOccured'])

        foo = int(input())
        infoLevel = foo if foo in (0,1,2) else infoLevel
        eventTrigger = False
        eventName = ''
        eventLevel = 1