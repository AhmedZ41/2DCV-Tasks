cmake_minimum_required(VERSION 3.5)
project(sobel_demo)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_PREFIX_PATH "/usr/local/opt/pybind11/share/cmake/pybind11")

# Add Eigen include manually
include_directories("/usr/local/include/eigen3")

find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

add_library(sobel_demo MODULE sobel_demo.cpp)
target_link_libraries(sobel_demo PRIVATE Python3::Python pybind11::module)
