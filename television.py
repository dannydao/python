class Television:
    """
    Object Television with constant variables
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """
        Instance Variables
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self):
        """
        Turns on and off the television by changing the value of the status variable.
        """
        self.__status = not self.__status

    def mute(self):
        """
        Mutes and unmutes television by changing the value of the mute variable
        and if television is muted then it is set to the minimum volume 0.
        """
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.__volume = Television.MIN_VOLUME

    def channel_up(self):
        """
        Increases the channel value when the television is on.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """
        Decreases the channel value when the television is on.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """
        Increase the volume when television is on, also increases volume if muted.
        """
        if self.__status:
            if self.__muted:
                if self.__volume < Television.MAX_VOLUME:
                    self.__volume += 1

    def volume_down(self):
        """
        Decreases the volume when the television is on and when the TV is on mute.
        """
        if self.__status:
            if not self.__muted:
                if self.__volume > Television.MIN_VOLUME:
                    self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns the values of the television object in the format of Power = [status], Channel = [channel],
        Volume = [volume].
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
