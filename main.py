import json
import os
# Step 1: Create a main function
def main():
    file_path = './data.json'
    # Read in data.json file
    if os.path.isfile(file_path):
        with open(file_path, 'r') as data_json:
            print(data_json)

    else: 
        print('Error data file not found')
