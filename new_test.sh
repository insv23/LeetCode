#!/bin/bash

# 检查是否传入目录路径
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# 跳转到指定目录
cd "$1"

# 初始化文件编号
file_num=1

# 循环检查文件是否存在，如果存在则递增编号
while true; do
    if [[ -f "${file_num}.in.txt" ]] || [[ -f "${file_num}.out.txt" ]] || [[ -f "${file_num}.ans.txt" ]]; then
        ((file_num++))
    else
        break
    fi
done

# 创建文件
touch "${file_num}.in.txt"
touch "${file_num}.ans.txt"

echo "已创建文件：${file_num}.in.txt, ${file_num}.ans.txt"