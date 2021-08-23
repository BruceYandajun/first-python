#!/bin/bash

my_array=(A B "C" D)
echo "第一个元素为: ${my_array[0]}"

echo "所有元素为: ${my_array[*]}"
echo "所有元素为: ${my_array[@]}"

echo "数组元素的个数为: ${#my_array[*]}"