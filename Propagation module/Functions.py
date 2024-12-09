import numpy as np
import csv

# Function to print text in different colors
def print_in_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

# Function to read debris coordinates in a csv file, an add them to an array
def read_debris(file_path):
    debris_positions = [] # Creating an array that will contain all the debris coordinates
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header (Usually there is one at the first row)
        for row in reader:
            # Add a [x, y, z] to the debris_positions
            debris_positions.append([float(row[1]), float(row[2]), float(row[3])]) # (Adjust, depend of the x, y, z positions in the csv file)
    return debris_positions

# Function to calculate the euclid distance between two vectors
def calculate_distance(vec1, vec2):
    return np.linalg.norm(np.array(vec1) - np.array(vec2))
