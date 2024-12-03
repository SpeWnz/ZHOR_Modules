# Small wrapper for measuring time with the timedelta utility.
# The idea is to have a stopwatch object which can have many instances, as there it can be useful to have multiple stopwatches
# for different parts of a program.

from datetime import timedelta
import time

class Stopwatch():
    def __init__(self):
        pass

    __start = None
    __end   = None

    def start(self):
        self.__start = time.time()

    def stop(self):
        self.__end = time.time()


    def getTimeDelta(self):
        return str(timedelta(seconds=int(self.__end - self.__start)))