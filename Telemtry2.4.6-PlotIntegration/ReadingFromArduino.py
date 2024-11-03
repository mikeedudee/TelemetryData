import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1) 
time.sleep(2) 

def read_data():
    if ser.in_waiting > 0:
        try:
            data = ser.readline().decode('utf-8').strip() 
            data_values = data.split(",") 
            return data_values
        except Exception as e:
            print(f"Error reading data: {e}")
            return None

while True:
    data = read_data()
    if data:
        # Accessing the a specific value from the array
        temperature = data[0]
        pressure = data[1]
        altitude = data[2]
        # ... Access other data as needed
        
        print(f"Temperature: {temperature} °C, Pressure: {pressure} Pa, Altitude: {altitude} m")
        
        # PLOTTING AREA 

    time.sleep(1) 
