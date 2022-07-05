
import os
import subprocess
import csv
from pathlib import Path
import pandas as pd

current_path = os.getcwd()

# cmake -S . -B build : Create a build folder if needed, configure, generate and add build files in build directory
build = subprocess.run(['cmake', '-S', '.', '-B', 'build' ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(build.stdout)
if build.returncode != 0:
    print(f"Unable to build the build system")
else:
    print(f"cmake build successful \n \n")


# Run cmake --build 
cmake_path = os.path.join(current_path, "build")
test = subprocess.run(['cmake', '--build', cmake_path], stdout=subprocess.PIPE)
print(test.stdout)
if test.returncode != 0:
    print(f"Unable to build")
else:
    print(f"cmake --build successful \n \n")


# Running the googletests : test_CalculatorTests.exe with pytest
print(f"Running tests in googletest through pytest")
test_path = os.path.join(current_path, "build/test/")
os.chdir(test_path)

with open('output.txt', 'w') as f:
    test2 = subprocess.run(['pytest', '-v'], stdout=f)

read_file = pd.read_csv(r'output.txt', sep='\t')

# Adding the output of pytest into a csv file 
read_file.to_csv (r'Test_Results.csv', index=None)
print(f"The test results have been stored in ../build/test/Debug folder \n \n")

os.chdir(current_path)