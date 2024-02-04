#!/bin/sh
GCC="gcc -Wall -Werror -Wextra -Wpedantic -Wstrict-prototypes -std=gnu11 -o "
GPP="g++ -Wall -Werror -Wextra -Wpedantic -std=c++17 -o "
BIN="../bin/"

mkdir ${BIN}
clear

rm ${BIN}hello
rm ${BIN}clk
rm ${BIN}clock
rm ${BIN}fork
rm ${BIN}fork2
rm ${BIN}kill
rm ${BIN}wait
rm ${BIN}waitpid
rm ${BIN}single_exec
rm ${BIN}multi_exec
rm ${BIN}pipe
rm ${BIN}shell
rm ${BIN}prog

$GCC ${BIN}hello hello.c
$GCC ${BIN}clk clk.c
$GCC ${BIN}clock clock.c
$GCC ${BIN}fork fork.c
$GCC ${BIN}fork2 fork2.c
$GCC ${BIN}kill kill.c
$GCC ${BIN}wait wait.c
$GCC ${BIN}waitpid waitpid.c
$GCC ${BIN}single_exec single_exec.c
$GCC ${BIN}multi_exec multi_exec.c
$GCC ${BIN}pipe pipe.c
$GCC ${BIN}shell shell.c
$GPP ${BIN}prog prog.cpp
