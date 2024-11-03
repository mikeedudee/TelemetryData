import serial
import time
import matplotlib.pyplot as plt
import numpy as np
import cupy as cp

ser = serial.Serial('COM17', 9600, timeout=0.01) 
time.sleep(2)

def read_data():
    if ser.in_waiting > 0:
        try:
            data = ser.readline().decode('utf-8').strip() 
            data_values = data.split("\t") 
            return data_values
        except Exception as e:
            print(f"Error reading data: {e}")
            return None

while True:
    data = read_data()
    if data:
        try:
            # Convert necessary values to float for numerical computations
            temperature     = float(data[0])
            pressure        = float(data[1])
            airDensity      = pressure / (287 * temperature)
            altitude        = float(data[2]) + 4  # Assume altitude is a float
            Latitude        = float(data[3])  # Assuming Latitude is a float
            Longitude       = float(data[4])  # Assuming Longitude is a float
            Month           = data[5]  # Keeping Month, Day, Year as strings
            Day             = data[6]
            Year            = data[7]
            Hour            = data[8]
            MinHand         = data[9]
            SecHand         = data[10]
            GyroSensorYaw   = float(data[12])  # Assuming Gyro sensor data is numerical
            GyroSensorPitch = float(data[13])
            GyroSensorRoll  = float(data[14])

            # Use only numeric values for GPU processing
            x = [temperature, pressure, airDensity, altitude, GyroSensorYaw, GyroSensorPitch, GyroSensorRoll]
            x_gpuTest = cp.array(x)

            # Print individual values of the GPU array
            #print("GPU Array:", x_gpuTest)
            # FORMAT: Temperature | Pressure | AirDensity | Altitude
            print(f"{x_gpuTest[0]:.2f} | {x_gpuTest[1]:.2f} | {x_gpuTest[2]:.2f} | {x_gpuTest[3]:.2f} | {x_gpuTest[4]:.2f} | {x_gpuTest[5]:.2f} | {x_gpuTest[6]:.2f}")
        
        except ValueError as e:
            print(f"ValueError: {e}. Invalid data format.")
