import unittest
from television import Television

class TestTelevision(unittest.TestCase):

    def setUp(self):
        self.tv = Television()

    def test_power_on(self):
        self.tv.power()
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")

    def test_power_off(self):
        self.tv.power()
        self.tv.power()
        self.assertEqual(str(self.tv), "Power = False, Channel = 0, Volume = 0")

    def test_mute(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")
        self.tv.mute()
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 1")

    def test_channel_up(self):
        self.tv.power()
        self.tv.channel_up()
        self.assertEqual(str(self.tv), "Power = True, Channel = 1, Volume = 0")
        self.tv.channel_up()
        self.assertEqual(str(self.tv), "Power = True, Channel = 2, Volume = 0")
        self.tv.channel_up()
        self.assertEqual(str(self.tv), "Power = True, Channel = 3, Volume = 0")
        self.tv.channel_up()
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")

    def test_channel_down(self):
        self.tv.power()
        self.tv.channel_down()
        self.assertEqual(str(self.tv), "Power = True, Channel = 3, Volume = 0")
        self.tv.channel_down()
        self.assertEqual(str(self.tv), "Power = True, Channel = 2, Volume = 0")
        self.tv.channel_down()
        self.assertEqual(str(self.tv), "Power = True, Channel = 1, Volume = 0")
        self.tv.channel_down()
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")

    def test_volume_up(self):
        self.tv.power()
        self.tv.volume_up()
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 1")
        self.tv.volume_up()
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 2")

    def test_volume_down(self):
        self.tv.power()
        self.tv.volume_down()
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")
        self.tv.volume_up()
        self.tv.volume_down()
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")


if __name__ == '__main__':
    unittest.main()