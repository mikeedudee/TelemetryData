# variableDictionary.py

import LogConsoleModules

def PrepInternalSys():
    print("PREPARING INTERNAL SYSTEM")

def SysCheckFinish():
    print("SYSTEM CHECK FINISHED")

def GoForFlight():
    print("GO FOR FLIGHT — Internal System Initialized")

def default():
    print("ID not found")

# Dictionary mapping value IDs to corresponding functions
funcs = {
    101: PrepInternalSys,
    102: SysCheckFinish,
    103: GoForFlight
}

def check_variable_and_execute():
    var = LogConsoleModules.variableValue1
    func = funcs.get(var, default)
    func()

# Example usage
#if __name__ == "__main__":
check_variable_and_execute()

