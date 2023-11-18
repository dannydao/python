from television import Television

def test_instance():
    TV = Television()
    assert TV._Television__status == False
    assert TV._Television__muted == False
    assert TV._Television__volume == Television.MIN_VOLUME
    assert TV._Television__channel == Television.MIN_CHANNEL

def test_power():
    TV = Television()
    TV.power()
    assert TV._Television__status == True
    TV.power()
    assert TV._Television__status == False

def test_mute():
    TV = Television()
    TV.mute()
    assert TV._Television__muted == False
    TV.power()
    TV.mute()
    assert TV._Television__muted == True
    assert TV._Television__volume == Television.MIN_VOLUME

def test_channel_up():
    TV = Television()
    TV.power()
    TV.channel_up()
    assert TV._Television__channel == Television.MIN_CHANNEL + 1
    TV._Television__channel = Television.MAX_CHANNEL
    TV.channel_up()
    assert TV._Television__channel == Television.MIN_CHANNEL

def test_channel_down():
    TV = Television()
    TV.power()
    TV.channel_down()
    assert TV._Television__channel == Television.MAX_CHANNEL
    TV._Television__channel = Television.MIN_CHANNEL
    TV.channel_down()
    assert TV._Television__channel == Television.MAX_CHANNEL

def test_volume_up():
    TV = Television()
    TV.power()
    TV.mute()
    TV.volume_up
    assert TV._Television__volume == Television.MIN_VOLUME
    TV._Television__volume = Television.MAX_VOLUME
    TV.volume_up
    assert TV._Television__volume == Television.MAX_VOLUME

def test_volume_down():
    TV = Television()
    TV.power()
    TV.mute()
    TV.volume_down()
    assert TV._Television__volume == Television.MIN_VOLUME
    TV.volume_down()
    assert TV._Television__volume == Television.MIN_VOLUME


