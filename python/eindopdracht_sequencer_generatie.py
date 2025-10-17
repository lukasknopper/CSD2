import random
import pygame
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(32)
from typing import List

#even of oneven boolean
def isEven (value):
    return (value % 2) == 0

depth = 3

#fractal grid rhythm generator
def make_fractal_rhythm_event_dict(depth, numerator, totalDur, durations = None, division = None):
    if durations is None:
        durations = [totalDur]
    if division is None:
        division = random.randrange(1, numerator) / numerator
        print(f"verdelingswaarde: {division}")
    if depth > 0:
        for i in range(len(durations) * 2):
            if (isEven(i)):
                lastValue = durations[i]
                splitValue = lastValue * division
                durations[i] = splitValue
            else:
                durations.insert(i, (lastValue - splitValue))
        depth = depth - 1
        return make_fractal_rhythm_event_dict(depth, numerator, totalDur, durations, division)
    else:  
        #omzetten naar timestamps
        from itertools import accumulate
        timestamps_list = list(accumulate(durations, initial= 0.0))[:-1]
        #dictionary maken
        events_dict = {}
        for i, d in enumerate(timestamps_list):
            events_dict[f"event{i}"] = {"timestamp": d, "duration": durations[i]} 
        #tags toevoegen aan de dictionary
        tags = ["high", "mid", "low"]
        #samples koppelen
        samples_dict = {
            "high": pygame.mixer.Sound(r"C:\Users\lukas\Downloads\pysamples\pyhat.wav"), 
            "mid": pygame.mixer.Sound(r"C:\Users\lukas\Downloads\pysamples\pyperc.wav"), 
            "low": pygame.mixer.Sound(r"C:\Users\lukas\Downloads\pysamples\pykick.wav")}
        for t in range(3):
            for j in range(0, len(events_dict), 2**t):
                events_dict[f"event{j}"]["layer"] = tags[t]
                for l in range(len(tags)):
                    if events_dict[f"event{j}"]["layer"] == tags[l]:
                        events_dict[f"event{j}"]["sample"] = samples_dict[tags[l]]
                    
        print(durations)
        print(events_dict)
        return events_dict