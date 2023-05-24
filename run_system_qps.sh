#!/bin/bash
n=5
for((j=1; j<=16; j=j*2))
do
  for i in `seq 1 $n`
  do
    if [ -f "/home/hucc/ray/python/record.txt" ];then
      rm -f /home/hucc/ray/python/record.txt
    fi
    python3.8 mul_request_iops_cir.py $j &> data/log_$j\_$i.txt
    sleep 10
  done
done
