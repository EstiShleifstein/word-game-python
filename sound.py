from winsound import Beep
import time

class Sound:
    def __init__(self):
        self.playing = False

    def play_tick_tock(self):
        self.playing = True
        while self.playing:
            Beep(600,300)
            time.sleep(0.1)
            Beep(800,300) #higher frequency sound
            time.sleep(0.1)
    
    def stop_sound(self):
        self.playing = False

    def play_alarm(self):
        for _ in range(10):
            Beep(2500,500)
            time.sleep(0.001)
            Beep(2500,500)
            time.sleep(0.0001)
    
