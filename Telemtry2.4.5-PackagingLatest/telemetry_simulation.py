
import time
import random
import numpy as np

# Constants for simulation
APOGEE = 10000
DURATION = 60
UPDATE_INTERVAL = 0.1
WINDOW_SIZE = 30 * 60
COUNTDOWN_TIME = 21  # Countdown time in seconds
consoleValueID = 1007
ejectionVariable = 0

def telemetry_simulation():
    """ Simulates telemetry data """
    altitude = 0
    velocity = random.uniform(10, 20)
    
    data = []
    for _ in range(int(DURATION / UPDATE_INTERVAL)):
        altitude += velocity * UPDATE_INTERVAL
        if altitude >= APOGEE:
            break
        data.append(altitude)
        time.sleep(UPDATE_INTERVAL)
    
    return data

def countdown_timer():
    """ Simulates a countdown timer """
    for i in range(COUNTDOWN_TIME, 0, -1):
        print(f"T-minus {i} seconds")
        time.sleep(1)
    print("Launch!")
