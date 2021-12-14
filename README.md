# Phoenix

A new reverse engineering, analysis, and transformation tool.

Uroboros: executable => assembly  
A2C:      assembly   => C  

## exe2c.sh

This script runs inside the docker (see the next section for the build instruction below).
It combines Uroboros and A2C for translating EXE to ASM and then to C.
It also compiles and runs the output C code.

It walks through the whole work flow:
C ---(gcc)--> EXE --(uroboros)--> ASM --(a2c)--> C --(gcc)--> EXE

## Docker

Uroboros is available as a docker image. 
Check the details in [Docker](Docker).

## Uroboros

(Python 2 and Ocaml)
python uroboros.py exe-file

(see README in the [Uroboros](uroboros) folder for the details.)

## A2C

(Python 3)
python3 a2c.py asm-file

(see README in the [A2C](a2c) folder for the details.)


## Analysis

to be integrated

## Transformation

to be integrated
