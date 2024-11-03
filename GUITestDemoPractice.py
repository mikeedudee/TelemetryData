import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("IAU Research and Development")

USERNAME = "admin"
PASSWORD = "iaurndae69"

def login():
    entered_username = entry1.get()
    entered_password = entry2.get()
    
    if entered_username == USERNAME and entered_password == PASSWORD:
        print("Login successful!")
        show_main_page()
    else:
        error_label.configure(text="Invalid username or password.")

def show_main_page():
    frame.destroy()
    
    main_frame = customtkinter.CTkFrame(master=root)
    main_frame.pack(pady=20, padx=60, fill="both", expand=True)
    
    label = customtkinter.CTkLabel(master=main_frame, text="Welcome to the Main Operation Page", font=("Roboto", 24))
    label.pack(pady=20, padx=10)
    
    operation_label = customtkinter.CTkLabel(master=main_frame, text="Main Operations", font=("Roboto", 18))
    operation_label.pack(pady=12, padx=10)

    logout_button = customtkinter.CTkButton(master=main_frame, text="Logout", command=return_to_login)
    logout_button.pack(pady=12, padx=10)

    exit_button = customtkinter.CTkButton(master=main_frame, text="Exit/Shutdown", command=root.quit)
    exit_button.pack(pady=12, padx=10)

def return_to_login():
    for widget in root.winfo_children():
        widget.destroy()

    create_login_page()

def create_login_page():
    global frame, entry1, entry2, error_label
    
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="TELEMETRY", font=("Roboto", 24))
    label.pack(pady=20, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    entry2.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Login", command=login)
    button.pack(pady=12, padx=10)

    error_label = customtkinter.CTkLabel(master=frame, text="", font=("Roboto", 12), text_color="red")
    error_label.pack(pady=10)

    label = customtkinter.CTkLabel(master=frame, text="Copyright 2024 — IAU Research and Development Office", font=("Roboto", 10))
    label.pack(pady=(20, 0), padx=10)

    author_label = customtkinter.CTkLabel(master=frame, text="Made by Francis Mike John Camogao", font=("Roboto", 10))
    author_label.pack(pady=(0, 20), padx=10)

create_login_page()

root.mainloop()
