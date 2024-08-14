import numpy as np

class Ball:
    def __init__(self) -> None:
        self.acceleration = np.array([0,0,0])
        self.position = np.array([0,0,0])