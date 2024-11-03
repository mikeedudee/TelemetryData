import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import cupy as cp

start_Time = time.time()
ser = serial.Serial('COM17', 9600, timeout=0.01)

# Parameters
x_len = 200         # Number of points to display
y_range = [40, 110]  # Range of possible Y values to display

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 200))
ys = [0] * x_len
ax.set_ylim(y_range)

# Create a blank line. We will update the line in animate
line, = ax.plot(xs, ys)

# Add labels
plt.title('LIVE TELEMTRY DATA')
plt.xlabel('Time (s)')
plt.ylabel('Data')

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

# This function is called periodically from FuncAnimation
def animate(i, ys):

    # Read temperature (Celsius) from TMP102
    '''temp_c = round(tmp102.read_temp(), 2)
    temp_f=(temp_c*9/5)+32'''
    
    data = read_data()
    if data:
        
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
            #print(f"{x_gpuTest[0]:.2f} | {x_gpuTest[1]:.2f} | {x_gpuTest[2]:.2f} | {x_gpuTest[3]:.2f} | {x_gpuTest[4]:.2f} | {x_gpuTest[5]:.2f} | {x_gpuTest[6]:.2f} | {y_Value:.2f}")
            
             # Add y to list
            ys.append(temperature)

            # Limit y list to set number of items
            ys = ys[-x_len:]

            # Update line with new Y values
            line.set_ydata(ys)
            
    ''' except ValueError as e:
            print(f"ValueError: {e}. Invalid data format.")'''
    return line,


# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys,),
    interval=1,
    blit=True)
plt.show()