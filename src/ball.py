import numpy as np

fieldSize = [900,700]

class Field:
    def __init__(self) -> None:
        self.grid = np.array(fieldSize)

    def findPlayerOnRoute(self, ballAcceleration, ballPosition):
        pass

class Ball:
    def __init__(self) -> None:
        self.acceleration = np.array([0.0,0.0,0.0])
        self.position = np.array([0.0,0.0,0.0])

    def setThrowinPosition(self) -> None:
        '''
        set ball's position valid to throwin.
        '''
        for i in range(2):
            if (self.position[i] < 0):
                self.position[i] = 0
            if (self.position[i] > fieldSize[i]):
                self.position[i] = fieldSize[i]

    def changePosition(self):
        '''
        changes ball's position.

        return (position[x][y][z]) when the ball goes out of limit of field.
        '''
        for i in range(3):
            self.position[i] += self.acceleration[i]
        if (self.position[2] < 0):
            self.position[2] = -(self.position[2])

        for i in range(2):
            if (self.position[i] < 0 or self.position[i] > fieldSize[i]): # 라인 넘어갔을 때
                self.setThrowinPosition()
                return self.position