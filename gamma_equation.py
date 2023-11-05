import math
import time


c = 299792458  # speed of light in m/s

def calculate_gamma(v):
    gamma = 1 / math.sqrt(1 - (v**2 / c**2))
    return gamma

# report spacecraft gamma
v = 299777180  # spacecraft speed in m/s
step_factor = 10
for x in range(int(c - v / step_factor)):
    try:
        gamma = calculate_gamma(v)
        percent_light = v/c
        print(f"At a speed of {v} m/s, {gamma} years pass on the planet for each year in the spacecraft.")
        print(f"The spacecraft is traveling at {percent_light}% light speed.")
        v += step_factor
        time.sleep(0.3)
    except:
        print('Final domain reached.')
        break
