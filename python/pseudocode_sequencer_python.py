print("Hello, world!")

#random importeren
import random

#fractal grid rhythm generator
#bepaal maatsoort eisen
numerator = 7
denominatorDur = 0.5
totalDur = numerator * denominatorDur

#TODO idee om te kleine nootwaarden samen te voegen met vorige noten

#TODO playback mogelijk maken
# -- speel geluid, wacht

#TODO code herformuleren

#genereer een nummer om de maat op te delen
division = random.randrange(1, numerator)/numerator
print(division)
#voor elke noot 1 for loop formule bedenken
#aantal recursieve divisions
depth = 3
#notenaantal berekenen
N = (2 ** depth)
durations = [totalDur]


def isEven (value):
    return (value % 2) == 0

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
        print(durations)
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



