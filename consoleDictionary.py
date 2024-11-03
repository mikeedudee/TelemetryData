import datetime
import threading

class DateAndTime:
    current_time = datetime.datetime.now().strftime("%H:%M:%S]")
    today = datetime.datetime.now()
    day = today.day
    suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    formatted_date = today.strftime(f"[%d{suffix} of %B %Y — ")
    
    def DateAndTime():
        global dateTime
        dateTime = DateAndTime.formatted_date + DateAndTime.current_time
        return dateTime

def read_value_from_file():
    try:
        with open('dataBehavior.txt', 'r') as file:
            value = int(file.read().strip())
        return value
    except FileNotFoundError:
        print("dataBehavior.txt not found.")
        return None
    except ValueError:
        print("Invalid value in dataBehavior.txt.")
        return None

def TextDictionaryHandler(value_id):
    global dateTime
    id_to_text = {
        
        #GENERAL TERMS
        0000: f"{DateAndTime.DateAndTime()} -> IGNITION",
        1000: f"{DateAndTime.DateAndTime()} -> COUNTDOWN SEQUENCE INITIATED",
        1001: f"{DateAndTime.DateAndTime()} -> RUNNING EXTERNAL SYSTEM CHECK", 
        1002: f"{DateAndTime.DateAndTime()} -> EXTERNAL SYSTEM CHECK FINISHED",
        1003: f"{DateAndTime.DateAndTime()} -> INITIALIZING INTERNAL SYSTEMS",
        1004: f"{DateAndTime.DateAndTime()} -> INTERNAL SYSTEMS INITIALIZED",
        1005: f"{DateAndTime.DateAndTime()} -> GO FOR FLIGHT",
        1006: f"{DateAndTime.DateAndTime()} -> FLIGHT IN PROGRESS",
        1007: f"{DateAndTime.DateAndTime()} -> NO ACTION",
        1008: f"{DateAndTime.DateAndTime()} -> COUNTDOWN HALTED",
        
        #ERROR CODES
        1009: f"{DateAndTime.DateAndTime()} -> MAJOR - NO DATA TRANSMISSION FROM CANSAT",
        1010: f"{DateAndTime.DateAndTime()} -> CANSAT INTERNAL MEMORY NONFUNCTIONAL",
        1011: f"{DateAndTime.DateAndTime()} -> XBEE COMMUNICATION SLOW",
        1012: f"{DateAndTime.DateAndTime()} -> PS-1 MALFUNCTION",
        1013: f"{DateAndTime.DateAndTime()} -> PS-2 MALFUNCTION",
        1014: f"{DateAndTime.DateAndTime()} -> PS-3 MALFUNCTION",
        1015: f"{DateAndTime.DateAndTime()} -> NO GPS LOCATION DATA",
        1016: f"{DateAndTime.DateAndTime()} -> NO GPS DATE AND TIME DATA",
        1017: f"{DateAndTime.DateAndTime()} -> NO ATTITUDE DATA",
        1018: f"{DateAndTime.DateAndTime()} -> NO ACCELEROMETER DATA",
        1019: f"{DateAndTime.DateAndTime()} -> NO TEMPERATURE DATA",
        1020: f"{DateAndTime.DateAndTime()} -> CAMERA NONFUNCTIONAL",
        1021: f"{DateAndTime.DateAndTime()} -> XBEE DATA TRANSMISSION EXPIRED",
        1021: f"{DateAndTime.DateAndTime()} -> LAUNCH SCRUBBED",
        
        #SUCCES CODES
        1022: f"{DateAndTime.DateAndTime()} -> PS-1 READ.",
        1023: f"{DateAndTime.DateAndTime()} -> PS-2 READ.",
        1024: f"{DateAndTime.DateAndTime()} -> PS-3 READ.",
        1025: f"{DateAndTime.DateAndTime()} -> GYRO READINGS VALIDATED.",
        1026: f"{DateAndTime.DateAndTime()} -> CAMERA RUNNING.",
        1027: f"{DateAndTime.DateAndTime()} -> DATA COMMUNICATION UPLINK CONNECTED.",
        1028: f"{DateAndTime.DateAndTime()} -> INTERNAL MEMORY FUNCTIONAL.",
        1029: f"{DateAndTime.DateAndTime()} -> GPS LOCATION READ.",
        1030: f"{DateAndTime.DateAndTime()} -> GPS DATE AND TIME READ.",
        
        #CHECKING SYSTEM
        1031: f"{DateAndTime.DateAndTime()} -> PS-1 CHECKING READING.",
        1032: f"{DateAndTime.DateAndTime()} -> PS-2 CHECKING READING.",
        1033: f"{DateAndTime.DateAndTime()} -> PS-3 CHECKING READING.",
        1034: f"{DateAndTime.DateAndTime()} -> GPS DATA READING.",
        1035: f"{DateAndTime.DateAndTime()} -> CAMERA LINK CHECKING.",
        1036: f"{DateAndTime.DateAndTime()} -> COMMUNICATION UPLINK CHECKING.",
        1037: f"{DateAndTime.DateAndTime()} -> TESTING INTERNAL MEMORY STATUS (writing and reading something).",
        1038: f"{DateAndTime.DateAndTime()} -> COMMUNICATION UPLINK CHECKING.",
        1039: f"{DateAndTime.DateAndTime()} -> GYRO READING VALIDATING, PLEASE WAIT.",
        
        #LAUNCH PROGRESS CODES
        1041: f"{DateAndTime.DateAndTime()} -> LAUNCH SCRUBBED.",
        1042: f"{DateAndTime.DateAndTime()} -> TOO MANY SENSOR MALFUNCTION.",
        1043: f"{DateAndTime.DateAndTime()} -> SCRUBBING.",
        
        #ARMING PROCESS
        1050: f"{DateAndTime.DateAndTime()} -> EJECTION CHARGE ARMED.",
        1051: f"{DateAndTime.DateAndTime()} -> EJECTION CHARGE FIRED - EJECTED.",
        1052: f"{DateAndTime.DateAndTime()} -> DROGUE CHUTE DEPLOYED.",
        1053: f"{DateAndTime.DateAndTime()} -> MAIN CHUTE DEPLOYED.",
        1054: f"{DateAndTime.DateAndTime()} -> ROCKET COMPONENTS ARE COASTING",
        1055: f"{DateAndTime.DateAndTime()} -> CANSAT TOUCHEDDOWN"
    }
    
    return id_to_text.get(value_id, "UNLISTED HANDLER.")

import threading

def ConsoleTextHandler(value_id):
    #start_id = 1031
    #end_id   = 1037
    
    textHandled = TextDictionaryHandler(value_id)
    print(textHandled)
    if value_id == 1100:
        def print_message(key):
            #Get the text for each key and print it
            textHandled = TextDictionaryHandler(key)
            print(textHandled)
        
        for key in range(1031, 1039 + 1):
            # Set a delay for each message without freezing the main thread
            delay = (key - 1031) * 1  # 1-second intervals, you can adjust the multiplier for different timing
            threading.Timer(delay, print_message, [key]).start()

# Example usage
value = read_value_from_file()
ConsoleTextHandler(value)

