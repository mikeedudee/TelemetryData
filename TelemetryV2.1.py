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
DURATION = 60
UPDATE_INTERVAL = 0.1
#WINDOW_SIZE = 30 * 60
COUNTDOWN_TIME = 15 # Countdown time in seconds

# Create the main application window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def CenterWindowToDisplay(Screen: customtkinter, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2.47)) * scale_factor)
    y = int(((screen_height/2) - (height/2.47)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

root = customtkinter.CTk()

# will launch a 900x400 window in the center of the main screen.
root.geometry(CenterWindowToDisplay(root, 1920, 1080, root._get_window_scaling()))
root.title("TeresaV Control Panel")
root.iconbitmap('C:/Users/Mikee/Desktop/Random Ass Files/Logos/rndIcon.ico')


# Function to generate sample data (FOR SIMULATION ONLY)
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

# Create a login page
def create_login_page():
    global frame, usernameGet, buttonExit, versionLabel, logoIAUPack, logoRnD, logoSYAE, logoSYAEPack, logoRnDPack, passwordGet, error_label, TelemetryLabel, copyrightLabel, buttonLogin, author_label, versionTeresa, logoIAU
    frame = customtkinter.CTkFrame(master=root)
    TelemetryLabel = customtkinter.CTkLabel(master=frame, text="TELEMETRY", font=("Inter", 40))
    versionTeresa = customtkinter.CTkLabel(master=frame, text="TeresaV Control Panel", font=("Inter", 12.5))
    usernameGet = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    passwordGet = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    buttonLogin = customtkinter.CTkButton(master=frame, text="Login", command=login)
    buttonExit = customtkinter.CTkButton(master=frame, text="Exit", command=root.quit)
    error_label = customtkinter.CTkLabel(master=frame, text="", font=("Inter", 12), text_color="red")
    copyrightLabel = customtkinter.CTkLabel(master=frame, text="Copyright © 2024 — IAU Aerospace Engineering Research and Development Office", font=("Inter", 10))
    versionLabel = customtkinter.CTkLabel(master=frame, text="version 2.1 — stable-beta", font=("Inter", 10))
    author_label = customtkinter.CTkLabel(master=frame, text="Made by Francis Mike John Camogao", font=("Inter", 10))
    logoIAU = customtkinter.CTkImage(light_image=Image.open('C:/Users/Mikee/Desktop/Random Ass Files/Logos/IAU Logo.png'), size=(100,100))
    logoIAUPack = customtkinter.CTkLabel(master=frame, text="", image=logoIAU)
    logoRnD = customtkinter.CTkImage(light_image=Image.open('C:/Users/Mikee/Desktop/Random Ass Files/Logos/rndIcon.png'), size=(150,100))
    logoRnDPack = customtkinter.CTkLabel(master=frame, text="", image=logoRnD)
    logoSYAE = customtkinter.CTkImage(light_image=Image.open('C:/Users/Mikee/Desktop/Random Ass Files/Logos/syae.png'), size=(105,105))
    logoSYAEPack = customtkinter.CTkLabel(master=frame, text="", image=logoSYAE)
    login_page_packs()

# Packs for Login Page Widgets
def login_page_packs(): 
    frame.pack(pady=20, padx=60, fill="both", expand=True) #Entire Frame
    TelemetryLabel.pack(pady=(170, 0))
    versionTeresa.pack(pady=0)
    usernameGet.pack(pady=12)
    passwordGet.pack(pady=12)
    buttonLogin.pack(pady=12)
    buttonExit.pack(pady=0)
    error_label.pack(pady=10)
    copyrightLabel.pack()
    author_label.pack()
    versionLabel.pack(anchor='s', pady=0, padx=10, side="right")
    logoIAUPack.pack(anchor='s', pady=10, padx=10, side="left")
    logoRnDPack.pack(anchor='s', pady=10, padx=10, side="left")
    logoSYAEPack.pack(anchor='s', pady=10, padx=10, side="left")
    pywinstyles.set_opacity(logoIAUPack, value=0.8)
    pywinstyles.set_opacity(logoRnDPack, value=0.8)
    pywinstyles.set_opacity(logoSYAEPack, value=0.8)

def show_main_page():
    frame.destroy()
    global countdown_label, logout_button, exit_button, start_countdown_button
    countdown_label = customtkinter.CTkLabel(master=root, text=f"Countdown: {COUNTDOWN_TIME} seconds", font=("Inter", 16))
    start_countdown_button = customtkinter.CTkButton(master=root, text="Start Countdown", command=start_countdown)
    logout_button = customtkinter.CTkButton(master=root, text="Logout", command=lambda: return_to_login())
    exit_button = customtkinter.CTkButton(master=root, text="Shutdown", command=root.quit)
    main_page_button_packs()

def main_page_button_packs():
    countdown_label.pack(pady=5)
    start_countdown_button.pack(pady=1)
    logout_button.pack(pady=0, padx=10, side='left')
    exit_button.pack(pady=0, padx=10, side='left')

# Handle login validation
def USERNAME() -> list:
    return [
        "admin",
        "jeremy",
        "francis",
        "kokoks"
    ]
def PASSWORD() -> list:
    return [
        "admin",
        "123"
    ]

# Handle login validation
def login() -> None:
    entered_username = usernameGet.get()
    entered_password = passwordGet.get()

    if entered_username in USERNAME() and entered_password in PASSWORD():
        #print("Login successful!")
        show_main_page()
    else:
        error_label.configure(text="Unrecognized credential.")

countdown_complete = False

# Update the countdown timer
def update_countdown():
    global countdown_label, countdown_time_remaining, countdown_complete, consoleLog
    
    if countdown_time_remaining > 0:
        countdown_time_remaining -= 1
        countdown_label.configure(text=f"Countdown: {countdown_time_remaining} seconds")
        root.after(1000, update_countdown)  # Schedule the update every second
        if countdown_time_remaining  == 5:
            countdown_complete = True
        elif countdown_time_remaining == 10:
            label_system_check = customtkinter.CTkLabel(master=root, text="SYSTEM CHECK FINISHED", text_color="green", font=("Inter", 11))
            label_system_check.pack(pady=0, padx=5, side='right') 
    else:
        countdown_label.configure(text="IGNITION!")

def start_countdown():
        global countdown_time_remaining, countdown_complete
        countdown_complete = False  # Reset the countdown complete flag
        countdown_time_remaining = COUNTDOWN_TIME
        update_countdown()

def checkingSystem():
        consoleLog = customtkinter.CTkLabel(master=root, text="STARTING SYSTEM CHECK", text_color="green", font=("Inter", 11))
        consoleLog.pack(pady=0, padx=5, side='right') 

# Handle logout and return to login page
def return_to_login():
    for widget in root.winfo_children():
        widget.destroy()
    #plot_frame.destroy()  # Clear the plot frame
    frame.destroy()
    create_login_page()

create_login_page()
root.mainloop()