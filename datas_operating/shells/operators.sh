#!/bin/bash

val=`expr 1 + 1`
echo "sum is ${val}"


a=10
b=20
val=`expr $b % $a`
echo "b % a: $val"

if [ $a == $b ]
then
  echo "a 等于 b"
else
  echo "a 不等于 b"
fi

