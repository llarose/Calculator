
import os
import subprocess
import csv
from pathlib import Path
import pandas as pd

current_path = os.getcwd()

# cmake build : configure, generate and add build files in build directory

build_path = os.path.join(current_path, "build")
build = subprocess.run(['cmake', 'build'], stdout=subprocess.PIPE)

# Run cmake --build 
cmake_path = os.path.join(current_path, "build")
test = subprocess.run(['cmake', '--build', cmake_path], stdout=subprocess.PIPE)
print(test.stdout)

# Running the googletests : test_CalculatorTests.exe with pytest
test_path = os.path.join(current_path, "build\\test\\Debug")
os.chdir(test_path)

with open('output.txt', 'w') as f:
    test2 = subprocess.run(['pytest', '-v'], stdout=f)

read_file = pd.read_csv(r'output.txt', sep='\t')

# Adding the output of pytest into a csv file 
read_file.to_csv (r'File name.csv', index=None)

os.chdir(current_path)