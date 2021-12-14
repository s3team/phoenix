#!/bin/bash

# Usage: exe2c.sh foo.c

# works with the directory structure inside
# the default docker

workdir=$(pwd)
gcc -m32 -w -no-pie $1 -o $1.exe
cd ~/phoenix/uroboros/src
python uroboros.py "$workdir/$1.exe"
cp final.s "$workdir/$1.exe.s"
cd ~/phoenix/a2c/src
python3 a2c.py "$workdir/$1.exe.s"
cp output.c "$workdir/$1.exe.s.c"
cd $workdir
gcc -m32 -w -no-pie $1.exe.s.c -o $1.exe.s.c.exe
./$1.exe.s.c.exe
