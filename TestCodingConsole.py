class InputBehaviorContainers:
    # Creating a Data File Container if not exists
    @staticmethod
    def save_value_to_file(value):
        with open('dataBehavior.txt', 'w') as file:
            file.write(str(value))

    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert(tk.END, text)
        self.widget.see(tk.END)  # Auto-scroll to the bottom

    @staticmethod
    def run_script():
        # Run the script in a separate thread to avoid blocking the GUI
        thread = threading.Thread(target=InputBehaviorContainers.run_subprocess)
        thread.start()

    @staticmethod
    def run_subprocess():
        # Run your script or command
        script_path = "consoleDictionary.py"  # Replace with your script path

        # Start the process and continuously read the output
        process = subprocess.Popen(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1, universal_newlines=True)

        # Redirect stdout and stderr to the console widget
        sys.stdout = InputBehaviorContainers(console_text)
        sys.stderr = InputBehaviorContainers(console_text)

        # Loop through the process output and display it in real-time
        while True:
            output = process.stdout.readline()  # Read output line by line
            if output == '' and process.poll() is not None:  # Check if the process is done
                break
            if output:
                print(output.strip())  # Print the output in the console

        # Capture errors if any
        errors = process.stderr.read()
        if errors:
            print(errors.strip())

        # Restore stdout and stderr after the script completes
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__