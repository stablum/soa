import datetime
import time
import math

def mean(a): 
    count = float(len(a))
    if count == 0:
       raise Exception("unable to make mean with no elements")
    s = float(sum(a))
    return float(s) / float(count)

def harmean(a):
    
    # removing values 0 in the list 'a'
    a_filt = filter(lambda x: x != 0, a)
    
    a_no_inf = [ 99999 if x > 99999 else x for x in a_filt ]

    # calculating harmonic mean
    s = sum([1.0 /x for x in a_no_inf])
    
    if s == 0:
        raise Exception("harmean: sum is 0; a="+str(a)+",a_filt="+str(a_filt)+",a_no_inf="+str(a_no_inf))
    
    hm = float(len(a)) / float(s)
    return hm

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

