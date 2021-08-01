cmake_minimum_required(VERSION 3.16)
project(basecode C)

set(CMAKE_C_STANDARD 11)

include_directories(src)

add_executable(basecode
        src/ai.c
        src/ai.h
        src/hashtable.c
        src/hashtable.h
        src/layouts.h
        src/list.c
        src/list.h
        src/stack.c
        src/stack.h
        src/utils.c
        src/utils.h
        peg_solitaire.c)
