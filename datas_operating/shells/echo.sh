#!/bin/bash

echo -e "OK! \n" # -e 开启转义
echo "It is a test"


echo -e "OK! \c" # -e 开启转义 \c 不换行
echo "It is a test"

echo "It is a test" > test_file.txt

echo '$name\"' # 原样输出

echo `date`
