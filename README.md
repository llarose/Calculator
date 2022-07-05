# Calculator 


### Description of the Project
1. Create a Calculator library in C++
2. Integrate unit testing using googletest
3. Integrate cmake to 
   -  build the Calculator library 
   -  create a test executable(using googletest) that runs on the Calculator library 
4. Add a Python script to build the library, build test framework, run tests and 
add results in a csv file 

### Environment
IDE : VS code
Platform : Windows 


### Softwares/Tools to be installed
1. Download and Install cmake : https://cmake.org/download/
2. Install Visual Studio community : https://visualstudio.microsoft.com/fr/vs/community/

3. Clone googletest into the root directory : git clone https://github.com/google/googletest.git

### VS code settings
Install below plugins
1. C/C++ for Visual Studio Code
2. CMake Tools

### How to configure, build and run 
Configure : 
- After cloning the Calculator project and cloning googletest,  
VS code gives a choice to pick a kit for the compiler 
- Choose Visual Studio Community 
- The above step will configure the generator, detect the tools and builds the build system 

Build the libraries and test executable:
- Click on Build icon ( F7 windows) 
- This will execute cmake --build 
- Calculator.lib and the test_CalculatorTests.exe are generated 

Running the tests:
- Click on the icon Run CTests in VS code 

Running the tests in Terminal:
- execute cd "$(pwd)/build/test/Debug"
- Run the exe: test_CalculatorTests.exe 

########################################################################


### PYTHON SCRIPT 

1. Install Python 
2. Install pip

3. Open a command prompt and execute the following:
   pip install pytest-cpp,
   pip install pandas
   
4. Clone googletest into the roort directory
   git clone https://github.com/google/googletest.git
   
5. Run the script:
   python script.py 
   
6. The python script should be able to build the build system, Calculator.lib and
   test_CalculatorTests.exe and run the exe through pytest and add the test results in a csv
   at "$(pwd)/build/test/Debug"



 