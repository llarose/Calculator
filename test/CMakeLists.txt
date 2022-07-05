cmake_minimum_required(VERSION 3.8)

set(This test_CalculatorTests)

set(Sources
    test_CalculatorTests.cpp
)

set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

add_executable(${This} ${Sources})
target_link_libraries(${This} PUBLIC
       gtest_main
       Calculator
)

add_test(
    NAME ${This}
    COMMAND ${This}
)

install(
    PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/test_CalculatorTests
    DESTINATION /opt/Calculator/bin
    COMPONENT Calculator
)