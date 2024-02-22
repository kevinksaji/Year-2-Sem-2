#!/bin/bash

# Define compiler commands and flags
GCC="gcc -Wall -Werror -Wextra -Wpedantic -Wstrict-prototypes -std=gnu11 -o manager"
GPP="g++ -Wall -Werror -Wextra -Wpedantic -std=c++17 -o prog"

# Compile the C code
$GCC manager.c

# Execute the program
./manager