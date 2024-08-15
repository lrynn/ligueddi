from numpy import array
class Player:
    def __init__(self, name, num, height, weight, visualAngle, visualAcuity,
                 intellect, spacePerception, acceleration, rightAccuracy, leftAccuracy,
                 kickPower, headerAccuracy, standingStability, hollywoodAction, composure, cooperation) -> None:
        self.position = array([0,0])
        self.name = name
        self.num = num
        # 공용 능력치 설정
        self.allHeight = height                             # 키
        self.allWeight = weight                             # 몸무게
        self.allVisualAngle = visualAngle                   # 시야각
        self.allVisualAcuity = visualAcuity                 # 동체 시력
        self.allIntellect = intellect                       # 지능
        self.allSpacePerception = spacePerception           # 공간지각
        self.allAcceleration = acceleration                 # 가속력
        self.allRightAccuracy = rightAccuracy               # 오른발 정확도
        self.allLeftAccuracy = leftAccuracy                 # 왼발 정확도
        self.allKickPower = kickPower                       # 킥력
        self.allHeaderAccuracy = headerAccuracy             # 헤더 정확도
        self.allStandingStability = standingStability       # 안정성
        self.allHollywoodAction = hollywoodAction           # 연기력
        self.allComposure = composure                       # 평정심
        self.allCooperation = cooperation                   # 협력 <- 능력치가아니라 성향
        # 골키퍼 성향 설정
        self.golNeuer = 0                  # 김병지
        self.golLongBall = 0               # 롱볼 얼마나 떨구냐
        self.golBoldness = 0               # 과감성
        # 수비수 성향 설정
        self.defAimOffside = 0             # 오프사이드 만들기
        self.defBanzaiDash = 0             # 개돌
        # 미드필더 성향 설정
        self.midMyBall = 0                 # 개인주의
        self.midGoalDesire = 0             # 골 넣고 싶어함
        # 공격수 성향 설정
        self.stkHeader = 0                 # 헤더 선호도

    def passBall(self, target):
        pass

    def dribble(self, encounter):
        pass

    def jumpWithEnemy(self):
        pass

    def tackle(self):
        pass

class Goaley(Player):
    def __init__(self, name, num, height, weight, visualAngle, visualAcuity, intellect, spacePerception, acceleration, rightAccuracy, leftAccuracy, kickPower, headerAccuracy, standingStability, hollywoodAction, composure, cooperation,
                 neuer, longball, boldness) -> None:
        super().__init__(name, num, height, weight, visualAngle, visualAcuity, intellect, spacePerception, acceleration, rightAccuracy, leftAccuracy, kickPower, headerAccuracy, standingStability, hollywoodAction, composure, cooperation)
        self.golNeuer = neuer
        self.golLongBall = longball
        self.golBoldness = boldness

    def goalkick(self):
        pass

    def catchBall(self):
        pass

    def dive(self):
        pass

class Defender(Player):
    def __init__(self, name, num, height, weight, visualAngle, visualAcuity, intellect, spacePerception, acceleration, rightAccuracy, leftAccuracy, kickPower, headerAccuracy, standingStability, hollywoodAction, composure, cooperation,
                 aimOffside, banzaiDash) -> None:
        super().__init__(name, num, height, weight, visualAngle, visualAcuity, intellect, spacePerception, acceleration, rightAccuracy, leftAccuracy, kickPower, headerAccuracy, standingStability, hollywoodAction, composure, cooperation)
        self.defAimOffside = aimOffside
        self.defBanzaiDash = banzaiDash

class Midfielder(Player):
    def __init__(self, name, num, height, weight, visualAngle, visualAcuity, intellect, spacePerception, acceleration, rightAccuracy, leftAccuracy, kickPower, headerAccuracy, standingStability, hollywoodAction, composure, cooperation,
                 myBall, goalDesire) -> None:
        super().__init__(name, num, height, weight, visualAngle, visualAcuity, intellect, spacePerception, acceleration, rightAccuracy, leftAccuracy, kickPower, headerAccuracy, standingStability, hollywoodAction, composure, cooperation)
        self.midMyBall = myBall
        self.midGoalDesire = goalDesire

class Striker(Player):
    def __init__(self, name, num, height, weight, visualAngle, visualAcuity, intellect, spacePerception, acceleration, rightAccuracy, leftAccuracy, kickPower, headerAccuracy, standingStability, hollywoodAction, composure, cooperation,
                 header) -> None:
        super().__init__(name, num, height, weight, visualAngle, visualAcuity, intellect, spacePerception, acceleration, rightAccuracy, leftAccuracy, kickPower, headerAccuracy, standingStability, hollywoodAction, composure, cooperation)
        self.stkHeader = header