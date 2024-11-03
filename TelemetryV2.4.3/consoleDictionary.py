# variableDictionary.py

def read_value_from_file():
    try:
        with open('dataBehavior.txt', 'r') as file:
            value = int(file.read().strip())
        return value
    except FileNotFoundError:
        print("data.txt not found.")
        return None
    except ValueError:
        print("Invalid value in data.txt.")
        return None

def TextDictionaryHandler(value_id):
    id_to_text = {
        1001: "RUNNING EXTERNAL SYSTEM CHECK", 
        1002: "EXTERNAL SYSTEM CHECK FINISHED",
        1003: "INITIALIZING INTERNAL SYSTEMS",
        1004: "INTERNAL SYSTEMS INITIALIZED",
        1005: "GO FOR FLIGHT",
        1006: "FLIGHT IN PROGRESS",
        1007: "NO ACTION",
        1008: "COUNTDOWN HALTED",
    }
    
    return id_to_text.get(value_id, "UNLISTED HANDLER.")

def ConsoleTextHandler(value_id):
    # Get the text from ConsoleDictionaryHandler
    global textHandled 
    textHandled = TextDictionaryHandler(value_id)
    if value is not None:
        print(textHandled)
    
value = read_value_from_file()
ConsoleTextHandler(value)