
import pygame
import time
import msvcrt

# from itertools import accumulate

#audio instellingen
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(32)

loop = ''
def loop_events(events_dict):
    global loop
    while not loop == 'y':
        loop = input('loop? (y/n): ')
    if loop == 'y':
        if msvcrt.kbhit():
            stop = msvcrt.getch().decode(errors='ignore').lower()
            if stop == 's':
                stop_events()
                print("Playback gestopt")
                return
        print("Druk 's' om te stoppen na de huidige sequence")
        play_events(events_dict)
        # niet-blokkerende check: stop als er een 's' ligt
        
def stop_events():
    global loop
    loop = 'n' 
    time.sleep(0.5)
    pygame.quit()

def play_events(events_dict):
    #playback starten
    startTime = time.perf_counter()
    for e in range(len(events_dict)):
        while (startTime + events_dict[f"event{e}"]["timestamp"]) - time.perf_counter() > 0:
            time.sleep(0.001)
        events_dict[f"event{e}"]["sample"].play()
    last_duration = time.perf_counter()
    while time.perf_counter() - last_duration < events_dict[f"event{len(events_dict) - 1}"]["duration"]:
        time.sleep(0.001)
    loop_events(events_dict)

#TODO time.sleep(0.001)