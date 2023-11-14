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

    def power(self):
        self.__status = not self.__status   # self.__status = True
        pass

    def mute(self):
        pass
    
    def channel_up(self):
        pass

    def channel_down(self):
        pass

    def volume_up(self):
        pass

    def volume_down(self):
        pass

    def __str___(self):
        pass
