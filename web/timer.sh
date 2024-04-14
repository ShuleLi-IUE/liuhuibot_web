#!/bin/bash

while true; do
    date
    echo "rerun"
    # 运行需要定时执行的命令或脚本
    bash ./rerun.sh
    echo 
    echo "finish rerun, waiting ..."
    # 等待一段时间（例如一小时）
    sleep 3600  # 3600 秒 = 1 小时
done
