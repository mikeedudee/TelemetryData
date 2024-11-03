import cupy as cp
import time

def read_values_for_simulation():
    with open('cutdata.txt', 'r') as file:
        lines = file.readlines()  # Read all lines
        values = [line.strip().split() for line in lines]  # Split by tabs or spaces
    return values

def writingvalue():
    values = read_values_for_simulation()  # Read all rows at once
    
    for value in values:
        if value:
            try:
                # Convert necessary values to float for numerical computations
                groupNumber     = float(value[0])
                Temperature     = float(value[1])
                Pressure        = float(value[2])
                altitude        = float(value[3]) + 4  # Adjust altitude
                Longitude       = float(value[4])
                Latitude        = float(value[5])
                SDStatus        = float(value[6])
                GyroSensorYaw   = float(value[7])
                GyroSensorPitch = float(value[8])
                GyroSensorRoll  = float(value[9])

                # Store values in an array
                x = [groupNumber, Temperature, Pressure, altitude, Longitude, Latitude, SDStatus, GyroSensorYaw, GyroSensorPitch, GyroSensorRoll]
                x_gpuTest = cp.array(x)  # Transfer to GPU

                # Print individual values to simulate output
                print(f"{x_gpuTest[0]:.2f} | {x_gpuTest[1]:.2f} | {x_gpuTest[2]:.2f} | {x_gpuTest[3]:.2f} | {x_gpuTest[4]:.2f} | {x_gpuTest[5]:.2f} | {x_gpuTest[6]:.2f} | {x_gpuTest[7]:.2f} | {x_gpuTest[8]:.2f} | {x_gpuTest[9]:.2f}")
                time.sleep(0.1)

            except ValueError as e:
                print(f"ValueError: {e}. Invalid value format.")

# Call the function to start printing values
writingvalue()
