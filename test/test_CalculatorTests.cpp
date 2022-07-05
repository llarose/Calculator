#include "../include/Calculator.h"
#include "math.h"
#include <gtest/gtest.h>


TEST(CalculatorTests, Addition){
    Calculator cal1;
    float x = 5;
    float y = 2;

    float sum = 7;
    
    float value = cal1.add(x,y);
    EXPECT_EQ(
        sum,
        value
    );
}

TEST(CalculatorTests, Subtraction){
    Calculator cal2;
    float x = 5;
    float y = 2;
    
    float sum = x - y;
    
    float value = cal2.sub(x,y);
    EXPECT_EQ(
        sum,
        value
    );
}

TEST(CalculatorTests, Multiplication){
    Calculator cal3;
    float x = 25.5;
    float y = 35;
    
    float ExpectedValue = x * y;
    
    float value = cal3.mul(x,y);
    EXPECT_EQ(
        ExpectedValue,
        value
    );
}

TEST(CalculatorTests, Division){
    Calculator cal4;
    float x = 100;
    float y = 35;
    
    float ExpectedValue = x / y;
    
    float value = cal4.div(x,y);
    EXPECT_EQ(
        ExpectedValue,
        value
    );
}

TEST(CalculatorTests, DivisionbyZero){
    Calculator cal5;
    float x = 100;
    float y = 0;
    
    float value = cal5.div(x,y);
    EXPECT_EQ(
        INFINITY,
        value
    );
}

TEST(CalculatorTests, Subtraction2){
    Calculator cal6;
    float x = 5;
    float y = 25;
    
    float sum = x - y;
    
    float value = cal6.sub(x,y);
    EXPECT_EQ(
        sum,
        value
    );
}