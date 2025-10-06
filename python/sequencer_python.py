#hallo!
print("Hello, world!")

#random importeren
import random
import pygame
import time

#vraag de gebruiker of het 5/4 of 7/4 moet zijn
#bepaal maatsoort eisen

# --- Vraag tempo (BPM) ---
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

# --- Vraag maatsoort ---
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



#TODO idee om te kleine nootwaarden samen te voegen met vorige noten

#TODO playback mogelijk maken
# -- speel geluid, wacht

#genereer een nummer om de maat op te delen
division = random.randrange(1, numerator)/numerator
print(f"verdelingswaarde: {division}")
#voor elke noot 1 for loop formule bedenken

#aantal recursieve divisions
initialDepth = 3
depth = initialDepth

#notenaantal berekenen
N = (2 ** depth)
durations = [totalDur]

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
        #dictionary maken
        durations_dict = {i: {"dur": d} for i, d in enumerate(durations)}
        #tags voorbereiden
        tags = ["high", "mid", "low"]
        #tags toevoegen aan de dictionary
        for t in range(initialDepth):
            for j in range(0, len(durations_dict), 2**t):
                durations_dict[j]["layer"] = tags[t]
            
        print(durations_dict)
        return durations
        
fractals(depth)

#Dur1 = totalDur * division * division * division
#Dur2 = totalDur * division * division * (1 - division)
#Dur3 = totalDur * division * (1 - division) * division
#Dur4 = totalDur * division * (1 - division) * (1 - division)
#Dur5 = totalDur * (1 - division) * division * division
#Dur6 = totalDur * (1 - division) * division * (1 - division)
#Dur7 = totalDur * (1 - division) * (1 - division) * division
#Dur8 = totalDur * (1 - division) * (1 - division) * (1 - division)



