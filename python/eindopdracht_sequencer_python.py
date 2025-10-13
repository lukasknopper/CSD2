#hallo!
print("Hello, world!")

#modules importeren
import random
import pygame
import time
import msvcrt

# vraag de gebruiker het tempo
while True:
    try:
        bpm_input = int(input("Kies tempo in BPM (40–240): "))
        if 40 <= bpm_input <= 240:
            BPM = bpm_input
            break
        else:
            print("BPM moet tussen 40 en 240 liggen.")
    except ValueError:
        print("Typ een getal, geen tekst.")

print(f"Gekozen tempo: {BPM} BPM")

# vraag de gebruiker of het 5/4 of 7/4 moet zijn
while True:
    choice = input("Kies maatsoort (5 of 7): ")
    if choice in ["5", "7"]:
        numerator = int(choice)
        break
    else:
        print("Ongeldige invoer. Typ '5' of '7'. Probeer opnieuw.")

denominatorDur = 60 / BPM
totalDur = numerator * denominatorDur

print(f"Gekozen maat: {numerator}/4  → totale duur = {totalDur} seconds")

#genereer een nummer om de maat op te delen
division = random.randrange(1, numerator)/numerator
print(f"verdelingswaarde: {division}")

#aantal recursieve divisions
initialDepth = 3
depth = initialDepth

N = (2 ** depth)
durations = [totalDur]
events_dict = {}
tags = ["high", "mid", "low"]

#even of oneven boolean
def isEven (value):
    return (value % 2) == 0

#fractal grid rhythm generator
def fractals (depth):
    if (depth > 0):
        for i in range(len(durations) * 2):
            if (isEven(i)):
                lastValue = durations[i]
                splitValue = lastValue * division
                durations[i] = splitValue
            else:
                durations.insert(i, (lastValue - splitValue))
        fractals (depth - 1)
    else:  
        #omzetten naar timestamps
        from itertools import accumulate
        timestamps_list = list(accumulate(durations, initial= 0.0))[:-1]
        #dictionary maken
        for i, d in enumerate(timestamps_list):
            events_dict[f"event{i}"] = {"timestamp": d, "duration": durations[i]} 
        #tags toevoegen aan de dictionary
        for t in range(initialDepth):
            for j in range(0, len(events_dict), 2**t):
                events_dict[f"event{j}"]["layer"] = tags[t]
        print(durations)
        print(events_dict)
        return events_dict

fractals(depth)

#audio instellingen
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(32)

#samples opslaan
samples_dict = {
    "high": pygame.mixer.Sound(r"C:\Users\lukas\Downloads\pysamples\pyhat.wav"), 
    "mid": pygame.mixer.Sound(r"C:\Users\lukas\Downloads\pysamples\pyperc.wav"), 
    "low": pygame.mixer.Sound(r"C:\Users\lukas\Downloads\pysamples\pykick.wav")}

loop = ''
def loop_events():
    global loop
    while not loop == 'y':
        loop = input('loop? (y/n): ')
    if loop == 'y':
        if msvcrt.kbhit():
            ch = msvcrt.getch().decode(errors='ignore').lower()
            if ch == 's':
                stop_events()
                return
        print("Druk 's' om te stoppen na de huidige sequence")
        play_events(events_dict, samples_dict)
        # niet-blokkerende check: stop als er een 's' ligt
        

def stop_events():
    global loop
    loop = 'n' 
    time.sleep(0.5)
    pygame.quit()

def play_events(events_dict, samples_dict):
    #playback starten
    startTime = time.perf_counter()
    for e in range(len(events_dict)):
        remain = (startTime + events_dict[f"event{e}"]["timestamp"]) - time.perf_counter()
        if remain > 0:
            time.sleep(remain)
        samples_dict[events_dict[f"event{e}"]["layer"]].play()
        time.sleep(events_dict[f"event{e}"]["duration"])
    loop_events()

play_events(events_dict, samples_dict)



