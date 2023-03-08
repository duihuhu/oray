#!/bin/bash
n=100
for i in `seq 1 $n`
do
    python3.8 example.py &
done
