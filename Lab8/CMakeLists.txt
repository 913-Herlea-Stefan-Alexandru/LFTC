cmake_minimum_required(VERSION 3.17)
project(Lab8 C)

set(CMAKE_C_STANDARD 99)

add_executable(Lab8 main.c lex.yy.c y.tab.c)