class Television:
    # Class Variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

def __init__(self):
    # Instance varibles
    self.__status = False
    self.__muted = False
    self.__volume = Television.MIN_VOLUME
    self.__channel = Television.MIN_CHANNEL
