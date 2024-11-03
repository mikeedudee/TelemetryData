import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import cupy as cp

start_Time = time.time()

# Initialize lists for storing time (y) and temperature (x_gpuTest[0])
time_vals = []
temp_vals = []

# Create a figure and axis object for live plotting
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlabel("Time Elapsed (s)")
ax.set_ylabel("Data")
ax.set_title("Live Telemetry Data")

# Read data from the serial port
def read_values_for_simulation():
    with open('cutdata.txt', 'r') as file:
        lines = file.readlines()  # Read all lines
        values = [line.strip().split() for line in lines]  # Split by tabs or spaces
    return values

# Function to update the plot for each frame
def writingvalue():
    global plotValue
    values = read_values_for_simulation()  # Read all rows at once
    
    for value in values:
        if value:
            try:
                # Convert necessary values to float for numerical computations
                groupNumber     = float(value[0])
                Temperature     = float(value[1])
                Pressure        = float(value[2])
                altitude        = float(value[3]) + 4  # Adjust altitude
                Longitude       = float(value[4]) / 1000000
                Latitude        = float(value[5]) / 1000000
                SDStatus        = float(value[6])
                GyroSensorX     = float(value[7])
                GyroSensorW     = float(value[8])
                GyroSensorY     = float(value[9])
                GyroSensorZ     = float(value[10])
                timeInMill      = (float(value[11]) / 1000)

                # Store values in an array
                x = [groupNumber, Temperature, Pressure, altitude, Longitude, Latitude, SDStatus, GyroSensorX, GyroSensorW, GyroSensorY, GyroSensorZ, timeInMill]
                x_gpuTest = cp.array(x)  # Transfer to GPU
            
                y_Value = time.time() - start_Time
                print(f"{x_gpuTest[0]:.2f} | {x_gpuTest[1]:.2f} | {x_gpuTest[2]:.2f} | {x_gpuTest[3]:.2f} | {x_gpuTest[4]} | {x_gpuTest[5]} | {x_gpuTest[6]} | {x_gpuTest[7]:.2f} | {x_gpuTest[8]:.2f} | {x_gpuTest[9]:.2f} | {x_gpuTest[10]:.2f} | {x_gpuTest[11]}")
                plotValue = [y_Value, x_gpuTest[3]] #Change this value to what shows

                # Append the values for plotting
                time_vals.append(plotValue[0])
                temp_vals.append(float(plotValue[1].get()))

                # Update the data in the plot
                line.set_data(time_vals, temp_vals)

                # Adjust the plot limits dynamically
                ax.set_xlim(max(0, time_vals[-1] - 100), time_vals[-1] + 0)  # Keep the last 100 seconds in view
                ax.set_ylim(min(temp_vals) - 10, max(temp_vals) + 10)  # Adjust based on the data range
                
            except ValueError as e:
                print(f"ValueError: {e}. Invalid data format.")

    return line,

# Create the animation object, interval set to 100ms
ani = animation.FuncAnimation(fig, writingvalue, interval=100)
#writingvalue()
plt.show()
