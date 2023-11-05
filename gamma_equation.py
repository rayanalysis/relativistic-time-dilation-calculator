import math
import time

'''
This program was originally written to understand how much data a near-light-speed spacecraft could theoretically collect about a planet's evolution using an extremely precise long-range optical telescope aboard the spacecraft as it approaches the planet from extreme range.
'''

c = 299792458  # speed of light in m/s

def calculate_gamma(v):
    gamma = 1 / math.sqrt(1 - (v**2 / c**2))
    return round(gamma, 5)

# report spacecraft gamma
v = 299792422  # spacecraft speed in m/s
step_factor = 0.01
gamma = 0.0
day_hours = 365 * 24

def time_breakdown():
    years_per_hour = round(gamma / day_hours, 5)
    days_per_hour = round(years_per_hour * 365, 5)
    return days_per_hour

while v < c:
    try:
        gamma = calculate_gamma(v)
        percent_light = round(v / c, 10)
        percent_light = round(percent_light * 100, 10)
        days_per_hour = time_breakdown()
        print(f"At a speed of {v} m/s, ~{gamma} years pass on the planet for each year in the spacecraft." + '\n')
        print(f"The spacecraft is traveling at ~{percent_light}% light speed." + '\n')
        print(f"This is ~{days_per_hour} planet-days per spacecraft-hour." + '\n\n')
        v = round(v + step_factor, 5)
        time.sleep(0.1)
    except:
        print('Final domain reached.')
        break
