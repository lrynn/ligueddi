from ball import *
from player import *
from time import sleep

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

tick = 45*60*2

while (tick):
    eventTrigger = True
    tick -= 1
    if (eventTrigger):
        print(displayTime(tick))