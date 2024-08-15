# 디버그용 상수 선언
DEBUG = 1

from math import sqrt

from main import locale
import main
import ball
import player

class GameField(ball.Field):
    def findPlayerOnRoute(self, ballAcceleration, ballPosition) -> list:
        '''
        returns list of player who can take the ball.
        '''
        pass

class GameBall(ball.Ball):
    def move(self):
        for i in range(3):
            self.position[i] += self.acceleration[i]

    def calcDistanceToPlayer(self, team, pos, i):
        '''
        loads distance to A PLAYER playerList[team][pos][i].
        '''
        playerPos = playerList[team][pos][i].position
        return sqrt((self.position[0] - playerPos[0])**2 + (self.position[1] - playerPos[1])**2) # type: ignore

    def findPlayerByDist(self, checkNear=True):
        '''
        FINDS nearest/farest player by team.
        '''
        result = [[], []]
        for team in range(2):
            for pos in range(1,4):
                for i in range(len(playerList[team][pos])):
                    if (checkNear):
                        if (self.calcDistanceToPlayer(team, pos, i) < self.calcDistanceToPlayer(result[0], result[1], result[2])):
                            result[team] = [team, pos, i]
                    else:
                        if (self.calcDistanceToPlayer(team, pos, i) > self.calcDistanceToPlayer(result[0], result[1], result[2])):
                            result[team] = [team, pos, i]
        return result
    
    def isBallOnAir(self):
        return bool(self.position[2])

    def canPlayerReach(self):
        '''
        assume whether players can reach to the ball.
        '''
        if (self.position[2] < 3):
            return True
        else:
            return False
    
    def kick(self, kicker:tuple):
        pass
    
    def throwin(self, thrower:tuple, position) -> None:
        '''
        execute a throwin sequence.
        '''
        pass

    def freekick(self, team, goalkick=False):
        '''
        execute a freekick or goalkick sequence.

        param 'team' MUST be either 0(blue) or 1(red)!
        '''
        self.acceleration = 0

        # 키커 구하기
        kicker = [0,0] # [num, stat]
        if (goalkick):
            kicker[0] = playerList[team][0]
        else:
            for pos in playerList[team]:
                for player in pos:
                    if (player.allKickPower > kicker[1]):
                        kicker = [player.num, player.allKickPower]
        # 킥 하기
        self.kick(tuple(kicker))
    
# 플레이어 생성 시작
playerList = [[0,[],[],[]], [0,[],[],[]]]

class Blue:
    pass

class Red:
    pass

class BlueGoaley(Blue, player.Goaley):
    pass

# 경기 시작을 위한 준비
tick = 45*60*2
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
    
eventTrigger = False
infoLevel = 0 # 0: 전부, 1: 주요, 2: 핵심
eventName = ''
eventLevel = 1
while (tick):
    tick -= 1
    if (eventTrigger and infoLevel < eventLevel):
        print(displayTime(tick))
        print(locale['game']['eventOccured'])

        foo = int(input()) # 사용자가 확인할 때까지 경기 중단시키는 용도
        infoLevel = foo if foo in (0,1,2) else infoLevel
        eventTrigger = False
        eventName = ''
        eventLevel = 1