class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initializes values for power, mute, volume, channel"""
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__prev_vol = self.MIN_VOLUME

    def power(self):
        """Turns power on and off"""
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        """Mutes and unmutes the television. Volume is zero when muted
        and previous volume is restored when unmuted"""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_vol
            else:
                self.__muted = True
                self.__prev_vol = self.__volume
                self.__volume = self.MIN_VOLUME

    def channel_up(self):
        """Increases channel number"""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel = self.__channel + 1

    def channel_down(self):
        """Decreases channel number"""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel = self.__channel - 1

    def volume_up(self):
        """Increases volume. If TV is muted, it unmutes it and restores
        it to the previous volume"""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_vol
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """Decreases volume. If TV is muted, it unmutes it and restores
        it to the previous volume"""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_vol
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Returns the TVs current status, channel, and volume"""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"