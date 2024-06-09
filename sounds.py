# from winsound import Beep

# class Sound:
#     def __init__(self):
#         self.playing = False

#     def play_tick_tock(self):
#         start_time = time.time()
#         total_seconds = 30
        
#         self.playing = True
#         while time.time() - start_time < total_seconds:
#             Beep(600,100)
#             Beep(800,100) #higher frequency sound 
           
    
#     def stop_sound(self):
#         self.playing = False

#     def play_alarm(self):
#         for _ in range(5):
#             Beep(2500,500)
#             time.sleep(0.05)