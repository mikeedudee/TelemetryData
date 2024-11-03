
# Placeholder for any key-value pairs or settings
config = {
    "APOGEE": 10000,
    "DURATION": 60,
    "UPDATE_INTERVAL": 0.1,
    "COUNTDOWN_TIME": 21
}

def get_config_value(key):
    """ Returns the value from config based on the key """
    return config.get(key, None)
