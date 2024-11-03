import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import cupy as cp

start_Time = time.time()
ser = serial.Serial('COM17', 9600, timeout=0.01)

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
def read_data():
    if ser.in_waiting > 0:
        try:
            data = ser.readline().decode('utf-8').strip()
            data_values = data.split("\t")
            return data_values
        except Exception as e:
            print(f"Error reading data: {e}")
            return None

# Function to update the plot for each frame
def update(frame):
    global plotValue
    
    data = read_data()
    if data:
        try:
            # Convert necessary values to float for numerical computations
            temperature     = float(data[0])
            pressure        = float(data[1])
            airDensity      = pressure / (287 * temperature)
            altitude        = float(data[2]) + 8  # Assume altitude is a float
            GyroSensorYaw   = float(data[12])  # Assuming Gyro sensor data is numerical
            GyroSensorPitch = float(data[13])
            GyroSensorRoll  = float(data[14])

            # Use only numeric values for GPU processing
            x = [temperature, pressure, airDensity, altitude, GyroSensorYaw, GyroSensorPitch, GyroSensorRoll]
            x_gpuTest = cp.array(x)
            
            y_Value = time.time() - start_Time
            print(f"{x_gpuTest[0]:.2f} | {x_gpuTest[1]:.2f} | {x_gpuTest[2]:.2f} | {x_gpuTest[3]:.2f} | {x_gpuTest[4]:.2f} | {x_gpuTest[5]:.2f} | {x_gpuTest[6]:.2f} | {y_Value:.2f}")
            plotValue = [y_Value, x_gpuTest[2]]

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
ani = animation.FuncAnimation(fig, update, interval=0)

plt.show()
