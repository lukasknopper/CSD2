print("Hello, world!")

#random importeren
import random

#fractal grid rhythm generator
#bepaal maatsoort eisen
numerator = 7
denominatorDur = 0.5
totalDur = numerator * denominatorDur

#bereken de eerstegraads nootlengtes
# a - b -
a = random.randint(1, numerator - 1)
b = numerator - a
aDur = a * denominatorDur
bDur = b * denominatorDur

#bereken de tweedegraads nootlengtes
# a - c - b - d - 
c = random.randint(1, numerator - 1)
d = numerator - c
cDur = (aDur / numerator) * c
dDur = (bDur / numerator) * d

#bereken de derdegraads nootlengtes
# a - e - c - f - b - g - d - h -
e = random.randint(1, numerator - 1)
f = numerator - e
g = random.randint (1, numerator - 1)
h = numerator - g
eDur = ((aDur - cDur) / numerator) * e
fDur = (cDur / numerator) * f
gDur = ((bDur - dDur) / numerator) * g
hDur = (dDur / numerator) * h

# a - e - c - f - b - g - d - h -
#fix nootlengtes
aDur = aDur - (cDur + eDur)
cDur = cDur - fDur
bDur = bDur - (dDur + gDur)
dDur = dDur - hDur

#verzamelen in een lijst
durArray = [aDur, eDur, cDur, fDur, bDur, gDur, dDur, hDur]
print(durArray)

#TODO idee om te kleine nootwaarden samen te voegen met vorige noten

#TODO playback mogelijk maken
# -- speel geluid, wacht

