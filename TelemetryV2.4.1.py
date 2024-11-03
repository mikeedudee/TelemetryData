import customtkinter
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Frame
import numpy as np
import random
import time
from PIL import Image
import pywinstyles

# Constants FOR SIMULATION
APOGEE = 10000
DURATION = 65
UPDATE_INTERVAL = 0.1
WINDOW_SIZE = 30 * 60
COUNTDOWN_TIME = 15 # Countdown time in seconds

# Create the main application window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#def CenterWindowToDisplay(Screen: customtkinter, width: int, height: int, scale_factor: float = 1.0):
#    """Centers the window to the main display/monitor"""
#    screen_width = Screen.winfo_screenwidth()
#    screen_height = Screen.winfo_screenheight()
#    x = int(((screen_width/2) - (width/2.47)) * scale_factor)
#    y = int(((screen_height/2) - (height/2.47)) * scale_factor)
#    return f"{width}x{height}+{x}+{y}"

root = customtkinter.CTk()

# will launch a 900x400 window in the center of the main screen.
#root.geometry(CenterWindowToDisplay(root, 1920, 1080, root._get_window_scaling()))
root.geometry("1080x720")
root.title("TeresaV Control Panel")
root.iconbitmap('C:/Users/Mikee/Desktop/Random Ass Files/Logos/rndIcon.ico')

class GenerationOfSimulationData:
# Function to generate sample data (FOR SIMULATION ONLY)
    def generate_sample_data(t):
        global altitude
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

# Create a login page
def create_login_page():
    global frame, usernameGet, successLabel, buttonExit, nullLabel, nullLabel2, versionLabel, logoIAUPack, logoRnD, logoSYAE, logoSYAEPack, logoRnDPack, passwordGet, error_label, TelemetryLabel, copyrightLabel, buttonLogin, author_label, versionTeresa, logoIAU
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True) #Entire Frame
    nullLabel = customtkinter.CTkLabel(master=frame, text="")
    nullLabel2 = customtkinter.CTkLabel(master=frame, text="")
    TelemetryLabel = customtkinter.CTkLabel(master=frame, text="TELEMETRY", font=("Inter", 50))
    versionTeresa = customtkinter.CTkLabel(master=frame, text="TeresaV Control Panel", font=("Inter", 12.5))
    usernameGet = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    passwordGet = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    buttonLogin = customtkinter.CTkButton(master=frame, text="Login", corner_radius=10, border_color='gray', border_width=1, command=login)
    buttonExit = customtkinter.CTkButton(master=frame, text="Exit",  corner_radius=10, border_color='gray', border_width=1, command=root.quit)
    error_label = customtkinter.CTkLabel(master=frame, text="", font=("Inter", 12), text_color="red")
    successLabel = customtkinter.CTkLabel(master=frame, text="", font=("Inter", 12), text_color="red")
    copyrightLabel = customtkinter.CTkLabel(master=frame, text="Copyright © 2024 — IAU Aerospace Engineering Research and Development Office", font=("Inter", 10))
    versionLabel = customtkinter.CTkLabel(master=frame, text="version 2.4.1 — unstable-beta (under development)", font=("Inter", 10))
    author_label = customtkinter.CTkLabel(master=frame, text="Made by Francis Mike John D. Camogao", font=("Inter", 10))

    #IMAGES — icon
    logoIAU = customtkinter.CTkImage(light_image=Image.open('C:/Users/Mikee/Desktop/Random Ass Files/Logos/IAU Logo.png'), size=(100,100))
    logoIAUPack = customtkinter.CTkLabel(master=frame, text="", image=logoIAU)
    logoRnD = customtkinter.CTkImage(light_image=Image.open('C:/Users/Mikee/Desktop/Random Ass Files/Logos/rndIcon.png'), size=(150,100))
    logoRnDPack = customtkinter.CTkLabel(master=frame, text="", image=logoRnD)
    logoSYAE = customtkinter.CTkImage(light_image=Image.open('C:/Users/Mikee/Desktop/Random Ass Files/Logos/syae.png'), size=(105,105))
    logoSYAEPack = customtkinter.CTkLabel(master=frame, text="", image=logoSYAE)
    login_page_packs(frame)

# Packs for Login Page Widgets
def login_page_packs(frame): 
    nullLabel.grid(row=0, column=0, pady=0, padx=10, sticky='n')
    nullLabel2.grid(row=13, column=0, pady=0, padx=10, sticky='n')
    TelemetryLabel.grid(row=1, column=0, columnspan=5, pady=0, padx=10, sticky='n')
    versionTeresa.grid(row=2, column=0, columnspan=5, pady=0, padx=0, sticky='n')
    usernameGet.grid(row=3, column=0, columnspan=5, pady=12, padx=0, sticky='n')
    passwordGet.grid(row=4, column=0, columnspan=5, pady=12, padx=0, sticky='n')
    buttonLogin.grid(row=5, column=0, columnspan=5, pady=12, padx=0, sticky='n')
    buttonExit.grid(row=6, column=0, columnspan=5, pady=0, padx=0, sticky='n')
    error_label.grid(row=7, column=0, columnspan=5, pady=10, padx=0, sticky='n')
    successLabel.grid(row=8, column=0, columnspan=5, pady=12, padx=0, sticky='n')
    copyrightLabel.grid(row=9, column=0, columnspan=5, pady=0, padx=0, sticky='n')
    author_label.grid(row=10, column=0, columnspan=5, pady=0, padx=0, sticky='n')
    versionLabel.grid(row=11, column=0, columnspan=5, pady=0, padx=10, sticky='n')

    #IMAGES — ICON
    logoIAUPack.grid(row=12, column=1, pady=0, padx=10, sticky='se')
    logoRnDPack.grid(row=12, column=2, pady=0, padx=10, sticky='se')
    logoSYAEPack.grid(row=12, column=3, pady=0, padx=10, sticky='sw')

    #Widgets Opacity
    pywinstyles.set_opacity(logoIAUPack, value=0.8)
    pywinstyles.set_opacity(logoRnDPack, value=0.8)
    pywinstyles.set_opacity(logoSYAEPack, value=0.8)

    frame.grid_columnconfigure((0, 3), weight=1)
    frame.grid_rowconfigure((0,13), weight=1)

def show_main_page():
    frame.destroy()

    
    # Create frame for Matplotlib plots and countdown timer
    plot_frame = customtkinter.CTkFrame(master=root, fg_color='gray19')
    plot_frame.pack(fill='both', expand=True, padx=20, pady=20,)

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
    global time_data
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

    # Update function for animation
    def update(frame):
        global time_data, countdown_complete, elapsed_time
        if not countdown_complete:  # Only update if countdown is complete
            return lines
        
        current_time = time.time() - start_time
        elapsed_time = current_time % DURATION
        elapsed_time_int = round(elapsed_time)
        print(elapsed_time_int)
    
        # FLIGHT SEQUENCE SIMULATION LOGS
        global all_systems_go, ejectionCharged_label, ejectionChargedFired_label, drougeChute_deployed_label, mainChute_deployed_label
        if elapsed_time_int >= 25:
            all_systems_go.destroy()
            ejectionCharged_label = customtkinter.CTkLabel(master=button_frame, text="Arming Ejection Charge.", text_color="green", font=("Inter", 11))
            ejectionCharged_label.grid(row=1, column=0, columnspan=5, pady=0, padx=10, sticky='ne')
        elif elapsed_time_int >= 33:
            ejectionCharged_label.destroy()
            ejectionChargedFired_label = customtkinter.CTkLabel(master=button_frame, text="Ejection Charge Fired — Ejected.", text_color="green", font=("Inter", 11))
            ejectionChargedFired_label.grid(row=1, column=0, columnspan=5, pady=0, padx=10, sticky='ne')
        elif elapsed_time_int >= 35:
            ejectionChargedFired_label.destroy()
            drougeChute_deployed_label = customtkinter.CTkLabel(master=button_frame, text="Drogue Chute Deployed.", text_color="green", font=("Inter", 11))
            drougeChute_deployed_label.grid(row=1, column=0, columnspan=5, pady=0, padx=10, sticky='ne')
        elif elapsed_time_int >= 40:
            drougeChute_deployed_label.destroy()
            mainChute_deployed_label = customtkinter.CTkLabel(master=button_frame, text="Main Chute Deployed.", text_color="green", font=("Inter", 11))
            mainChute_deployed_label.grid(row=1, column=0, columnspan=5, pady=0, padx=10, sticky='ne')
            

        telemetry_data = GenerationOfSimulationData.generate_sample_data(elapsed_time)  # Generate sample data

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
    canvas.get_tk_widget().pack(fill='both', expand=True,)

    # Create a separate frame for the buttons
    global button_frame 
    button_frame = customtkinter.CTkFrame(master=root, fg_color='gray10')
    button_frame.pack(side='bottom', pady=20, fill='x')

    global countdown_label, logout_button, exit_button, start_countdown_button, manualEject_button, runSystemCheck_button
    countdown_label = customtkinter.CTkLabel(master=button_frame, text=f"00:{COUNTDOWN_TIME}:00", font=("Inter", 20),  text_color='white')
    start_countdown_button = customtkinter.CTkButton(master=button_frame, text="Start Countdown", command=start_countdown)
    logout_button = customtkinter.CTkButton(master=button_frame, text="Logout", command=lambda: return_to_login())
    exit_button = customtkinter.CTkButton(master=button_frame, text="Shutdown", command=root.quit)
    manualEject_button = customtkinter.CTkButton(master=button_frame, text="Manual Eject")
    runSystemCheck_button = customtkinter.CTkButton(master=button_frame, text="Run System Check")
    
    main_page_button_grid(button_frame)  # Pass the button frame to the function

    

def main_page_button_grid(button_frame):
    countdown_label.grid(row=0, column=0, columnspan=5, pady=0, padx=10, sticky='n')  # Label of the countdown

    # Align Shutdown and Manual Eject next to each other
    exit_button.grid(row=2, column=0, padx=10, pady=10, sticky='w')                        # Shutdown button
    manualEject_button.grid(row=2, column=1, padx=(0, 10), pady=10, sticky='w')            # Manual Eject button
    start_countdown_button.grid(row=2, column=0,  columnspan=5, pady=10, sticky='n')       # Start countdown button
    button_frame.grid_columnconfigure((1, 2), weight=1)

    # Align Logout and Run System Check next to each other
    logout_button.grid(row=3, column=0, padx=10, pady=10, sticky='w')               # Logout button
    runSystemCheck_button.grid(row=3, column=1, padx=(0, 19), pady=10, sticky='w')  # Run System Check button


# Handle login validation
def USERNAME():
    return {
        'jeremy': 101,
        'kokoks': 102,
        'beltraniga': 103,
        'admin': 104
    }
def PASSWORD():
    return {
        'jeremy123': 'jeremy',
        'kokoks123': 'kokoks',
        'beltran123': 'beltraniga',
        'admin': 'admin' 
    }

# Handle login validation
def login() -> None:
    entered_username = usernameGet.get()
    entered_password = passwordGet.get()

    #userID = USERNAME()
    userPWD = PASSWORD()

    if entered_password in userPWD:
        #error_label.configure(text="Verified credential.") 
        if userPWD[entered_password] == entered_username:
            show_main_page()
        else:
            error_label.configure(text="Unrecognized credential.") 
    else:
        error_label.configure(text="Unrecognized credential.") 

countdown_complete = False

# Update the countdown timer
# Global variable to store the reference to the scheduled after call
countdown_after_id = None

def update_countdown():
    global countdown_label, label_prep, countdown_time_remaining, countdown_complete, starting_system_check_label, all_systems_go, label_system_check, countdown_after_id
    
    if countdown_time_remaining > 1:
        countdown_time_remaining -= 1
        countdown_label.configure(text=f"00:{countdown_time_remaining}:00", font=("Inter", 20),  text_color='white')
        countdown_after_id = root.after(1000, update_countdown)  
        
        # System check messages and logic
        if countdown_time_remaining <= 5:
            countdown_complete = True
            label_prep.destroy()
            all_systems_go = customtkinter.CTkLabel(master=button_frame, text="GO FOR FLIGHT — Internal System Initialized", text_color="green", font=("Inter", 11))
            all_systems_go.grid(row=0, column=0, columnspan=5, pady=0, padx=10, sticky='ne')
        elif countdown_time_remaining == 10:
            starting_system_check_label.destroy()
            label_system_check = customtkinter.CTkLabel(master=button_frame, text="SYSTEM CHECK FINISHED", text_color="green", font=("Inter", 11))
            label_system_check.grid(row=0, column=0, columnspan=5, pady=0, padx=10, sticky='ne')
        elif countdown_time_remaining <= 8:
            label_system_check.destroy()
            label_prep = customtkinter.CTkLabel(master=button_frame, text="PREPARING INTERNAL SYSTEM", text_color="green", font=("Inter", 11))
            label_prep.grid(row=0, column=0, columnspan=5, pady=0, padx=10, sticky='ne')

    else:
        countdown_label.configure(text="IGNITION!", text_color='green', font=("Inter", 20))

def start_countdown():
    global countdown_time_remaining, countdown_complete
    start_countdown_button.destroy()
    countdown_complete = False  # Reset the countdown complete flag
    countdown_time_remaining = COUNTDOWN_TIME
    update_countdown()
    checkingSystem()
    stop_countdown_button = customtkinter.CTkButton(master=button_frame, text="Stop Countdown", command=stop_countdown)
    stop_countdown_button.grid(row=2, column=0,  columnspan=5, pady=10, sticky='n')

def stop_countdown():
    global countdown_complete, countdown_after_id, start_countdown_button, label_system_check, starting_system_check_label
    countdown_complete = False
    # Cancel the after loop by referencing the ID
    if countdown_after_id:
        root.after_cancel(countdown_after_id)
        countdown_after_id = None
    
    countdown_label.configure(text="00:00:00", text_color='white')
    starting_system_check_label.destroy()
    label_system_check.destroy()
    countdownStopped_Label = customtkinter.CTkLabel(master=button_frame, text="COUNTDOWN HALTED", text_color="yellow2", font=("Inter", 11))
    countdownStopped_Label.grid(row=0, column=0, columnspan=5, pady=0, padx=10, sticky='ne')
    start_countdown_button = customtkinter.CTkButton(master=button_frame, text="Start Countdown", command=start_countdown)
    main_page_button_grid(button_frame)

def checkingSystem():
        global starting_system_check_label
        starting_system_check_label = customtkinter.CTkLabel(master=button_frame, text="STARTING SYSTEM CHECK", text_color="green", font=("Inter", 11))
        starting_system_check_label.grid(row=0, column=0, columnspan=5, pady=0, padx=10, sticky='ne')

# Handle logout and return to login page
def return_to_login():
    for widget in root.winfo_children():
        widget.destroy()
    #plot_frame.destroy()  # Clear the plot frame
    frame.destroy()
    create_login_page()

#show_main_page()
create_login_page()
root.mainloop()