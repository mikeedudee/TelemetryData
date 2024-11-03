
import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def create_ui(root):
    """Sets up the main application UI"""
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    
    root.title("Telemetry UI")
    root.geometry("800x600")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    # Create a matplotlib figure
    fig, ax = plt.subplots()
    ax.set_title("Telemetry Data")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Altitude (m)")

    # Place the figure in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    return fig, ax, canvas

def create_buttons(frame, start_callback, stop_callback):
    """Creates start and stop buttons on the UI"""
    
    start_button = customtkinter.CTkButton(master=frame, text="Start", command=start_callback)
    start_button.pack(pady=10, padx=10, side=tk.LEFT)
    
    stop_button = customtkinter.CTkButton(master=frame, text="Stop", command=stop_callback)
    stop_button.pack(pady=10, padx=10, side=tk.LEFT)
