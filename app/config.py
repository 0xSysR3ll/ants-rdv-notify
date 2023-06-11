import yaml
import os
import sys


# This class handles the configuration file
class Config:
    # Initializes the class with the filename and an empty data dictionary
    def __init__(self, filename):
        self.filename = filename
        self.data = {}

    # Loads the data from the config file into the data dictionary
    def load(self):
        # If the file doesn't exist, the program exits
        if not os.path.isfile(self.filename):
            sys.exit(f"{self.filename} not found! Please add it and try again.")
        else:
            # Opens the file and loads the data into the dictionary
            with open(self.filename, 'r') as file:
                self.data = yaml.safe_load(file)

    # Returns the data from the specified key
    def get_config(self, key, value=None):
        if value is not None:
            return self.data[key][value]
        return self.data[key]