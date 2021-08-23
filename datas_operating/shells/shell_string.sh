#!/bin/bash

my_name='Bruce'
echo $my_name

# 字符串拼接
echo "My name is '"${my_name}"'"
echo 'My name is "'$my_name'"'
echo "My name is \""$my_name"\""

# 字符串长度
echo ${#my_name}
# 截取字符串，第2个字符开始截取3个字符
echo ${my_name:1:3}

my_name=$my_name' Yan'
echo "$my_name"

my_name=$my_name' Dj'
echo "$my_name"
