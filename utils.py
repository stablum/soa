import datetime
import time
import math

def mean(a): 
    count = float(len(a))
    if count == 0:
       raise Exception("unable to make mean with no elements")
    s = float(sum(a))
    return float(s) / float(count)

def std(a):
    avg = mean(a)
    variance = map(lambda x: (x - avg)**2, a)
    mean(variance)
    stand = math.sqrt(mean(variance))
    return stand

def now_timestamp():
    return int(time.mktime(datetime.datetime.now().timetuple()))

class Struct:
    def __init__(self, **entries): 
        self.__dict__.update(entries)

