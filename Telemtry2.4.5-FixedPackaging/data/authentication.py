from tkinter import Frame
import tkinter as tk
import customtkinter

def create_login_page():
        global frame, usernameGet, successLabel, buttonExit, nullLabel, nullLabel2, versionLabel, logoIAUPack, logoRnD, logoSYAE, logoSYAEPack, logoRnDPack, passwordGet, error_label, TelemetryLabel, copyrightLabel, buttonLogin, author_label, versionTeresa, logoIAU
        frame          = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True) #Entire Frame
        nullLabel      = customtkinter.CTkLabel(master=frame, text="")
        nullLabel2     = customtkinter.CTkLabel(master=frame, text="")
        TelemetryLabel = customtkinter.CTkLabel(master=frame, text="TELEMETRY", font=("Inter", 50))
        versionTeresa  = customtkinter.CTkLabel(master=frame, text="TeresaV Control Panel", font=("Inter", 12.5))
        usernameGet    = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
        passwordGet    = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
        buttonLogin    = customtkinter.CTkButton(master=frame, text="Login", corner_radius=10, border_color='gray', border_width=1, command=CredentialValidator.login)
        buttonExit     = customtkinter.CTkButton(master=frame, text="Exit",  corner_radius=10, border_color='gray', border_width=1, command=root.quit)
        error_label    = customtkinter.CTkLabel(master=frame, text="", font=("Inter", 12), text_color="red")
        successLabel   = customtkinter.CTkLabel(master=frame, text="", font=("Inter", 12), text_color="red")
        copyrightLabel = customtkinter.CTkLabel(master=frame, text="Copyright © 2024 — IAU Aerospace Engineering Research and Development Office", font=("Inter", 10))
        versionLabel   = customtkinter.CTkLabel(master=frame, text="version 2.4.5 — stable-beta (under development)", font=("Inter", 10))
        author_label   = customtkinter.CTkLabel(master=frame, text="Made by Francis Mike John D. Camogao", font=("Inter", 10))

        #IMAGES — icon
        logoIAU        = customtkinter.CTkImage(light_image=Image.open('C:/Users/Mikee/Desktop/Random Ass Files/Logos/IAU Logo.png'), size=(100,100))
        logoIAUPack    = customtkinter.CTkLabel(master=frame, text="", image=logoIAU)
        logoRnD        = customtkinter.CTkImage(light_image=Image.open('C:/Users/Mikee/Desktop/Random Ass Files/Logos/rndIcon.png'), size=(150,100))
        logoRnDPack    = customtkinter.CTkLabel(master=frame, text="", image=logoRnD)
        logoSYAE       = customtkinter.CTkImage(light_image=Image.open('C:/Users/Mikee/Desktop/Random Ass Files/Logos/syae.png'), size=(105,105))
        logoSYAEPack   = customtkinter.CTkLabel(master=frame, text="", image=logoSYAE)
        LoginFrame.login_page_packs(frame)

    # Packs for Login Page Widgets
def login_page_packs(frame): 
    nullLabel.grid(row=0, column=0, pady=0, padx=10, sticky='n')
    nullLabel2.grid(row=13, column=0, pady=0, padx=10, sticky='n')
    TelemetryLabel.grid(row=1, column=0, columnspan=5, pady=0, padx=10, sticky='n')
    versionTeresa.grid(row=2, column=0, columnspan=5, pady=0, padx=0, sticky='n')
    usernameGet.grid(row=3, column=0, columnspan=5, pady=12, padx=0, sticky='n')
    passwordGet.grid(row=4, column=0, columnspan=5, pady=10, padx=0, sticky='n')
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
    frame.grid_rowconfigure((0), weight=1)