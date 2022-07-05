cmake_minimum_required(VERSION 3.8)

set(This Calculator)

project (${This} C CXX)

set(CMAKE_CXX_STANDARAD 11)
set(CMAKE_POSITION_INDEPENDENT_CODE_ON)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")

set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

enable_testing()

add_subdirectory(googletest)

set(Headers
    include/Calculator.h
)

set(Sources
    src/Calculator.cpp
)

add_library(${This} STATIC src/Calculator.cpp include/Calculator.h)

add_subdirectory(test)

install(
    TARGETS Calculator
    DESTINATION /opt/Calculator/lib
    COMPONENT Calculator
)

install(
    FILES include/Calculator.h
    DESTINATION /opt/Calculator/include
    COMPONENT Calculator
)

SET(CPACK_GENERATOR "DEB")
SET(CPACK_DEBIAN_PACKAGE_MAINTAINER "KK") #required
INCLUDE(CPack)
