cmake_minimum_required(VERSION 3.16)

project(demo LANGUAGES C CXX)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

add_executable(demo
    src/Main.cpp
    src/glad.c
)

include_directories(include)

target_link_libraries(demo PRIVATE glad)
target_link_libraries(demo PRIVATE GLFW)