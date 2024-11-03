# Demo.py
import ReadAndWriteOutput
# Initialize the consoleValueID with a default value
consoleValueID = 101

def save_value_to_file(value):
    with open('data.txt', 'w') as file:
        file.write(str(value))

def main():
    global consoleValueID
    while True:
        try:
            # Take user input and update consoleValueID
            consoleValueID = int(input("Enter new consoleValueID value: "))
            save_value_to_file(consoleValueID)
            outputVar = ReadAndWriteOutput.main()
            print(outputVar)
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
