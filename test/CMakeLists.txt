cmake_minimum_required(VERSION 3.8)

set(This test_CalculatorTests)

set(Sources
    test_CalculatorTests.cpp
)

add_executable(${This} ${Sources})
target_link_libraries(${This} PUBLIC
       gtest_main
       Calculator
)

add_test(
    NAME ${This}
    COMMAND ${This}
)