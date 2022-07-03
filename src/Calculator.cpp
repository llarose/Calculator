#include "../include/Calculator.h"
#include <iostream>
#include <math.h>
using namespace std;

float Calculator:: add(float x, float y)
{
   return x + y;
}


float Calculator:: sub(float x, float y)
{
   return x - y;
}

// Function to multiply two numbers
float Calculator::mul(float x, float y)
{
    return x * y;
}

// Function to divide two numbers
float Calculator::div(float x, float y)
{
    if (y == 0.0)
    {
        cout << "Division By Zero" <<
                    endl;
        return INFINITY;
    }
    else
    {
        return x / y;
    }
}