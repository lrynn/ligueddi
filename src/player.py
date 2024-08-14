from os import name

class Player:
    def __init__(self, name, num) -> None:
        self.name = name
        self.num = num
        self.siya = 0

class Goaley(Player):
    def __init__(self, name, num) -> None:
        super().__init__(name, num)
        self.siya = 1

class Defender(Player):
    def __init__(self, name, num) -> None:
        super().__init__(name, num)

class Midfielder(Player):
    def __init__(self, name, num) -> None:
        super().__init__(name, num)

class Striker(Player):
    def __init__(self, name, num) -> None:
        super().__init__(name, num)

goaley = Goaley('sex', 1)

print(goaley.siya)