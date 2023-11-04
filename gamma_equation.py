import math


c = 299792458  # speed of light in m/s

def calculate_gamma(v):
    gamma = 1 / math.sqrt(1 - (v**2 / c**2))
    return gamma

# report spacecraft gamma
v = 299777100 # spacecraft speed in m/s
gamma = calculate_gamma(v)
percent_light = v/c
print(f"At a speed of {v} m/s, {gamma} years pass on the planet for each year in the spacecraft.")
print(f"The spacecraft is traveling at {percent_light}% light speed.")
