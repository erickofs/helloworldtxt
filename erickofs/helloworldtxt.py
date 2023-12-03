"""Module to print a string from a text file in current directory. 
It trims string and file lines for comparison.
"""
import os

# Defining current script path
PATH = os.path.dirname(os.path.abspath(__file__)) + '\\'
print(PATH)

# User friendly input and error handling for constants
while True:
    try:
        FILENAME = str(input('The name of the text file to be searched (Current Dir.): '))
        if FILENAME == '':
            raise ValueError
        break
    except ValueError:
        print('Invalid input. Please enter a valid file name.')

while True:
    try:
        # This assumes we're looking for a .txt file. Can be changed to any file type.
        TXT_FLIE = PATH + FILENAME + '.txt'
        break
    except FileNotFoundError:
        print('File not found. Please enter a valid file.')

while True:
    try:
        TXT = str(input('Enter a string to search for (will be trimmed): '))
        if TXT == '':
            raise ValueError
        break
    except ValueError:
        print('Invalid input. Please enter a valid string.')

STRIPPED_TXT = TXT.strip()
file = open(TXT_FLIE, 'r+', encoding='utf-8')

# Main function
def print_string():
    """Function to print the inputed string from the selected text file in current directory."""
    with file as f:
        for line in f:
            line = line.strip()
            if STRIPPED_TXT in line:
                return print(STRIPPED_TXT)
            continue
        return print('String not found')

print_string()
