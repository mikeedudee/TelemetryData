import customtkinter
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Frame
import numpy as np
import random
import time

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Simulation parameters
APOGEE = 10000
DURATION = 60
UPDATE_INTERVAL = 0.1
WINDOW_SIZE = 30 * 60

# Generation of Data for Simulation
def generate_sample_data(t):
    altitude = APOGEE * (1 - np.cos(np.pi * t / (DURATION / 2))) / 2
    velocity = (APOGEE / (DURATION / 2)) * np.sin(np.pi * t / (DURATION / 2))
    acceleration = (APOGEE / (DURATION / 2)) * (np.pi / (DURATION / 2)) * np.cos(np.pi * t / (DURATION / 2))
    attitude = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360))
    vibration = random.uniform(0, 5)
    temperature = random.uniform(-20, 40)
    pressure = 1013 * np.exp(-0.00012 * altitude)
    air_density = 1.225 * np.exp(-0.00012 * altitude)
    
    return {
        "altitude": altitude,
        "velocity": velocity,
        "acceleration": acceleration,
        "attitude": attitude,
        "vibration": vibration,
        "temperature": temperature,
        "pressure": pressure,
        "air_density": air_density
    }

# Initialize the main window
root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("IAU RnD Telemetry - Main Operations")

# Frame for Matplotlib plots
plot_frame = Frame(root)
plot_frame.pack(fill='both', expand=True, padx=20, pady=20)

# Create figure for plots
fig, axes = plt.subplots(4, 2, figsize=(12, 8))
fig.tight_layout(pad=3.0)

# Initialize plots with empty data
lines = []
for ax in axes.flat:
    line, = ax.plot([], [], lw=2)
    lines.append(line)

# Titles for each plot
plot_titles = [
    "Altitude (m)", "Velocity (m/s)", "Acceleration (m/s²)", "Attitude (Pitch)",
    "Vibration (g)", "Temperature (°C)", "Pressure (hPa)", "Air Density (kg/m³)"
]

# Set up plot parameters
for i, ax in enumerate(axes.flat):
    ax.set_title(plot_titles[i])
    ax.set_xlim(0, WINDOW_SIZE)  # Set x-axis limit for 30 minutes
    ax.set_ylim(0, 15000 if i == 0 else 1100)  # Adjust for high altitude and pressure
    ax.grid(True)

# Data placeholders
max_len = 3000  # Enough to cover 30 minutes of data
time_data = np.linspace(0, WINDOW_SIZE, max_len)
data_buffers = {
    "altitude": np.zeros(max_len),
    "velocity": np.zeros(max_len),
    "acceleration": np.zeros(max_len),
    "attitude_pitch": np.zeros(max_len),
    "attitude_yaw": np.zeros(max_len),
    "attitude_roll": np.zeros(max_len),
    "vibration": np.zeros(max_len),
    "temperature": np.zeros(max_len),
    "pressure": np.zeros(max_len),
    "air_density": np.zeros(max_len)
}

start_time = time.time()

def update(frame):
    global time_data
    current_time = time.time() - start_time
    elapsed_time = current_time % DURATION
    telemetry_data = generate_sample_data(elapsed_time)  # Generate sample data

    # Shift old data and add new data
    for key in data_buffers:
        data_buffers[key] = np.roll(data_buffers[key], -1)
    
    data_buffers["altitude"][-1] = telemetry_data["altitude"]
    data_buffers["velocity"][-1] = telemetry_data["velocity"]
    data_buffers["acceleration"][-1] = telemetry_data["acceleration"]
    data_buffers["attitude_pitch"][-1] = telemetry_data["attitude"][0]
    data_buffers["attitude_yaw"][-1] = telemetry_data["attitude"][1]
    data_buffers["attitude_roll"][-1] = telemetry_data["attitude"][2]
    data_buffers["vibration"][-1] = telemetry_data["vibration"]
    data_buffers["temperature"][-1] = telemetry_data["temperature"]
    data_buffers["pressure"][-1] = telemetry_data["pressure"]
    data_buffers["air_density"][-1] = telemetry_data["air_density"]

    time_data = np.roll(time_data, -1)
    time_data[-1] = elapsed_time


    lines[0].set_data(time_data, data_buffers["altitude"])
    lines[1].set_data(time_data, data_buffers["velocity"])
    lines[2].set_data(time_data, data_buffers["acceleration"])
    lines[3].set_data(time_data, data_buffers["attitude_pitch"])  # Only showing pitch for simplicity
    lines[4].set_data(time_data, data_buffers["vibration"])
    lines[5].set_data(time_data, data_buffers["temperature"])
    lines[6].set_data(time_data, data_buffers["pressure"])
    lines[7].set_data(time_data, data_buffers["air_density"])

    # Adjust x and y limits
    for i, ax in enumerate(axes.flat):
        ax.relim()
        ax.autoscale_view()
        
        # Dynamically adjust the x-axis limits to always show the latest 30 minutes
        ax.set_xlim(max(0, elapsed_time - WINDOW_SIZE), elapsed_time)
        ax.set_ylim(0, max(np.max(data_buffers[list(data_buffers.keys())[i]]), 15000 if i == 0 else 1100))

    return lines

# Setup animation
ani = FuncAnimation(fig, update, blit=False, interval=UPDATE_INTERVAL * 1000, cache_frame_data=False)

# Embed the plot into Tkinter
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill='both', expand=True)

# Buttons for Logout and Exit/Shutdown
logout_button = customtkinter.CTkButton(master=root, text="Logout", command=lambda: return_to_login(plot_frame))
logout_button.pack(pady=12, padx=10, side='left')

exit_button = customtkinter.CTkButton(master=root, text="Exit/Shutdown", command=root.quit)
exit_button.pack(pady=12, padx=10, side='right')

# Function to handle logout and return to login page
def return_to_login(plot_frame):
    plot_frame.destroy()  # Clear the plot frame
    # Add code to return to the login page

root.mainloop()
