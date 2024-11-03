import serial
import time
import threading
import matplotlib.pyplot as plt
import numpy as np
import cupy as cp  # GPU-accelerated numpy

ser = serial.Serial('COM17', 2000000, timeout=0.01)
time.sleep(2)

# Initialize lists for plotting data
temperature_data = []
pressure_data = []
altitude_data = []
time_data = []
stop_threads = False

# Create a figure for plotting
plt.ion()  # Interactive mode on for real-time updating
fig, ax = plt.subplots(3, 1, figsize=(10, 8))

# Function to update the plots
def update_plots():
    if len(time_data) > 0:  # Check if there's data to plot
        ax[0].cla()  # Clear the previous plot
        ax[1].cla()
        ax[2].cla()

        # Use cupy for GPU-based operations on the data
        time_data_gpu = cp.asarray(time_data)
        temperature_data_gpu = cp.asarray(temperature_data)
        pressure_data_gpu = cp.asarray(pressure_data)
        altitude_data_gpu = cp.asarray(altitude_data)

        # Plot Temperature
        ax[0].plot(cp.asnumpy(time_data_gpu), cp.asnumpy(temperature_data_gpu), color='r', label='Temperature (C)')
        ax[0].set_ylabel("Temperature (C)")
        ax[0].set_title("Real-time Temperature Data")
        ax[0].legend(loc="upper right")

        # Plot Pressure
        ax[1].plot(cp.asnumpy(time_data_gpu), cp.asnumpy(pressure_data_gpu), color='g', label='Pressure (Pa)')
        ax[1].set_ylabel("Pressure (Pa)")
        ax[1].set_title("Real-time Pressure Data")
        ax[1].legend(loc="upper right")

        # Plot Altitude
        ax[2].plot(cp.asnumpy(time_data_gpu), cp.asnumpy(altitude_data_gpu), color='b', label='Altitude (m)')
        ax[2].set_ylabel("Altitude (m)")
        ax[2].set_title("Real-time Altitude Data")
        ax[2].legend(loc="upper right")

        plt.xlabel("Time (s)")
        plt.tight_layout()
        plt.draw()  # Instead of pause(), use draw to keep it non-blocking

# Function to read serial data in a separate thread
def read_serial_data():
    start_time = time.time()
    while not stop_threads:
        if ser.in_waiting > 0:
            try:
                data = ser.readline().decode('utf-8').strip()
                data_values = data.split("\t")
                if len(data_values) >= 3:  # Check if the data is valid
                    temperature = float(data_values[0])
                    pressure = float(data_values[1])
                    altitude = float(data_values[2])

                    # Append new data points
                    current_time = time.time() - start_time
                    temperature_data.append(temperature)
                    pressure_data.append(pressure)
                    altitude_data.append(altitude)
                    time_data.append(current_time)

                    # Print the data (for logging purposes)
                    print(f"Temperature: {temperature}C | Pressure: {pressure}Pa | Altitude: {altitude}m")

            except (ValueError, IndexError) as e:
                print(f"Data format error: {e}")
    return temperature, pressure, altitude

# Start the thread for reading serial data
serial_thread = threading.Thread(target=read_serial_data)
serial_thread.start()

# Real-time plot update loop
try:
    while True:
        update_plots()  # Call the plot update function frequently
        plt.pause(0.01)  # Use a small pause for responsive GUI
finally:
    # Stop the thread when exiting
    stop_threads = True
    serial_thread.join()
    ser.close()
