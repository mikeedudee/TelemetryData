# OutPutID.py

def read_value_from_file():
    
        with open('data.txt', 'r') as file:
            value = int(file.read().strip())
        return value
    #except FileNotFoundError:
    #    print("data.txt not found.")
    #    return None
    #except ValueError:
    #    print("Invalid value in data.txt.")
    #    return None

def check_value(value):
    id_dict = {
        101: "ID 101: Console initialized.",
        102: "ID 102: User logged in.",
        103: "ID 103: System error detected.",
        # Add more IDs and their associated messages here
    }
    
    return id_dict.get(value, "Unknown ID.")

def main():
    value = read_value_from_file()
    print(check_value(value))
