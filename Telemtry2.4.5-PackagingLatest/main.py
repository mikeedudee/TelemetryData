
import tkinter as tk
from ui import create_ui, create_buttons
from telemetry_simulation import telemetry_simulation, countdown_timer
import threading

def start_simulation():
    telemetry_data = telemetry_simulation()
    print("Telemetry data:", telemetry_data)

def start_countdown():
    countdown_timer()

def main():
    root = tk.Tk()

    fig, ax, canvas = create_ui(root)
    
    # Create start and stop buttons
    create_buttons(root, start_simulation, lambda: print("Stop pressed"))
    
    # Launch the GUI
    root.mainloop()

if __name__ == "__main__":
    main()
