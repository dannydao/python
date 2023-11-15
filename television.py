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

    def mute(self):
        self.__muted = not self.__muted     # self.__muted = True
    
    def channel_up(self):
        if self.__status:
            self.__channel += 1     # Increase channel by 1 (max of 3) as long as self.__status is True
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL     # Replaces the minimum channel count with current count

    def channel_down(self):
        if self.__status:
            self.__channel -= 1     # Decreases channel by 1 as long as self.__status is True
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL     # Replaces the maximum channel with the current count

    def volume_up(self):
        pass

    def volume_down(self):
        pass

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
