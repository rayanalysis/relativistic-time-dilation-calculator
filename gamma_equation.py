import math
import time
import os

'''
This program was originally written to understand how much data a near-light-speed spacecraft could theoretically collect about a planet's evolution using an extremely precise long-range optical telescope aboard the spacecraft as it approaches the planet from extreme range.

We should consider the energy usage from the conversion of mass presumably, especially as it approaches the mass of the observable universe. But perhaps it could come from other domains. Ultimately our study of the theoretical speed of a spacecraft as it approaches c is limited by the decimal precision of our simulation, as well as the required energy which scales to an infinite limit.
'''

c = 299792458  # speed of light in m/s

def calculate_gamma(v, step_precision):
    gamma = 1 / math.sqrt(1 - (v**2 / c**2))
    return round(gamma, step_precision)

# report spacecraft gamma
v = 299792457.99999000001  # spacecraft speed in m/s
step_factor = 0.0000001  # fine-tuned step factor
gamma = 0
day_hours = 365 * 24
step_precision = 18  # PC float precision is generally around 16 or 17
double_precision = step_precision * 2
results = []

def time_breakdown(step_precision):
    years_per_hour = round(gamma / day_hours, step_precision)
    days_per_hour = round(years_per_hour * 365, step_precision)
    return days_per_hour

while True:
    time.sleep(0.2)
    if v < c:
        gamma = calculate_gamma(v, step_precision)
        percent_light = round(v / c, double_precision)
        percent_light = round(percent_light * 100, double_precision)
        days_per_hour = time_breakdown(step_precision)
        v = round(v + step_factor, step_precision)
        results.append(f"At a speed of {v} m/s, ~{gamma} years pass on the planet for each year in the spacecraft." + '\n')
        results.append(f"The spacecraft is traveling at ~{percent_light}% light speed." + '\n')
        results.append(f"This is ~{days_per_hour} planet-days per spacecraft-hour." + '\n\n')
           
        for s in results[len(results)-3:len(results)]:
            print(s)

    else:
        with open('lightspeed_results.txt') as results_file:
            results_file = results_file.read()
            out_v = open('lightspeed_results.txt', 'w')
            for s in results[len(results)-3:len(results)]:
                out_v.write(s)
            out_v.close()
        break

