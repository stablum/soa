import datetime
import time
import math

def mean(s): 
    return float(sum(s)) / float(len(s))

def std(s):
    avg = mean(s)
    variance = map(lambda x: (x - avg)**2, s)
    mean(variance)
    stand = math.sqrt(mean(variance))
    return stand

def now_timestamp():
    return int(time.mktime(datetime.datetime.now().timetuple()))

class Struct:
    def __init__(self, **entries): 
        self.__dict__.update(entries)

